import React, { useContext, useState } from 'react';
import AuthContext from '../../contexts/auth.context';
import styled from 'styled-components';
import Button from '../button/button';
import Input from '../input/input';
import Banner from '../banner/banner';
import useHttp from '../../hooks/http.hook';
import md5 from 'md5';
import authBackground from '../../assets/auth.png';
import { METHODS } from '../../constants/methods.contants';
import { passwordReg } from '../../constants/authorization.constants';

const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${authBackground}) no-repeat;
  background-size: cover;
`;

const Form = styled.form`
  padding: 30px 10px;
  display: flex;
  flex-flow: column;
`;

const ControlButtons = styled.div`
  margin-top: 40px;
  display: flex;
  flex-flow: column;
`;

const Authorization = () => {
  const { request } = useHttp();
  const { login } = useContext(AuthContext);
  const [form, setForm] = useState({ login: '', password: '' });
  const [error, setError] = useState('');

  const isValidPassword = () => {
    return passwordReg.test(
      form.password,
    );
  };

  const handleChange = ({ target }) => {
    setForm({
      ...form,
      [target.name]: target.value,
    });
  };

  const handleLogin = async (event) => {
    try {
      event.preventDefault();
      setError('');
      if (isValidPassword()) {
        const random = Math.random();
        const hash = md5(md5(form.password + form.login) + random);
        const data = await request(
          'http://localhost:8080/api/auth',
          METHODS.POST,
          {
            login: form.login,
            hash,
            random,
          },
        );
        login(data.token);
      }
    } catch (err) {
      setError(err.message);
    }
  };

  const handleSignup = async (event) => {
    try {
      event.preventDefault();
      if (form.login && isValidPassword()) {
        const hash = md5(form.password + form.login);
        const data = await request(
          'http://localhost:8080/api/signup',
          METHODS.POST,
          {
            login: form.login,
            hash,
          },
        );
        login(data.token);
      }
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <Container>
      <Form>
        <Banner />
        <Input
          id="login"
          type="text"
          placeholder="Логин"
          name="login"
          aria-label="login"
          aria-describedby="login"
          required
          autoComplete="username"
          autoFocus
          onChange={handleChange}
        />
        <Input
          id="password"
          type="password"
          placeholder="Пароль"
          name="password"
          aria-label="password"
          aria-describedby="password"
          required
          autoComplete="current-password"
          onChange={handleChange}
          onFocus={(event) => event.target.select()}
        />
        <ControlButtons>
          <Button type="submit" onClick={handleLogin}>Авторизоваться</Button>
          <Button type="submit" onClick={handleSignup}>Зарегистрироваться</Button>
        </ControlButtons>
      </Form>
    </Container>
  );
};

export default Authorization;

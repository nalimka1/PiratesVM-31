import React, { useContext, useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import styled from 'styled-components';
import Button from '../button/button';
import Input from '../input/input';
import Messages from '../messages/messages';
import AuthContext from '../../contexts/auth.context';
import { addMessages, sendMessage } from '../../redux/actions/chat.actions';
import { selectMessages } from '../../redux/selectors/chat.selectors';
import socket from '../../helpers/socket';
import { SOCKET_EVENTS } from '../../constants/socket.constants';

const StyledChat = styled.div`
  padding: 20px 10px;
  width: 100%;
  height: 100%;
  max-width: 700px;
  max-height: 700px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-flow: column;
`;

const StyledForm = styled.form`
  width: 100%;
  display: flex;
`;

const Chat = () => {
  const [message, setMessage] = useState('');
  const { token } = useContext(AuthContext);
  const messages = useSelector(selectMessages);
  const dispatch = useDispatch();

  useEffect(() => {
    const subscribeToMessages = (newMessages) => dispatch(addMessages(newMessages));
    socket.on(SOCKET_EVENTS.SEND_MESSAGE, subscribeToMessages);
    return () => {
      socket.off(SOCKET_EVENTS.SEND_MESSAGE, subscribeToMessages);
    };
  }, []);

  const handleInputChange = ({ target }: React.ChangeEvent<HTMLInputElement>) => {
    setMessage(target.value);
  };

  const handleSendMessage = () => {
    if (token && message.trim().length) {
      setMessage('');
      dispatch(sendMessage(socket, { token, message }));
    }
  };

  const handleFormSubmit = (event: React.FormEvent<HTMLFormElement>) => event.preventDefault();

  return (
    <StyledChat>
      <Messages messages={messages} />
      <StyledForm onSubmit={handleFormSubmit} className="send-message">
        <Input
          id="send-message"
          type="text"
          name="message"
          value={message}
          onChange={handleInputChange}
          placeholder="Введите сообщение"
          autoComplete="off"
        />
        <Button type="submit" onClick={handleSendMessage}>{'>'}</Button>
      </StyledForm>
    </StyledChat>
  );
};

export default Chat;

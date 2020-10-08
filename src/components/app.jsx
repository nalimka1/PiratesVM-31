import React from 'react';
import { BrowserRouter as Router, Redirect, Route, Switch } from 'react-router-dom';
import AuthContext from '../contexts/auth.context';
import Authorization from './authorization/authorization';
import useAuth from '../hooks/auth.hook';
import { AUTH_URL } from '../constants/url.constants';
import { ThemeProvider } from 'styled-components';

const theme = {
  fg: '#ffe190',
  fgError: '#eed4d4',
  bg: '#237773',
  bgActive: '#6fb38e',
};

const App = () => {
  const auth = useAuth();
  const isAuth = !!auth.token;

  return (
    <Router>
      <ThemeProvider theme={theme}>
        <AuthContext.Provider value={auth}>
          {!isAuth && <Redirect to={AUTH_URL}/>}
          <Switch>
            <Route>
              <Authorization/>
            </Route>
          </Switch>
        </AuthContext.Provider>
      </ThemeProvider>
    </Router>
  );
};

export default App;

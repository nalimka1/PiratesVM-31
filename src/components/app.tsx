import React from 'react';
import { BrowserRouter as Router, Redirect, Route, Switch } from 'react-router-dom';
import AuthContext from '../contexts/auth.context';
import Authorization from './authorization/authorization';
import useAuth from '../hooks/auth.hook';
import { AUTH_URL, LOBBY_URL } from '../constants/url.constants';
import { ThemeProvider, DefaultTheme } from 'styled-components';
import ErrorBoundary from './error-boundary/error-boundary';
import Lobby from './lobby/lobby';

const theme: DefaultTheme = {
  fg: '#ffe190',
  fgError: '#d4eee8',
  bg: '#237773',
  bgActive: '#6fb38e',
};

const App = () => {
  const auth = useAuth();
  const isAuth = !!auth.token;

  return (
    <Router>
      <ThemeProvider theme={theme}>
        <ErrorBoundary>
          <AuthContext.Provider value={auth}>
            {!isAuth ? <Redirect to={AUTH_URL}/> : <Redirect to={LOBBY_URL} />}
            <Switch>
              <Route path={AUTH_URL}>
                <Authorization />
              </Route>
              <Route path={LOBBY_URL}>
                <Lobby />
              </Route>
            </Switch>
          </AuthContext.Provider>
        </ErrorBoundary>
      </ThemeProvider>
    </Router>
  );
};

export default App;

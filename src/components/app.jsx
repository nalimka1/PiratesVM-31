import React from 'react';
import { BrowserRouter as Router, Redirect, Route, Switch } from 'react-router-dom';
import AuthContext from '../contexts/auth.context';
import Authorization from './authorization/authorization';
import useAuth from '../hooks/auth.hook';
import { AUTH_URL } from '../constants/url.constants';
import { ThemeProvider } from 'styled-components';
import ErrorBoundary from './error-boundary/error-boundary';

const theme = {
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
          {!isAuth && <Redirect to={AUTH_URL}/>}
          <Switch>
            <Route>
              <Authorization/>
            </Route>
          </Switch>
        </AuthContext.Provider>
        </ErrorBoundary>
      </ThemeProvider>
    </Router>
  );
};

export default App;

import React from 'react';
import { BrowserRouter as Router, Route, Redirect, Switch } from 'react-router-dom';
import AuthContext from '../contexts/auth.context';
import Authorization from './authorization/authorization';
import useAuth from '../hooks/auth.hook';
import { AUTH_URL } from '../constants/url.constants';

const App = () => {
  const auth = useAuth();
  const isAuth = !!auth.token;

  return (
    <Router>
      <AuthContext.Provider value={auth}>
        {!isAuth && <Redirect to={AUTH_URL} />}
        <Switch>
          <Route>
            <Authorization />
          </Route>
        </Switch>
      </AuthContext.Provider>
    </Router>
  );
};

export default App;

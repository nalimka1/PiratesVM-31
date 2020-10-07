import { createContext } from 'react';

const AuthContext = createContext({
  token: '',
  login: () => {},
  logout: () => {},
  signup: () => {},
});

export default AuthContext;

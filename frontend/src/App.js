import React from 'react';
import Login from './components/auth/Login';
import Signup from './components/auth/Signup';
import logo from './logo.svg';

import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
// import Login from './components/auth/Login'
// import Requests from './components/Requests'
//import './App.css';

function App() {
  return (
    <div>
      {/* <p>Placeholder</p> */}
      <BrowserRouter>
        <Routes>
          {/* Default Route to Login Page */}
          <Route path='/' element={<Navigate to='/requests' />} />

          {/* Login page route */}
          {<Route path='/login' element={<Login />} /> }

          {/* Signup page route */}
          {<Route path='/signup' element={<Signup />} /> }

          {/* Home page  */}
          {/* <Route path='/home' element={} /> */}

        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
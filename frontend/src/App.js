import logo from './logo.svg';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
// import Login from './components/auth/Login'
import Requests from './components/Requests'
//import './App.css';
import Home from './components/Home'

function App() {
  return (
    <div>
      {/* <p>Placeholder</p> */}
      <BrowserRouter>
        <Routes>
          {/* Default Route to Login Page */}
          <Route path='/' element={<Navigate to='/home' />} />

          {/* Login page route */}
          {/* <Route path='/login' element={<Login />} /> */}

          {/* Home page  */}
          <Route path='/home' element={<Home />} />

          {/* Requests received page */}
          <Route path='/requests' element={<Requests />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

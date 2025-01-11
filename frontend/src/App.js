import logo from './logo.svg';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
// import Login from './components/auth/Login'
import Requests from './components/Requests'
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
          {/* <Route path='/login' element={<Login />} /> */}

          {/* Home page  */}
          {/* <Route path='/home' element={} /> */}

          {/* Requests received page */}
          <Route path='/requests' element={<Requests />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

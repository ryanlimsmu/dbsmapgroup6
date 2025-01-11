import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom'; // Import Link for navigation
import '../../css/Login.css'; // Import the CSS for styling
import InputField from './InputField';
import userService from '../../services/login';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [usernameError, setUsernameError] = useState(false);
  const [passwordError, setPasswordError] = useState(false);
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();

    const userCredentials = {username, password};
    console.log('Logging in with:', { username, password });

    // call the login user API
    userService.loginUser(userCredentials)
    .then(result => {
      // navigate to home page if successful
      console.log(result);
      const jwt_token = result.data.data.accessToken;

      if (jwt_token) {
        sessionStorage.setItem('jwt_token', jwt_token);
        navigate('/home');
      } else {
        setError('Token not found, authentication failed.');
      }
      
    })
    .catch(e => {
      // handle errors here 
      if (e.response) {
        switch (e.response.status) {
          case 400:
            setError(e.response.data.message); // Missing email and/or password
            setUsernameError(true);
            setPasswordError(true);
            break;
          case 401:
            setError(e.response.data.message); // Wrong email and/or password
            setUsernameError(true);
            setPasswordError(true); 
            break;
          case 500:
            setError(e.response.data.message); // Database or server error 
            break;
          default:
            setError("An unexpected error occurred.");
            break;
        }
      } else {
        setError("Network error. Please check your connection.");
      }
    })
  };

  return (
    <div className="login-container">
      <div className="left-side">
        <h1 className="title">DBS Techtrek 2025</h1>
        <h2 className="subtitle">Sign In</h2>
      </div>
      <div className="right-side">
        <div className="input-container">
          <form onSubmit={handleLogin}>
            <div>
              <InputField 
              label="Company User Name" 
              type="text" 
              placeholder="Enter your company user name" 
              onChange={(e) => {
                setUsername(e.target.value)
                setUsernameError(false);
              }}
              error={usernameError}
              required
              />
              <InputField label="Password" 
              type="password" 
              placeholder="Enter your password" 
              onChange={(e) => {
                setPassword(e.target.value)
                setPasswordError(false)
              }}
              error={passwordError}
              required
              />
            </div>
            <div className="button-container">
              <Link to="/signup" className="create-account-link">Create Account</Link>
              <button type="submit" className="login-button">Sign In</button>
            </div>
          </form>
          <div className='notification'>
              {error && <p className="text-danger mt-3">{error}</p>}
            </div>
        </div>
      </div>
    </div>

    
  );
};

export default Login;

import React from 'react';
import { Link } from 'react-router-dom';
import '../../css/Navbar.css';
import logo from '../../DBS.png';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <img src={logo} alt="DBS Logo" className="navbar-logo" />
      </div>
      <div className="navbar-center">
        <Link to="/requests" className="navbar-link">Requests</Link>
      </div>
      <div className="navbar-right">
        <button className="navbar-button" onClick={() => alert('Logging out...')}>
          Logout
        </button>
      </div>
    </nav>
  );
};

export default Navbar;

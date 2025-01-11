import React, { useState, useEffect } from 'react';
import Navbar from '../components/auth/requests/Navbar';
import Balance from '../components/auth/requests/Balance';

function landing() {
    return (
        <div>
            <Navbar />
            <Balance />
        </div>
    )
}

export default landing;
import React, { useState, useEffect } from 'react';
import Navbar from '../components/requests/Navbar';
import Balance from '../components/requests/Balance';

function landing() {
    return (
        <div>
            <Navbar />
            <Balance />
        </div>
    )
}

export default landing;
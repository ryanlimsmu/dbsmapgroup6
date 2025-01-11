import React from 'react';
import './Balance.css';

const Balance = ({ carbonBalance, cashBalance }) => {
  return (
    <div className="balance-container">
      <div className="balance-label">Balance</div>
      <div className="balance-values">
        <div className="balance-item">
          <strong>Carbon:</strong> {carbonBalance} kg CO₂
        </div>
        <div className="balance-item">
          <strong>Cash:</strong> ${cashBalance}
        </div>
      </div>
    </div>
  );
};

export default Balance;

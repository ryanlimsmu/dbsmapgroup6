import React from 'react';
import '../../css/Balance.css';

const Balance = ({ carbonBalance, cashBalance }) => {
  return (
    <div className="balance-container">
      <div className="balance-label">Balance</div>
      <div className="balance-values">
        <div className="balance-item">
          <strong>Carbon:</strong> {carbonBalance ? carbonBalance > 0 : 0} kg CO₂
        </div>
        <div className="balance-item">
          <strong>Cash:</strong> ${cashBalance ? cashBalance : 0}
        </div>
      </div>
    </div>
  );
};

export default Balance;

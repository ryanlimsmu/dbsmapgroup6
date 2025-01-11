import React, { useState } from 'react';
import '../../css/AddForm.css'; // Import the CSS for styling

const AddForm = ({ onSubmit, closeModal }) => {
  const [newRow, setNewRow] = useState({
    request_date: '',
    company_name: '',
    carbon_price: '',
    carbon_qty: '',
    requesting_reason: '',
    request_type: '',
  });

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setNewRow({
      ...newRow,
      [name]: value,
    });
  };

  // Handle form submit
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(newRow);
  };

  return (
    <div className="modal">
      <div className="modal-content">
        <h2>Add New Row</h2>
        <form onSubmit={handleSubmit} className="add-form">
          <div className="form-field">
            <label htmlFor="request_date">Request Date</label>
            <input
              type="text"
              name="request_date"
              id="request_date"
              value={newRow.request_date}
              onChange={handleChange}
            />
          </div>

          <div className="form-field">
            <label htmlFor="company_name">Company Name</label>
            <input
              type="text"
              name="company_name"
              id="company_name"
              value={newRow.company_name}
              onChange={handleChange}
            />
          </div>

          <div className="form-field">
            <label htmlFor="carbon_price">Carbon Price</label>
            <input
              type="number"
              name="carbon_price"
              id="carbon_price"
              value={newRow.carbon_price}
              onChange={handleChange}
            />
          </div>

          <div className="form-field">
            <label htmlFor="carbon_qty">Carbon Quantity</label>
            <input
              type="number"
              name="carbon_qty"
              id="carbon_qty"
              value={newRow.carbon_qty}
              onChange={handleChange}
            />
          </div>

          <div className="form-field">
            <label htmlFor="requesting_reason">Requesting Reason</label>
            <input
              type="text"
              name="requesting_reason"
              id="requesting_reason"
              value={newRow.requesting_reason}
              onChange={handleChange}
            />
          </div>

          <div className="form-field">
            <label htmlFor="request_type">Request Type</label>
            <input
              type="text"
              name="request_type"
              id="request_type"
              value={newRow.request_type}
              onChange={handleChange}
            />
          </div>

          <div className="form-buttons">
            <button type="submit">Add Row</button>
            <button type="button" onClick={closeModal}>
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AddForm;

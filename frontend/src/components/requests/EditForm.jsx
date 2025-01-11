import React, { useState } from 'react';
import '../../css/EditForm.css';

const EditForm = ({ request, onSubmit, closeModal }) => {
  const [formData, setFormData] = useState(request);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData); // Send updated data back to Home.jsx
    closeModal(); // Close the modal after submission
  };

  return (
    <div className="modal-overlay">
      <div className="modal">
        <h2>Edit Request</h2>
        <form onSubmit={handleSubmit}>
          <label>
            Request Date:
            <input
              type="text"
              name="request_date"
              value={formData.request_date}
              onChange={handleChange}
            />
          </label>
          <label>
            Company Name:
            <input
              type="text"
              name="company_name"
              value={formData.company_name}
              onChange={handleChange}
            />
          </label>
          <label>
            Carbon Price:
            <input
              type="number"
              name="carbon_price"
              value={formData.carbon_price}
              onChange={handleChange}
            />
          </label>
          <label>
            Carbon Quantity:
            <input
              type="number"
              name="carbon_qty"
              value={formData.carbon_qty}
              onChange={handleChange}
            />
          </label>
          <label>
            Requesting Reason:
            <input
              type="text"
              name="requesting_reason"
              value={formData.requesting_reason}
              onChange={handleChange}
            />
          </label>
          <label>
            Request Type:
            <input
              type="text"
              name="request_type"
              value={formData.request_type}
              onChange={handleChange}
            />
          </label>
          <button type="submit">Save Changes</button>
          <button type="button" onClick={closeModal}>Cancel</button>
        </form>
      </div>
    </div>
  );
};

export default EditForm;

import React, { useState } from 'react';
import ReqTable from './requests/ReqTable';
import Navbar from './requests/Navbar';
import Balance from './requests/Balance';
import AddForm from './requests/AddForm'; // Import AddForm component

const Home = () => {
  const [requests, setRequests] = useState([
    {
      id: 1,
      request_date: "11/07/2020",
      company_name: "ABC",
      carbon_price: 11,
      carbon_qty: 13,
      requesting_reason: "ABCD",
      request_type: "Buy",
    },
  ]);
  const [showAddModal, setShowAddModal] = useState(false); // State to manage Add modal visibility

  // Handle adding a new row
  const handleAddSubmit = (newRow) => {
    setRequests((prevRequests) => [
      ...prevRequests,
      { ...newRow, id: prevRequests.length + 1 },
    ]);
    setShowAddModal(false); // Close the modal after submission
  };

  // Function to handle deleting a row
  const handleDelete = (id) => {
    const filteredRequests = requests.filter((request) => request.id !== id);
    setRequests(filteredRequests); // Update state by removing the selected row
  };

  // Function to close the modal
  const closeAddModal = () => {
    setShowAddModal(false); // Close modal without adding anything
  };

  return (
    <div>
      <Navbar />
      <Balance />
      <button
        className="navbar-button"
        onClick={() => setShowAddModal(true)} // Trigger Add Modal
      >
        Add New Row
      </button>
      <ReqTable
        isHomePage={true}
        requests={requests}
        onDelete={handleDelete} // Pass the delete function as a prop
      />
      {showAddModal && (
        <AddForm onSubmit={handleAddSubmit} closeModal={closeAddModal} />
      )}
    </div>
  );
};

export default Home;

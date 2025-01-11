import React from 'react';

const HomeButton = ({ onDelete }) => {
  const handleDelete = () => {
    const confirmDelete = window.confirm("Are you sure you want to delete this request?");
    if (confirmDelete) {
      onDelete(); // Proceed with deletion if confirmed
    }
  };

  return (
    <div>
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        <button style={{ color: 'blue' }}type='button'>Edit</button>
        <button style={{ color: 'red' }}type='button'>Delete</button>
=======
=======
>>>>>>> Stashed changes
      <button style={{ backgroundColor: 'blue' }} type="button">
        Edit
      </button>
      <button
        style={{ backgroundColor: 'red' }}
        type="button"
        onClick={handleDelete} // Trigger delete with confirmation
      >
        Delete
      </button>
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
    </div>
  );
};

export default HomeButton;

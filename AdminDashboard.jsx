import React from 'react';
import "./AdminDashboard.css"; // Import CSS file for styling

function AdminDashboard({ user, handleLogout, handleExit }) {

  return (
    <div className="admin-dashboard-container">
      <h2>Welcome{user.name}!</h2>
      <h3>Admin Dashboard</h3>
      <ul className="options-list">
        <li>Admin Summary</li>
        <li>User Summary</li>
        <li onClick={handleLogout}>Logout</li>
        <li onClick={handleExit}>Exit</li>
      </ul>
    </div>
  );
}

export default AdminDashboard;

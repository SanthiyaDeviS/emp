// UserSummary.jsx

import React from 'react';
import "./UserDashboard.css"; // Import CSS file for styling

function UserDashboard({ handleLogout, handleExit }) {
  return (
    <div className="user-summary-container">
      <h2>Welcome!</h2>
      <h2>User Dashboard</h2>
      <ul className="options-list">
        <li>User Summary</li>
        <li onClick={handleLogout}>Logout</li>
        <li onClick={handleExit}>Exit</li>
      </ul>
    </div>
  );
}

export default UserDashboard;

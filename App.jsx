// App.jsx

import React, { useState } from "react";
import Login from "./components/Login.jsx"; // Ensure correct capitalization
import AdminDashboard from "./components/AdminDashboard.jsx";
import UserDashboard from "./components/UserDashboard.jsx";
import userCredentials from "./data/user_credentials.json";
function App() {
  const [loggedInUser, setLoggedInUser] = useState(null);

  return (
    <div>
      {!loggedInUser ? (
        <Login setLoggedInUser={setLoggedInUser} />
      ) : loggedInUser.is_admin ? (
        <AdminDashboard
          user={loggedInUser}
          handleLogout={() => setLoggedInUser(null)}
          handleExit={() => window.close()}
        />
      ) : (
        <UserDashboard
          user={loggedInUser}
          handleLogout={() => setLoggedInUser(null)}
          handleExit={() => window.close()}
        />
      )}
    </div>
  );
}

export default App;

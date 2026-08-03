import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Signup from './pages/Signup';
import Login from './pages/Login';
import ProfileWizard from './pages/ProfileWizard';
import Catalog from './pages/Catalog';

function App() {
  return (
    <BrowserRouter>
      <div style={{ padding: '20px' }}>
        <nav style={{ marginBottom: '20px' }}>
          <Link to="/login" style={{ marginRight: '10px' }}>Login</Link>
          <Link to="/signup" style={{ marginRight: '10px' }}>Signup</Link>
          <Link to="/catalog">Catalog</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/profile-wizard" element={<ProfileWizard />} />
          <Route path="/catalog" element={<Catalog />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;

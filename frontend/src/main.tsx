import { createRoot } from 'react-dom/client';
import { StrictMode } from 'react';
// Context Providers
import { KGInfoProvider } from './context/kgInfo.tsx';
import { UserInfoProvider } from './context/userInfo.tsx';
// Routing for page redirection
import { BrowserRouter as BrowserRouter, Route, Routes } from 'react-router-dom';
// Components
import App from './login.tsx';  // Login/ID Search Page
import StudentDashboard from './student.tsx';  // Student Dashboard Page
import AdminDashboard from './admin.tsx';
// Global CSS styles for antd components
import 'antd/dist/reset.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <UserInfoProvider>
        <KGInfoProvider>
          <Routes>
            <Route path="/" element={<App />} />
            <Route path="/student" element={<StudentDashboard />} />
            <Route path="/admin" element={<AdminDashboard />} />
          </Routes>
        </KGInfoProvider>
      </UserInfoProvider>
    </BrowserRouter>
  </StrictMode>

)

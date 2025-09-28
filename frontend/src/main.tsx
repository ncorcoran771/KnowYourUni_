import { createRoot } from 'react-dom/client';
import { StrictMode } from 'react';
// Context Providers
import { KGInfoProvider } from './context/KGInfoProvider.tsx';
import { UserInfoProvider } from './context/UserInfoProvider.tsx';
import { ThemeConfigProvider } from './context/ThemeProvider.tsx';
// Routing for page redirection
import { BrowserRouter as BrowserRouter, Route, Routes } from 'react-router-dom';
// Components
import App from './login.tsx';  // Login/ID Search Page
import StudentDashboard from './student.tsx';  // Student Dashboard Page
import AdminDashboard from './admin.tsx';
// Global CSS styles for antd components
import 'antd/dist/reset.css';

// Render the application
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <ThemeConfigProvider>
        <UserInfoProvider>
          <KGInfoProvider>
            <Routes>
              <Route path="/" element={<App />} />
              <Route path="/student" element={<StudentDashboard />} />
              <Route path="/admin" element={<AdminDashboard />} />
            </Routes>
          </KGInfoProvider>
        </UserInfoProvider>
      </ThemeConfigProvider>
    </BrowserRouter>
  </StrictMode>

)

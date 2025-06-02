import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './utils/authContext';
import { ProtectedRoute } from './utils/protected-route';

import Login from './pages/login';
import Menu from './pages/menu';
import Institutions from './pages/institutions';
import InstitutionFloors from './pages/institutionFloors';

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route
            path='/'
            element={
              <ProtectedRoute>
                <Menu />
              </ProtectedRoute>
            }
          />
          <Route path='/login' element={<Login />} />
          <Route
            path='/institutions'
            element={
              <ProtectedRoute>
                <Institutions />
              </ProtectedRoute>
            }
          />
          <Route
            path='/institutions/:slug'
            element={
              <ProtectedRoute>
                <InstitutionFloors />
              </ProtectedRoute>
            }
          />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

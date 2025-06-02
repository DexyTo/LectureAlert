import { Navigate } from 'react-router-dom';
import { useAuth } from './authContext';

export function ProtectedRoute({ children }) {
  const { user } = useAuth();
  return user ? children : <Navigate to="/login" />;
}
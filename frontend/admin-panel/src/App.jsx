import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/login';
import Dashboard from './pages/dashboard';
import Menu from './pages/menu';
import Institutions from './pages/institutions';
import InstitutionFloors from './pages/institutionFloors';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Menu />} />
        <Route path='/login' element={<Login />} />
        <Route path='/dashboard' element={<Dashboard />} />
        <Route path='/institutions' element={<Institutions />} />
        <Route path='/institutions/:slug' element={<InstitutionFloors />} />
      </Routes>
    </BrowserRouter>
  );
}

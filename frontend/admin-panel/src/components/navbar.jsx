import { Link } from 'react-router-dom';
import { useAuth } from '../utils/authContext';
import { useNavigate } from 'react-router-dom';

export default function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className='navbar bg-blue-700 text-white'>
      <div className='navbar-start'></div>
      <div className='navbar-center'>
        <Link to='/'>
          <h1 className='text-3xl font-bold cursor-pointer hover:text-gray-300 transition-colors duration-200'>
            Lecture Alert
          </h1>
        </Link>
      </div>
      <div className='navbar-end'>
        {user ? (
          <button onClick={handleLogout} className='btn btn-error'>
            Выйти
          </button>
        ) : (
          <></>
        )}
      </div>
    </div>
  );
}

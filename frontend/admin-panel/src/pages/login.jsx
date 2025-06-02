import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../utils/authContext';
import Navbar from '../components/navbar';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { user, login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const success = await login(username, password);
      if (success) {
        navigate('/');
      }
    } catch (err) {
      setError('Неверные учетные данные');
    }
  };

  useEffect(() => {
    if (user) {
      navigate('/');
    }
  }, [user, navigate]);

  return (
    <>
      <Navbar />
      {error && <div className='alert alert-error mb-4'>{error}</div>}
      <form className='mt-14' onSubmit={handleSubmit}>
        <fieldset className='fieldset mx-auto bg-base-200 border-base-300 rounded-box w-xs border p-4'>
          <legend className='fieldset-legend mx-auto text-3xl'>Войти</legend>

          <label className='label'>Логин</label>
          <input
            type='text'
            className='input'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />

          <label className='label'>Пароль</label>
          <input
            type='password'
            className='input'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <button className='btn btn-info text-white text-xl mt-4'>
            Войти
          </button>
        </fieldset>
      </form>
    </>
  );
}

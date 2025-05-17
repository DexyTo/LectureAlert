import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { apiClient } from '../api/client';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await apiClient.post('/auth/login', { email, password });
      navigate('/dashboard');
    } catch (error) {
      alert('Login failed!');
    }
  };

  return (
    <>
      <div className='navbar mb-36 bg-blue-700 text-white'>
        <div className='navbar-center mx-auto'>
          <h1 className='text-3xl font-bold'>Lecture Alert</h1>
        </div>
      </div>

      <form onSubmit={handleSubmit}>
        <fieldset className='fieldset mx-auto bg-base-200 border-base-300 rounded-box w-xs border p-4'>
          <legend className='fieldset-legend mx-auto text-3xl'>Войти</legend>

          <label className='label'>Почта</label>
          <input
            type='email'
            className='input'
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder='Почта'
            required
          />

          <label className='label'>Пароль</label>
          <input
            type='password'
            className='input'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder='Пароль'
            required
          />

          <button className='btn btn-info text-white text-xl mt-4'>Войти</button>
        </fieldset>
      </form>
    </>
  );
}

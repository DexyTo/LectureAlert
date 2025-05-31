import { useNavigate } from 'react-router-dom';
import Navbar from '../components/navbar';

export default function Menu() {
  const navigate = useNavigate();

  return (
    <>
      <Navbar />

      <div className='flex flex-col items-center gap-10'>
        <button className='btn w-3xl text-2xl py-7 bg-info text-white'>
          Студенты
        </button>
        <button
          className='btn w-3xl text-2xl py-7 bg-info text-white'
          onClick={() => navigate('/institutions')}
        >
          Фотографии институтов
        </button>
        <button className='btn w-3xl text-2xl py-7 bg-info text-white'>
          FAQ
        </button>
        <button className='btn w-3xl text-2xl py-7 bg-info text-white'>
          Расписание
        </button>
        <button className='btn w-3xl text-2xl py-7 bg-info text-white'>
          Настройки
        </button>
      </div>
    </>
  );
}

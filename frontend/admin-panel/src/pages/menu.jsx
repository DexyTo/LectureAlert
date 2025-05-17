export default function Menu() {
  return (
    <>
      <div className='navbar mb-20 bg-blue-700 text-white'>
        <div className='navbar-start'>
          <button className='btn btn-soft'>Назад</button>
        </div>
        <div className='navbar-center'>
          <h1 className='text-3xl font-bold'>Lecture Alert</h1>
        </div>
        <div className='navbar-end'>
          <button className='btn btn-error'>Выйти</button>
        </div>
      </div>

      <div className='flex flex-col items-center gap-10'>
        <button className='btn w-3xl text-2xl py-7 bg-info text-white'>
          Студенты
        </button>
        <button className='btn w-3xl text-2xl py-7 bg-info text-white'>
          Фото местности
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

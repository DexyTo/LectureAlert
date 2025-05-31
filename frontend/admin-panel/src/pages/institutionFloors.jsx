import { useParams, useNavigate } from 'react-router-dom';
import floorPlansData from '../data/floorsPlanData';

import Navbar from '../components/navbar';

export default function InstitutionSchemas() {
  const { slug } = useParams();
  const institution = floorPlansData[slug];
  const navigate = useNavigate();

  if (!institution) {
    return (
      <>
        <Navbar />
        <div className='text-center'>
          <h2 className='text-3xl font-bold text-error'>Институт не найден</h2>
          <button
            onClick={() => navigate('/institutions')}
            className='btn btn-primary mt-4'
          >
            Назад к списку
          </button>
        </div>
      </>
    );
  }

  return (
    <>
      <Navbar />
      <div className='pb-6 px-6'>
        <h1 className='text-3xl font-bold mb-6'>
          Схемы этажей: {institution.title}
        </h1>

        <div className='grid grid-cols-1 md:grid-cols-2 gap-6'>
          {institution.floors.map((floor) => (
            <div key={floor.level} className='card bg-base-200'>
              <figure>
                <img
                  src={floor.image}
                  alt={`${institution.title} - ${floor.level}`}
                  className='rounded-xl w-full object-cover'
                />
              </figure>
              <div className='card-body justify-center'>
                <div className='flex justify-between'>
                  <h3 className='card-title'>{floor.level}</h3>
                  <div className='card-actions'>
                    <button className='btn btn-primary'>Изменить</button>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

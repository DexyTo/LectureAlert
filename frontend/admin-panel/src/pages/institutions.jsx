import { useNavigate } from 'react-router-dom';
import Navbar from '../components/navbar';


import iritRtfImg from '@locationImages/Institutions/irit-rtf.png';
import gukImg from '@locationImages/Institutions/guk.jpg';
import aninImg from '@locationImages/Institutions/anin.webp';
import inmitHtiImg from '@locationImages/Institutions/inmit-hti.webp';
import isaImg from '@locationImages/Institutions/isa.webp';
import ugiImg from '@locationImages/Institutions/ugi.webp';

function createInstitution(title, image, slug) {
  return {
    title,
    image,
    slug,
    buttonText: 'Схемы этажей',
  };
}

export default function Institutions() {
  const navigate = useNavigate();

  const institutions = [
    createInstitution('ИРИТ-РТФ', iritRtfImg, 'irit-rtf'),
    createInstitution('ГУК', gukImg, 'guk'),
    createInstitution('ЭнИн', aninImg, 'anin'),
    createInstitution('ИНМТ', inmitHtiImg, 'inmit'),
    createInstitution('ИСА', isaImg, 'isa'),
    createInstitution('УГИ', ugiImg, 'ugi'),
    createInstitution('ХТИ', inmitHtiImg, 'hti'),
  ];

  return (
    <>
      <Navbar />

      <div className='flex flex-wrap gap-7 justify-center pb-4 px-4'>
        {institutions.map((institution) => (
          <div
            key={institution.slug}
            className='card bg-base-100 shadow-sm w-96 hover:shadow-lg transition-shadow'
          >
            <figure className='px-4 pt-4'>
              <img
                src={institution.image}
                alt={institution.title}
                className='rounded-xl h-48 w-full object-cover'
              />
            </figure>
            <div className='card-body items-center text-center'>
              <h2 className='card-title'>{institution.title}</h2>
              <div className='card-actions'>
                <button
                  className='btn btn-primary'
                  onClick={() => navigate(`/institutions/${institution.slug}`)}
                >
                  {institution.buttonText}
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </>
  );
}

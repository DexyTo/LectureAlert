import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <div className='navbar mb-14 bg-blue-700 text-white'>
      <div className='navbar-start'></div>
      <div className='navbar-center'>
        <Link to='/'>
          <h1 className='text-3xl font-bold cursor-pointer hover:text-gray-300 transition-colors duration-200'>
            Lecture Alert
          </h1>
        </Link>
      </div>
      <div className='navbar-end'>
        <button className='btn btn-error'>Выйти</button>
      </div>
    </div>
  );
}

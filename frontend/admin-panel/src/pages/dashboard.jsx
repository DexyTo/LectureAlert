import { useQuery } from '@tanstack/react-query';
import { apiClient } from '../api/client';

export default function Dashboard() {
  const { data: lectures, isLoading } = useQuery({
    queryKey: ['lectures'],
    queryFn: () => apiClient.get('/lectures').then(res => res.data)
  });

  if (isLoading) return <div>Loading...</div>;

  return (
    <div style={{ padding: '20px' }}>
      <h1>Lecture Schedule</h1>
      <table style={{ width: '100%' }}>
        <thead>
          <tr>
            <th>Title</th>
            <th>Time</th>
            <th>Location</th>
          </tr>
        </thead>
        <tbody>
          {lectures?.map((lecture) => (
            <tr key={lecture.id}>
              <td>{lecture.name}</td>
              <td>{new Date(lecture.start_time).toLocaleString()}</td>
              <td>{lecture.location}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
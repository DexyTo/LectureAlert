import { useState } from 'react';

export default function EditFloorModal({ floor, onClose, onSave }) {
  const [newImage, setNewImage] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setNewImage(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  const handleSave = () => {
    onSave(newImage);
    onClose();
  };

  return (
    <div className="modal modal-open">
      <div className="modal-box max-w-full">
        <h3 className="font-bold text-lg">Редактирование: {floor.level}</h3>
        
        <div className="flex flex-col gap-6 mt-4">
          <div className="flex-1">
            <p className="mb-2">Новое фото:</p>
            <input
              type="file"
              accept="image/*"
              onChange={handleFileChange}
              className="file-input file-input-bordered mb-4"
            />
            {preview && (
              <img
                src={preview}
                alt={`Предпросмотр - ${floor.level}`}
                className="rounded-lg object-contain max-h-96 w-full border"
              />
            )}
          </div>

          <div className="flex-1">
            <p className="mb-2">Текущее фото:</p>
            <img 
              src={floor.image} 
              alt={`Текущее - ${floor.level}`}
              className="rounded-lg max-h-96 w-full object-contain border"
            />
          </div>
        </div>

        <div className="modal-action mt-6">
          <button onClick={onClose} className="btn">Отмена</button>
          <button 
            onClick={handleSave} 
            className="btn btn-primary"
            disabled={!newImage}
          >
            Сохранить
          </button>
        </div>
      </div>
    </div>
  );
}
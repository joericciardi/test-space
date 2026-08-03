import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { updateProfile, uploadPhotos } from '../services/api';

function ProfileWizard() {
  const [step, setStep] = useState(1);
  const [measurements, setMeasurements] = useState({ chest: '', body_length: '', shoulder_width: '', sleeve_length: '' });
  const [photos, setPhotos] = useState(null);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleMeasurementChange = (e) => {
    setMeasurements({ ...measurements, [e.target.name]: e.target.value });
  };

  const handlePhotoChange = (e) => {
    setPhotos(e.target.files);
  };

  const submitMeasurements = async () => {
    try {
      await updateProfile(measurements);
      setStep(2);
      setError('');
    } catch (err) {
      setError('Failed to update measurements.');
    }
  };

  const submitPhotos = async () => {
    if (!photos || photos.length < 3 || photos.length > 5) {
      setError('Please upload between 3 and 5 full-body photos.');
      return;
    }

    const formData = new FormData();
    for (let i = 0; i < photos.length; i++) {
      formData.append('files', photos[i]);
    }

    try {
      await uploadPhotos(formData);
      navigate('/catalog');
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to upload photos.');
    }
  };

  return (
    <div>
      <h2>Profile Setup Wizard</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {step === 1 && (
        <div>
          <h3>Step 1: Body Measurements</h3>
          <div>
            <label>Chest size:</label>
            <input type="text" name="chest" onChange={handleMeasurementChange} placeholder="e.g. 40&quot;" required />
          </div>
          <div>
            <label>Body length:</label>
            <input type="text" name="body_length" onChange={handleMeasurementChange} placeholder="e.g. 29&quot;" required />
          </div>
          <div>
            <label>Shoulder width:</label>
            <input type="text" name="shoulder_width" onChange={handleMeasurementChange} placeholder="e.g. 18.5&quot;" required />
          </div>
          <div>
            <label>Sleeve length:</label>
            <input type="text" name="sleeve_length" onChange={handleMeasurementChange} placeholder="e.g. 34&quot;" required />
          </div>
          <button onClick={submitMeasurements}>Next</button>
        </div>
      )}

      {step === 2 && (
        <div>
          <h3>Step 2: Photo Upload</h3>
          <p>Please upload 3-5 full-body photos of yourself to generate your digital twin.</p>
          <input type="file" multiple accept="image/*" onChange={handlePhotoChange} />
          <button onClick={submitPhotos}>Finish Setup</button>
        </div>
      )}
    </div>
  );
}

export default ProfileWizard;

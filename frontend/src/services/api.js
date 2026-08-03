import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

// Interceptor to add JWT token if exists
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const signup = async (userData) => {
  return await api.post('/signup', userData);
};

export const login = async (credentials) => {
  return await api.post('/login', credentials);
};

export const updateProfile = async (profileData) => {
  return await api.post('/profile', profileData);
};

export const uploadPhotos = async (formData) => {
  return await api.post('/upload_photos', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

export const fetchCatalog = async () => {
  return await api.get('/catalog');
};

export default api;

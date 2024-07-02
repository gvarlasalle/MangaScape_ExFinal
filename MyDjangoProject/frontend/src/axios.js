// frontend/src/axios.js

import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/',  // Ajusta la URL base según la configuración de tu servidor Django
  headers: {
    'Content-Type': 'application/json',
    // Otros encabezados si es necesario
  }
});

export default apiClient;

import axios from "axios";

export const axiosInstance = axios.create({
  baseURL: "http://localhost:5000/api",
  headers: { "Content-Type": "application/json" },
  withCredentials: true,
});

// Interceptor de requête
axiosInstance.interceptors.request.use(
  (config) => {
    // Exemple : ajouter un token d'authentification à chaque requête
    const token = localStorage.getItem("token");
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
  },
  (error) => Promise.reject(error)
);

// Interceptor de réponse
axiosInstance.interceptors.response.use(
  (response) => response, // si tout va bien, renvoie la réponse
  (error) => {
    // Exemple : gestion globale des erreurs
    if (error.response?.status === 401) {
      console.log("Non autorisé ! Déconnexion automatique possible.");
      // window.location.href = "/login"; // redirection si besoin
    }
    return Promise.reject(error);
  }
);

"use client";
import { useState, useEffect, useCallback } from "react";
import axios from "axios";

export default function useRequest(url, options = {}, immediate = true) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(immediate);
  const [error, setError] = useState(null);

  // On enlève "options" des dépendances pour éviter les rerenders infinis
  const execute = useCallback(
    async (customUrl = url, customOptions = options) => {
      if (!customUrl) return; // pas d'URL → rien à faire
      setLoading(true);
      setError(null);

      try {
        const response = await axios({
          url: customUrl,
          ...customOptions,
        });
        setData(response.data);
        return response.data;
      } catch (err) {
        // Gestion spéciale du 404 pour APIs comme geo.api.gouv.fr
        if (err.response && err.response.status === 404) {
          setData([]);
          setError(null);
        } else {
          setError(err.message || "Erreur inconnue");
        }
        throw err;
      } finally {
        setLoading(false);
      }
    },
    [options] // options sont passés dynamiquement
  );

  useEffect(() => {
    if (immediate && url) {
      execute();
    }
  }, [execute, immediate, url]);

  return { data, loading, error, execute };
}

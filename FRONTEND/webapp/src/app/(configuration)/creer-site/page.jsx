"use client";
import styles from "./page.module.css";
import { useForm } from "react-hook-form";
import { useState, useMemo } from "react";
import useRequest from "@/hooks/useRequest";
import { toast } from "react-hot-toast";

export default function CreationSitePage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const [postalCode, setPostalCode] = useState("");

  const requestOptions = useMemo(() => ({ method: "GET" }), []);

  // URL = null si code postal invalide → évite les 404
  const url =
    postalCode.length === 5
      ? `https://geo.api.gouv.fr/communes?codePostal=${postalCode}`
      : null;

  const {
    data: villes,
    loading,
    error,
    execute,
  } = useRequest(
    url,
    requestOptions,
    false // exécution manuelle
  );

  const handlePostalCodeChange = (value) => {
    setPostalCode(value);

    if (value.length === 5) {
      const apiUrl = `https://geo.api.gouv.fr/communes?codePostal=${value}`;

      toast.promise(
        execute(apiUrl), // la promesse à surveiller
        {
          loading: "Chargement des villes...",
          success: <b>Villes chargées !</b>,
          error: <b>Erreur lors du chargement.</b>,
        }
      );
    }
  };

  const onSubmit = (data) => {
    console.log("données à soumettre : ", data);
  };

  return (
    <div className={styles.container}>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className={styles.inputform}>
          <label htmlFor="name">Nom :</label>
          <input
            type="text"
            id="name"
            {...register("name", { required: "Nom obligatoire" })}
          />
          {errors.name && (
            <p className={styles.errorMessage}>{errors.name.message}</p>
          )}
        </div>

        <div className={styles.inputform}>
          <label htmlFor="address">Adresse :</label>
          <input
            type="text"
            id="address"
            {...register("address", { required: "Adresse obligatoire" })}
          />
          {errors.address && (
            <p className={styles.errorMessage}>{errors.address.message}</p>
          )}
        </div>

        <div className={styles.groupform}>
          <div className={styles.inputform}>
            <label htmlFor="postal_code">Code Postal :</label>
            <input
              type="text"
              id="postal_code"
              {...register("postal_code", {
                required: "Code postal obligatoire",
              })}
              onChange={(e) => handlePostalCodeChange(e.target.value)}
            />
            {errors.postal_code && (
              <p className={styles.errorMessage}>
                {errors.postal_code.message}
              </p>
            )}
          </div>

          <div className={styles.inputform}>
            <label htmlFor="city">Ville :</label>
            <select
              id="city"
              {...register("city", { required: "Ville obligatoire" })}
            >
              <option value="">-- Sélectionner une ville --</option>
              {villes?.map(
                (commune) =>
                  commune.codesPostaux.includes(postalCode) && (
                    <option key={commune.code} value={commune.nom}>
                      {commune.nom}
                    </option>
                  )
              )}
            </select>
            {loading && <p>Chargement des villes...</p>}
            {error && <p className="text-red-500">{error}</p>}
            {errors.city && (
              <p className={styles.errorMessage}>{errors.city.message}</p>
            )}
          </div>
        </div>

        <button type="submit" className="button button-primary">
          Créer le site
        </button>
      </form>
    </div>
  );
}

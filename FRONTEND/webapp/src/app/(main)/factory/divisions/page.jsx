// FRONTEND\webapp\src\app\(main)\factory\divisions\page.jsx
"use client";
import styles from "./page.module.css";
import { useState } from "react";
import LoadingButton from "@/components/ui/Button/LoadingNavigateButton";
export default function Division() {
  const [loadingButton, setLoadingButton] = useState(null);

  return (
    <div className="card-global">
      <h4>Que souhaitez-vous faire ?</h4>
      <p>Choisissez une option :</p>
      <LoadingButton
        path="/factory/divisions/creer-division"
        buttonKey="créer"
        loadingButton={loadingButton}
        setLoadingButton={setLoadingButton}
      >
        Créer une division
      </LoadingButton>
      <LoadingButton
        path="/factory/divisions/lire-division"
        buttonKey="lire"
        loadingButton={loadingButton}
        setLoadingButton={setLoadingButton}
      >
        Lire les divisions
      </LoadingButton>
    </div>
  );
}

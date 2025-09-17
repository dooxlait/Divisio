"use client";

import styles from "./page.module.css";

import { useState } from "react";
import LoadingButton from "@/components/ui/Button/LoadingNavigateButton";

export default function Origine() {
  const [loadingButton, setLoadingButton] = useState(null); // null | "creer" | "lire"

  return (
    <div className="card-global">
      <h4>Que souhaitez-vous faire ?</h4>
      <p>Choisissez une option :</p>

      <LoadingButton
        path="/products/raw-material/create"
        buttonKey="creer"
        loadingButton={loadingButton}
        setLoadingButton={setLoadingButton}
      >
        Enregistrer une Matère Première
      </LoadingButton>

      <LoadingButton
        path="/products/raw-material/read"
        buttonKey="lire"
        loadingButton={loadingButton}
        setLoadingButton={setLoadingButton}
      >
        Lire informations Matières Premières
      </LoadingButton>
    </div>
  );
}

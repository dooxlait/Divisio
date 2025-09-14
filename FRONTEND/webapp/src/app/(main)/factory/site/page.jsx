"use client";

import { useState } from "react";
import LoadingButton from "@/components/ui/Button/LoadingNavigateButton";

export default function SitePage() {
  const [loadingButton, setLoadingButton] = useState(null); // null | "creer" | "lire"

  return (
    <div className="card-global">
      <h4>Que souhaitez-vous faire ?</h4>
      <p>Choisissez une option :</p>

      <LoadingButton
        path="/factory/site/creer-site"
        buttonKey="creer"
        loadingButton={loadingButton}
        setLoadingButton={setLoadingButton}
      >
        Créer un nouveau site
      </LoadingButton>

      <LoadingButton
        path="/factory/site/lire-site"
        buttonKey="lire"
        loadingButton={loadingButton}
        setLoadingButton={setLoadingButton}
      >
        Lire les informations du site
      </LoadingButton>
    </div>
  );
}

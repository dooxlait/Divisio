"use client";
import { useState, useEffect } from "react";
import { FolderPlus } from "lucide-react";
import { useForm } from "react-hook-form";
import { useSession } from "@/context/SessionContext";

import ActionButton from "@/components/ui/Button/ActionButton";
import useApi from "@/hooks/useApi";
import MiniCard from "@/components/cards/mini-card/minicard";
import ParentTree from "@/components/ui/HierarchyBuilder/ParentTree";

export default function CreerDivision() {
  const rawSession = useSession();
  const [loadingButton, setLoadingButton] = useState(null);
  const [session, setSession] = useState(null);
  const [selectedService, setSelectedService] = useState(null);
  const [selectedParent, setSelectedParent] = useState(null);
  const [customErrors, setCustomErrors] = useState({});

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();

  // Gestion de la session
  useEffect(() => {
    if (rawSession) {
      try {
        setSession(JSON.parse(rawSession));
      } catch (err) {
        console.error("Erreur parsing session :", err);
        setSession(null);
      }
    } else {
      setSession(null);
    }
  }, [rawSession]);

  // Récupération de la hiérarchie via useApi
  const { status, data } = useApi({ endpoint: "factory/divisions" });

  const onSubmit = (formData) => {
    let newErrors = {};

    if (!formData.site) newErrors.site = "Le site doit être sélectionné.";
    if (!selectedService) newErrors.service = "Un type doit être sélectionné.";
    if (!formData.name) newErrors.name = "Le nom est obligatoire.";
    if (!selectedParent)
      newErrors.parent = "Un rattachement doit être sélectionné.";

    setCustomErrors(newErrors);

    if (Object.keys(newErrors).length > 0) {
      setLoadingButton(null);
      return;
    }

    console.log("✅ Données à soumettre :", {
      ...formData,
      service: selectedService,
      parent: selectedParent,
    });

    // Ici appel API par ex.
    setLoadingButton(null);
  };

  // Vérifie si le formulaire est valide pour activer le bouton
  const isFormValid = () => {
    const site = document.getElementById("site")?.value;
    return site && selectedService && selectedParent && watch("name");
  };

  return (
    <div className="card-global">
      <h4 className="card-title">
        <FolderPlus style={{ marginRight: "8px" }} />
        Création d'une division
      </h4>

      <form onSubmit={handleSubmit(onSubmit)}>
        <table className="table-light">
          <tbody>
            <tr>
              <th style={{ minWidth: "150px" }}>Site :</th>
              <td>
                <select
                  id="site"
                  {...register("site", { required: true })}
                  defaultValue=""
                >
                  <option value="">--Sélectionner un site--</option>
                  <option value={session?.id}>{session?.name}</option>
                </select>
                {(errors.site || customErrors.site) && (
                  <p className="form-error">
                    {errors.site?.message || customErrors.site}
                  </p>
                )}
              </td>
            </tr>
            <tr>
              <th>Nom :</th>
              <td>
                <input
                  type="text"
                  id="name"
                  {...register("name", { required: "Le nom est obligatoire." })}
                />
                {errors.name && (
                  <p className="form-error">{errors.name.message}</p>
                )}
              </td>
            </tr>
            <tr>
              <th>Type: </th>
              <td>
                <div className="visual-card">
                  <MiniCard
                    onSelect={setSelectedService}
                    selected={selectedService}
                  />
                </div>
                {customErrors.service && (
                  <p className="form-error">{customErrors.service}</p>
                )}
              </td>
            </tr>
          </tbody>
        </table>

        <table className="table-light" style={{ marginTop: "16px" }}>
          <tbody>
            <tr>
              <th>Rattachement :</th>
              <td>
                {status === "loading" && <p>Chargement des données...</p>}
                {status === "error" && <p>Erreur lors du chargement.</p>}
                {status === "ok" && data && (
                  <ParentTree
                    data={data}
                    parentId={selectedParent}
                    onSelect={(node) => setSelectedParent(node?.id || null)}
                  />
                )}
                {customErrors.parent && (
                  <p className="form-error">{customErrors.parent}</p>
                )}
              </td>
            </tr>
          </tbody>
        </table>

        <ActionButton
          buttonKey="submitDivision"
          loadingButton={loadingButton}
          setLoadingButton={setLoadingButton}
          onClick={() => handleSubmit(onSubmit)()}
          className="button button-primary"
          disabled={!isFormValid()}
          style={{ marginTop: "24px" }}
        >
          Créer
        </ActionButton>
      </form>
    </div>
  );
}

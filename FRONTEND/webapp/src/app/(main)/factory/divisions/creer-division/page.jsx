"use client";
import styles from "./page.module.css";
import { useState, useEffect } from "react";
import { FolderPlus } from "lucide-react";
import { useForm } from "react-hook-form";
import { useSession } from "@/context/SessionContext";
import useApi from "@/hooks/useApi";
import MiniCard from "@/components/cards/mini-card/minicard";
import ParentTree from "@/components/ui/HierarchyBuilder/ParentTree";

export default function CreerDivision() {
  const rawSession = useSession();
  const [session, setSession] = useState(null);
  const [selectedService, setSelectedService] = useState(null);
  const [selectedParent, setSelectedParent] = useState(null);

  const {
    register,
    handleSubmit,
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
    console.log("Données à soumettre :", {
      ...formData,
      service: selectedService,
      parent: selectedParent,
    });
  };

  return (
    <div className="card-global">
      <h4 className="card-title">
        <FolderPlus />
        Création d'une division
      </h4>
      <hr />
      <form onSubmit={handleSubmit(onSubmit)}>
        <table className="table-light">
          <tbody>
            <tr>
              <th>Site :</th>
              <td>
                <select name="site" id="site">
                  <option value="">--Sélectionner un site--</option>
                  <option value={session?.id}>{session?.name}</option>
                </select>
              </td>
            </tr>
            <tr>
              <th>Type: </th>
            </tr>
          </tbody>
        </table>

        <div className={styles.visualCard}>
          <MiniCard onSelect={setSelectedService} selected={selectedService} />
        </div>

        <table className="table-light">
          <tbody>
            <tr>
              <th>Nom :</th>
              <td>
                <input
                  type="text"
                  name="name"
                  id="name"
                  {...register("name", { required: true })}
                />
              </td>
            </tr>
            <tr>
              <th>Rattachement :</th>
              <td>
                {status === "loading" && <p>Chargement des données...</p>}
                {status === "error" && <p>Erreur lors du chargement.</p>}
                {status === "ok" && data && (
                  <ParentTree
                    data={data}
                    parentId={selectedParent}
                    onSelect={(node) => setSelectedParent(node.id)}
                  />
                )}
              </td>
            </tr>
          </tbody>
        </table>

        <button type="submit" className="btn-primary">
          Créer
        </button>
      </form>
    </div>
  );
}

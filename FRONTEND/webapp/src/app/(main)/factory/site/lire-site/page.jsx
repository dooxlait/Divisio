// FRONTEND\webapp\src\app\(main)\factory\site\lire-site\page.jsx
"use client";
import styles from "./page.module.css";
import { Book, SquarePen } from "lucide-react";
import useApi from "@/hooks/useApi";
import { useForm } from "react-hook-form";
import { useState } from "react";

export default function LireSite() {
  const { status, data } = useApi({ endpoint: "factory/sites" });
  const { register } = useForm();
  const [modeEdit, setModeEdit] = useState(false);

  if (status !== "ok") return "un instant svp..";

  const site = data?.payload[0];
  const handleEditMode = () => {
    setModeEdit((prev) => !prev);
  };

  return (
    <div className={styles.container}>
      <div className="card">
        <div className={styles.cardHeader}>
          <span className={styles.cardHeading}>
            <Book /> Informations
          </span>
          <span className={styles.editMode}>
            <button className={styles.buttonEdit} onClick={handleEditMode}>
              <SquarePen />
              Edit
            </button>
          </span>
        </div>
        <div className={styles.cardContent}>
          <table className="table-light">
            <tbody>
              <tr>
                <th>Nom :</th>
                <td>
                  <input
                    type="text"
                    id="name"
                    {...register("name")}
                    defaultValue={site?.name}
                    disabled={!modeEdit}
                  />
                </td>
              </tr>
              <tr>
                <th>Adresse :</th>
                <td>
                  <input
                    type="text"
                    id="address"
                    {...register("address")}
                    defaultValue={site?.address}
                    disabled={!modeEdit}
                  />
                </td>
              </tr>
              <tr>
                <th>Code Postal :</th>
                <td>
                  <input
                    type="text"
                    id="postal_code"
                    {...register("postal_code")}
                    defaultValue={site?.postal_code}
                    disabled={!modeEdit}
                  />
                </td>
              </tr>
              <tr>
                <th>Ville :</th>
                <td>
                  <input
                    type="text"
                    id="city"
                    {...register("city")}
                    defaultValue={site?.city}
                    disabled={!modeEdit}
                  />
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

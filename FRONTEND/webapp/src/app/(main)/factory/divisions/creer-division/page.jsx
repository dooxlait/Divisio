// FRONTEND\webapp\src\app\factory\divisions\page.jsx
"use client";
import styles from "./page.module.css";
import { useState, useEffect } from "react";
import { FolderPlus } from "lucide-react";
import { useForm } from "react-hook-form";
import { useSession } from "@/context/SessionContext";
import useApi from "@/hooks/useApi";
import MiniCard from "@/components/cards/mini-card/minicard";
export default function CreerDivision() {
  const rawSession = useSession();
  const [session, setSession] = useState(null);

  useEffect(() => {
    if (rawSession) {
      try {
        setSession(JSON.parse(rawSession));
      } catch (err) {
        console.error("Erreur de parsing du cookie session :", err);
        setSession(null);
      }
    } else {
      setSession(null);
    }
  }, [rawSession]);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  const onSubmit = (data) => {
    console.log("données à soumettre : ", data);
  };
  return (
    <div className="card-global ">
      <h4 className="card-title">
        <FolderPlus />
        Création d'une division
      </h4>
      <hr />
      <form onSubmit={handleSubmit(onSubmit)}>
        <table className="table-light">
          <tr>
            <th>Site :</th>
            <td>
              <select name="site" id="site">
                <option value="">--Selectionner un site</option>
                <option value={session?.id}>{session?.name}</option>
              </select>
            </td>
          </tr>
        </table>
        <div className={styles.visualCard}>
          <MiniCard />
        </div>
      </form>
    </div>
  );
}

"use client";

import styles from "./page.module.css";
import { useForm } from "react-hook-form";
import { FolderPlus } from "lucide-react";

export default function CreateRawMaterial() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (formData) => {
    console.log("Matière Première enregistrée :", formData);
  };

  return (
    <div className={styles.container}>
      <div className="card-global">
        <h4 className="card-title">
          <FolderPlus style={{ marginRight: "8px" }} />
          Enregistrement d&apos;une Matière Première
        </h4>

        <form onSubmit={handleSubmit(onSubmit)}>
          <table className="table-light">
            <tbody>
              <tr>
                <th style={{ minWidth: "150px" }}>
                  <label htmlFor="name">Nom :</label>
                </th>
                <td>
                  <input
                    type="text"
                    id="name"
                    placeholder="Ex : Lait de brebis"
                    {...register("name", {
                      required: "Le nom est obligatoire.",
                    })}
                  />
                  {errors.name && (
                    <p className="form-error">{errors.name.message}</p>
                  )}
                </td>
              </tr>

              <tr>
                <th style={{ minWidth: "150px" }}>
                  <label htmlFor="name">Description :</label>
                </th>
                <td>
                  <textarea
                    type="text"
                    id="name"
                    placeholder="Description du produit"
                    {...register("description")}
                  />
                  {errors.name && (
                    <p className="form-error">{errors.name.message}</p>
                  )}
                </td>
              </tr>

              <tr>
                <td
                  colSpan={2}
                  style={{ textAlign: "right", paddingTop: "10px" }}
                >
                  <button type="submit" className="btn-primary">
                    Enregistrer
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </form>
      </div>
    </div>
  );
}

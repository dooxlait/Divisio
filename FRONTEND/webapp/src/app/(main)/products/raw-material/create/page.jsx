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
      <div className="form-card">
        <h4 className="">
          <FolderPlus style={{ marginRight: "8px" }} />
          Enregistrement d&apos;une Matière Première
        </h4>
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className={styles.formcontrol}>
            <label htmlFor="nom">Nom : </label>
            <input type="text" name="nom" id="nom" />
          </div>
        </form>
      </div>
    </div>
  );
}

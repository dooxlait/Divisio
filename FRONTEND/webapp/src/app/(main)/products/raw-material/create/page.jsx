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
      <div className={styles.title}>
        <FolderPlus />
        <span>Enregistrement d'une matière première</span>
      </div>
    </div>
  );
}

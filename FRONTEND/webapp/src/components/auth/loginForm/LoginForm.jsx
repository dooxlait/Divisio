"use client";

import styles from "./LoginForm.module.css";
import SiteSelect from "@/components/form/SiteSelect/SiteSelect";
import Cookies from "js-cookie";

export default function LoginForm({ onSuccess }) {
  // ✅ onSuccess reçu en prop
  const handleSubmit = (e) => {
    e.preventDefault();
    const siteId = Cookies.get("site_id");
    if (siteId && onSuccess) {
      onSuccess(siteId);
    }
  };

  return (
    <div className={styles.container}>
      <h1>Welcome back!</h1>
      <h4>Merci d'entrer les informations de connexion</h4>

      <form onSubmit={handleSubmit}>
        <div className={styles.formGroup}>
          <label htmlFor="select-site">Sélectionnez le site :</label>
          <SiteSelect />
        </div>

        <button type="submit" className={styles.sign_in_apl}>
          Connexion
        </button>
      </form>
    </div>
  );
}

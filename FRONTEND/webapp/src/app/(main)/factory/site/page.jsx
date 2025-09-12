"use client";
import styles from "./page.module.css";
import { useRouter } from "next/navigation";

import Spinner from "@/components/ui/Spinner";

export default function SitePage() {
  const router = useRouter();

  return (
    <div className={styles.container}>
      <h4>Que souhaitez vous faire ?</h4>
      <p>Choisissez une option :</p>

      <button
        className={styles.button}
        onClick={() => router.push("/factory/site/creer-site")}
      >
        Créer un nouveau site
      </button>

      <button
        className={styles.button}
        onClick={() => router.push("/factory/site/lire-site")}
      >
        Lire les informations du site
      </button>

    </div>
  );
}

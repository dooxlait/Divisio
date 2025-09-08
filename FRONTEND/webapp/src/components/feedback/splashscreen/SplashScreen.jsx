import styles from "./SplashScreen.module.css";
import useApiCheck from "@/hooks/useApiCheck";
import { ShieldQuestionMark } from "lucide-react";

export default function SplashScreen() {
  const { status } = useApiCheck();

  return (
    <div className={styles.container}>
      <img src="/morice_sas_logo.jpg" alt="logo de BIOCHAMPS et MORICE" />
      <p className={styles.subtitle}>Bienvenue !</p>
      <div className={styles["application-state"]}>
        <p className={styles.subtitle}>Vérification des composants...</p>
        {status == "ok" ? (
          <span>
            <ShieldQuestionMark />
            OK
          </span>
        ) : null}
      </div>
    </div>
  );
}

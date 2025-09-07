import { useEffect, useState } from "react";
import styles from "./Header.module.css";
import { useSession } from "@/context/SessionContext";
import { capitalize } from "@/utils/string";

export default function Header({ module }) {
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

  return (
    <header className={styles.header}>
      <h5 className={styles.moduleTitle}>{capitalize(module)}</h5>
      {session ? (
        <p>📍 Site de {session.city}</p>
      ) : (
        <p>Aucun site sélectionné</p>
      )}
    </header>
  );
}

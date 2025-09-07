"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import styles from "./logo.module.css";
import { useSession } from "@/context/SessionContext";
export default function Logo() {
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
    <Link href="/dashboard" className={styles.logoLink}>
      <div className={styles.logo}>
        <img
          src="/morice_sas_logo-removedbg.png"
          alt="logo de BIOCHAMPS et MORICE"
        />
        <h5>{session?.name} MES</h5>
      </div>
    </Link>
  );
}

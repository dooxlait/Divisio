"use client";
import Link from "next/link";
import styles from "./logo.module.css";

export default function Logo() {
  return (
    <Link href="/dashboard" className={styles.logoLink}>
      <div className={styles.logo}>
        <img
          src="/morice_sas_logo-removedbg.png"
          alt="logo de BIOCHAMPS et MORICE"
        />
        <h5>Biochamps MES</h5>
      </div>
    </Link>
  );
}

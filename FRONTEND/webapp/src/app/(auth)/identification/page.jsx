// FRONTEND\webapp\src\app\identification\page.jsx

"use client";
import Link from "next/link";
import { useRouter } from "next/navigation";

import styles from "./page.module.css";
import Logo from "@/components/auth/logo/logo";
import LoginForm from "@/components/auth/loginForm/LoginForm";

export default function IdentificationPage() {
  const router = useRouter();
  const handleLoginSuccess = (siteId) => {
    router.push(`/dashboard/`);
  };
  return (
    <div className={styles.container}>
      <div className={styles.main}>
        <div className={styles.section}>
          <div className={styles.topsection}>
            <Logo />
          </div>
          <div className={styles.midsection}>
            <LoginForm onSuccess={handleLoginSuccess} />
            <Link href="/creer-site">Créer un site</Link>
          </div>

          <div className={styles.footersection}>footer</div>
        </div>
        <div className={styles.section}>
          <div className={styles.decoration}></div>
        </div>
      </div>
    </div>
  );
}

// FRONTEND\webapp\src\app\(configuration)\creer-site\layout.jsx

import styles from "./layout.module.css";

export default function CreerSiteLayout({ children }) {
  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <h1 className={styles.pagetitle}>Création d'un site de production</h1>
      </header>
      <main className={styles.main} style={{ display: "flex" }}>
        {children}
      </main>
      <footer className={styles.footer}>© 2025 Morice SAS</footer>
    </div>
  );
}

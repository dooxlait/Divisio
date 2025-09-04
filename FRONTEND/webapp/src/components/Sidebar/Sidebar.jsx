// Sidebar.jsx
"use client";
import styles from "./Sidebar.module.css";

export default function Sidebar({ items = [] }) {
  return (
    <aside className={styles.sidebar}>
      <div className={styles.logo}>
        <h2>MonApp</h2>
        <p>MES</p>
      </div>
      <nav className={styles.nav}>
        {items.map((item) => (
          <a key={item.label} href={item.href} className={styles.navItem}>
            {item.label}
          </a>
        ))}
      </nav>
    </aside>
  );
}

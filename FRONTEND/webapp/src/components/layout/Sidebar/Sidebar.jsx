// Sidebar.jsx
"use client";
import styles from "./Sidebar.module.css";

export default function Sidebar({ items = [] }) {
  return (
    <aside className={styles.sidebar}>
      <div className={styles.sidebarContent}>Sidebar</div>
    </aside>
  );
}

"use client";

import Sidebar from "@/components/Sidebar/Sidebar";
import Header from "@/components/Header/Header";
import styles from "./layout.module.css";

export default function DashboardLayout({ children }) {
  return (
    <div className={`${styles.container} `}>
      <aside className={styles.sidebar}>
        <Sidebar />
      </aside>
      <header className={styles.header}>
        <Header />
      </header>
      <main className={styles.content}>{children}</main>
    </div>
  );
}

// Sidebar.jsx
"use client";
import { useState } from "react";
import styles from "./Sidebar.module.css";
import { LayoutDashboard, Factory } from "lucide-react";

export default function Sidebar({ items = [] }) {
  const [isFactoryOpen, setIsFactoryOpen] = useState(false);

  const handleToggleFactoryMenu = () => {
    setIsFactoryOpen((prev) => !prev);
  };

  return (
    <aside className={styles.sidebar}>
      <div className={styles.sidebarContent}>
        <div className={styles.sidebarItem}>
          <LayoutDashboard />
          Dashboard
        </div>

        <div className={styles.sidebarItem} onClick={handleToggleFactoryMenu}>
          <Factory />
          Factory
          <span className={styles.action}>{isFactoryOpen ? "▼" : "►"}</span>
        </div>

        {isFactoryOpen && (
          <div className={styles.subMenu}>
            {/* exemple d’items du sous-menu */}
            <div className={styles.sidebarItem}>Sites</div>
            <div className={styles.sidebarItem}>Divisions</div>
          </div>
        )}
      </div>
    </aside>
  );
}

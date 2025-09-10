"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import styles from "./Sidebar.module.css";
import { sidebarItems } from "@/config/sidebar.config";

export default function Sidebar({ items = sidebarItems }) {
  const router = useRouter();
  const [openMenus, setOpenMenus] = useState({});

  const toggleMenu = (label) => {
    setOpenMenus((prev) => ({
      ...prev,
      [label]: !prev[label],
    }));
  };

  const handleNavigate = (path) => {
    router.push(path);
  };

  return (
    <aside className={styles.sidebar}>
      <ul className={styles.tree}>
        {items.map((item) => {
          const Icon = item.icon;
          const isOpen = openMenus[item.label] || false;

          return (
            <li key={item.label} className={isOpen ? styles.open : undefined}>
              <div
                className={styles.item}
                onClick={() => item.children && toggleMenu(item.label)}
              >
                <Icon />
                <span className={styles.itemName}>{item.label}</span>
                {item.children && (
                  <span className={styles.arrow}>{isOpen ? "▼" : "►"}</span>
                )}
              </div>

              {item.children && isOpen && (
                <ul>
                  {item.children.map((child) => {
                    const ChildIcon = child.icon;
                    return (
                      <li key={child.label}>
                        <div
                          className={styles.item}
                          onClick={() => handleNavigate(child.path)}
                        >
                          <ChildIcon />
                          <span className={styles.itemName}>{child.label}</span>
                        </div>
                      </li>
                    );
                  })}
                </ul>
              )}
            </li>
          );
        })}
      </ul>
    </aside>
  );
}

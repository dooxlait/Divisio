//FRONTEND\webapp\src\app\(main)\layout.jsx
"use client";
import { usePathname } from "next/navigation";

import Header from "@/components/layout/Header/Header";
import Sidebar from "@/components/layout/Sidebar/Sidebar";
import Logo from "@/components/layout/Logo/logo";

import styles from "./layout.module.css";

export default function MainLayout({ children }) {
  const pathname = usePathname();
  const firstSegment = pathname.split("/")[1] || "";
  return (
    <div className={styles.mainLayout}>
      <div className={styles.mainLayoutLogo}>
        <Logo />
      </div>
      <div className={styles.mainLayoutHeader}>
        <Header module={firstSegment} />
      </div>
      <div className={styles.mainLayoutSidebar}>
        <Sidebar />
      </div>
      <div className={styles.mainLayoutContent}>{children}</div>
    </div>
  );
}

// FRONTEND\webapp\src\app\factory\divisions\layout.jsx

import styles from "./layout.module.css";

export default function CreationDivisionLayout({ children }) {
  return <div className={styles.container}>{children}</div>;
}

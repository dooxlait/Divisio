// FRONTEND\webapp\src\app\factory\layout.jsx

import styles from "./layout.module.css";

export default function FactoryLayout({ children }) {
  return <div className={styles.container}>{children}</div>;
}

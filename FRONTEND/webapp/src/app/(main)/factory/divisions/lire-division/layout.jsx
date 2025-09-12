import styles from "./layout.module.css";

export default function LireDivisionLayout({ children }) {
  return <div className={styles.containers}>{children}</div>;
}

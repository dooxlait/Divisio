import styles from "./layout.module.css";

export default function SiteLayout({ children }) {
  return <div className={styles.container}>{children}</div>;
}

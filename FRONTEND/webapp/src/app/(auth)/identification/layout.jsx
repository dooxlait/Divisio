import styles from "./layout.module.css";

export default function AuthLayout({ children }) {
  return <div className={styles.authContainer}>{children}</div>;
}

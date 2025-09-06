import styles from "./Header.module.css";
import { capitalize } from "@/utils/string";
export default function Header({ module }) {
  return (
    <div className={styles.header}>
      <h5 className={styles.moduleTitle}>{capitalize(module)}</h5>
    </div>
  );
}

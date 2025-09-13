import styles from "./minicard.module.css";
import { serviceChoice } from "@/config/servicechoice.config";

export default function MiniCard({ items = serviceChoice }) {
  return (
    <>
      {items.map((item) => {
        const Icon = item.icon;
        return (
          <div key={item.label} className={styles.minicard}>
            <Icon />
            <div className={styles.content}>
              <span>{item.label}</span>
              <hr />
              <span>{item.explication}</span>
            </div>
          </div>
        );
      })}
    </>
  );
}

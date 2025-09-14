// minicard.jsx
import styles from "./minicard.module.css";
import { serviceChoice } from "@/config/servicechoice.config";

export default function MiniCard({
  items = serviceChoice,
  onSelect,
  selected,
}) {
  return (
    <>
      {items.map((item) => {
        const Icon = item.icon;
        const isActive = selected?.label === item.label; // vérifie si c’est le choisi

        return (
          <div
            key={item.label}
            className={`${styles.minicard} ${isActive ? styles.active : ""}`}
            onClick={() => onSelect(item)} // on envoie l’item choisi
          >
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

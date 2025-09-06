import styles from "./logo.module.css";
export default function Logo() {
  return (
    <div className={styles.logo}>
      <img
        src="/morice_sas_logo.jpg"
        alt="logo de BIOCHAMPS et MORICE"
        style={{ height: "50px", margin: "15px" }}
      />
      <span>Biochamps MES</span>
    </div>
  );
}

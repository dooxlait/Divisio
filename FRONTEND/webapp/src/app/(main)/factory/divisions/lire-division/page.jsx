"use client";
import styles from "./page.module.css";
import useApi from "@/hooks/useApi";
import HierarchyBuilder from "@/components/ui/HierarchyBuilder";

export default function LireDivisionPage() {
  const { status, data } = useApi({ endpoint: "factory/divisions" });

  if (status !== "ok") return "Un instant svp...";

  return (
    <div className={styles.container}>
      <h1>Organisation</h1>
      {/* On passe l'objet complet avec payload */}
      <HierarchyBuilder data={data} />
    </div>
  );
}

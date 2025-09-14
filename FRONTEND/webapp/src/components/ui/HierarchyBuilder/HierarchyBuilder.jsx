// FRONTEND\webapp\src\components\ui\HierarchyBuilder\HierarchyBuilder.jsx
"use client";
import { useMemo, useState, useEffect } from "react";
import { buildHierarchy } from "@/helpers/buildHierarchy";
import { useSession } from "@/context/SessionContext";
import TreeNode from "./TreeNode";
import styles from "./HierarchyBuilder.module.css";

export default function HierarchyBuilder({ data }) {
  const hierarchy = useMemo(() => buildHierarchy(data.payload), [data]);
  const rawSession = useSession();
  const [session, setSession] = useState(null);

  useEffect(() => {
    if (rawSession) {
      try {
        setSession(JSON.parse(rawSession));
      } catch (err) {
        console.error("Erreur de parsing du cookie session :", err);
        setSession(null);
      }
    } else {
      setSession(null);
    }
  }, [rawSession]);

  return (
    <div className={`${styles.treeContainer} card`}>
      <h4>{session?.name}</h4>
      <ul className={styles.tree}>
        {hierarchy.map((root, idx) => (
          <TreeNode
            key={root.id}
            node={root}
            level={0}
            isLast={idx === hierarchy.length - 1}
          />
        ))}
      </ul>
    </div>
  );
}

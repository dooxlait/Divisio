"use client";
import { useState } from "react";
import styles from "./TreeNode.module.css";

export default function TreeNode({
  node,
  level = 0,
  isLast = true,
  onSelect,
  selectedId,
}) {
  const [open, setOpen] = useState(true);
  const hasChildren = node.subdivisions?.length > 0;

  return (
    <li className={styles.treeItem}>
      <div
        className={`${styles.nodeLabel} ${
          selectedId === node.id ? styles.selected : ""
        }`}
        onClick={(e) => {
          e.stopPropagation(); // éviter ouverture/fermeture si nécessaire
          onSelect?.(node);
          if (hasChildren) setOpen((prev) => !prev);
        }}
      >
        {hasChildren && (
          <span className={styles.toggle}>{open ? "▼" : "▶"}</span>
        )}
        <strong>{node.name}</strong> <em>({node.type})</em>
      </div>

      {hasChildren && open && (
        <ul>
          {node.subdivisions.map((sub, idx) => (
            <TreeNode
              key={sub.id}
              node={sub}
              level={level + 1}
              isLast={idx === node.subdivisions.length - 1}
              onSelect={onSelect}
              selectedId={selectedId}
            />
          ))}
        </ul>
      )}
    </li>
  );
}

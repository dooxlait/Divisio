"use client";
import { useMemo } from "react";
import { buildHierarchy } from "@/helpers/buildHierarchy";
import TreeNode from "./TreeNode";
import styles from "./HierarchyBuilder.module.css";

function findNodeById(tree, id) {
  for (const node of tree) {
    if (node.id === id) return node;
    if (node.subdivisions?.length) {
      const found = findNodeById(node.subdivisions, id);
      if (found) return found;
    }
  }
  return null;
}

export default function ParentTree({ data, parentId, onSelect }) {
  const hierarchy = useMemo(() => buildHierarchy(data.payload), [data]);

  const parentNode = useMemo(() => {
    if (!parentId) return null;
    return findNodeById(hierarchy, parentId);
  }, [hierarchy, parentId]);

  return (
    <div className={`${styles.treeContainer} card`}>
      <h4>Parent sélectionné</h4>
      {/* Bouton retour + info élément sélectionné */}
      {parentId && (
        <div className={styles.selectionHeader}>
          <button
            type="button"
            className={styles.backButton}
            onClick={() => onSelect({ id: null })}
          >
            ⬅ Retour
          </button>
        </div>
      )}
      <span className={styles.selectedLabel}>
        Selection : {parentNode?.name || "N/A"}{" "}
        <em> ({parentNode?.type || ""})</em>
      </span>
      <ul className={styles.tree}>
        {parentNode ? (
          <TreeNode
            node={parentNode}
            level={0}
            isLast={true}
            onSelect={onSelect}
            selectedId={parentId}
          />
        ) : (
          hierarchy.map((root) => (
            <TreeNode
              key={root.id}
              node={root}
              level={0}
              isLast={true}
              onSelect={onSelect}
              selectedId={parentId}
            />
          ))
        )}
      </ul>
    </div>
  );
}

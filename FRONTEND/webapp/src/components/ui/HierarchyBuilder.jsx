"use client";
import { useMemo, useState, useEffect } from "react";
import { buildHierarchy } from "@/helpers/buildHierarchy";
import { useSession } from "@/context/SessionContext";
function TreeNode({ node, level = 0, isLast = true }) {
  const [open, setOpen] = useState(true); // état ouvert/fermé

  const hasChildren = node.subdivisions.length > 0;

  return (
    <li className="tree-item">
      <div
        className="node-label"
        onClick={() => hasChildren && setOpen((prev) => !prev)}
      >
        {hasChildren && <span className="toggle">{open ? "▼" : "▶"}</span>}
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
            />
          ))}
        </ul>
      )}

      <style jsx>{`
        .tree-item {
          position: relative;
          padding-left: 26px;
          list-style: none;
        }

        /* Ligne verticale */
        .tree-item::before {
          content: "";
          position: absolute;
          top: 0;
          left: 16px;
          width: 1px;
          height: ${isLast ? "12px" : "100%"};
          border-left: 1px solid #aaa;
        }

        /* Ligne horizontale vers le nœud */
        .node-label::before {
          content: "";
          position: absolute;
          top: 12px;
          left: -10px;
          width: 10px;
          height: 1px;
          border-top: 1px solid #aaa;
        }

        .node-label {
          position: relative;
          padding: 4px 8px;
          cursor: pointer;
          user-select: none;
        }

        .node-label:hover {
          background-color: #f0f0f0;
        }

        .toggle {
          display: inline-block;
          width: 16px;
          text-align: center;
          margin-right: 4px;
        }
      `}</style>
    </li>
  );
}

export default function HierarchyBuilder({ data }) {
  const hierarchy = useMemo(() => buildHierarchy(data.payload), [data]);
  const rawSession = useSession();
  const [session, setSession] = useState(null);
  console.log(session);
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
    <div className="tree-container card">
      <h4>{session?.name}</h4>
      <ul className="tree">
        {hierarchy.map((root, idx) => (
          <TreeNode
            key={root.id}
            node={root}
            level={0}
            isLast={idx === hierarchy.length - 1}
          />
        ))}
      </ul>

      <style jsx>{`
        .tree-container {
          max-width: 400px;
          overflow-x: auto;
          border: 1px solid #ddd;
          padding: 8px;
        }

        .tree {
          list-style: none;
          margin: 0;
          padding: 0;
        }
      `}</style>
    </div>
  );
}

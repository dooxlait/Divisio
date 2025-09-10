import {
  LayoutDashboard,
  Factory,
  Blocks,
  LayoutList,
  CircleUserRound,
  VectorSquare,
  Cpu,
} from "lucide-react";

export const sidebarItems = [
  {
    label: "Dashboard",
    icon: LayoutDashboard,
    path: "/dashboard", // 👈 ajouté
    children: null,
  },
  {
    label: "Factory",
    icon: Factory,
    children: [
      { label: "Site", icon: Blocks, path: "/factory/site" },       // 👈 ajouté
      { label: "Division", icon: LayoutList, path: "/factory/division" },
    ],
  },
  {
    label: "HR",
    icon: CircleUserRound,
    children: [
      { label: "Employees", icon: Blocks, path: "/hr/employees" },
      { label: "Affectations", icon: LayoutList, path: "/hr/affectations" },
    ],
  },
  {
    label: "Technical",
    icon: VectorSquare,
    children: [
      { label: "Machines", icon: Cpu, path: "/technical/machines" },
    ],
  },
];

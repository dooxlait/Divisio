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
    children: null,
  },
  {
    label: "Factory",
    icon: Factory,
    children: [
      { label: "Site", icon: Blocks },
      { label: "Division", icon: LayoutList },
    ],
  },
  {
    label: "HR",
    icon: CircleUserRound,
    children: [
      { label: "Employees", icon: Blocks },
      { label: "Affectations", icon: LayoutList },
    ],
  },
  {
    label: "Technical",
    icon: VectorSquare,
    children: [{ label: "Machines", icon: Cpu }],
  },
];

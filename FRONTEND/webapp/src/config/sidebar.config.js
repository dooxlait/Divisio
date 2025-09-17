import {
  LayoutDashboard,
  Factory,
  Blocks,
  LayoutList,
  CircleUserRound,
  VectorSquare,
  Cpu,
  Apple,
  Milk,
  BookCopy,
  TrendingUpDown,
  ScanQrCode,
  Boxes,
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
      { label: "Site", icon: Blocks, path: "/factory/site" }, // 👈 ajouté
      { label: "Division", icon: LayoutList, path: "/factory/divisions" },
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
    children: [{ label: "Machines", icon: Cpu, path: "/technical/machines" }],
  },
  {
    label: "Products",
    icon: Apple,
    children: [
      {
        label: "Matières Premières",
        icon: Milk,
        path: "/products/raw-material",
      },
      {
        label: "Familles Produits",
        icon: BookCopy,
        path: "/products/type-products",
      },
      {
        label: "Variantes Familles Produits",
        icon: TrendingUpDown,
        path: "/products/variants-products",
      },
      {
        label: "Formats Emballages",
        icon: ScanQrCode,
        path: "/products/packaging-formats",
      },
      {
        label: "Palettes",
        icon: Boxes,
        path: "/products/pallets",
      },
    ],
  },
];

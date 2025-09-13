import {
  Building2, // pour Service
  Building, // pour Department
  Factory, // pour Atelier
  Workflow, // pour Ligne
} from "lucide-react";

export const serviceChoice = [
  {
    label: "Service",
    explication:
      "Un service regroupe un ensemble de fonctions ou d’activités liées à un domaine (par ex. maintenance, qualité, logistique).",
    icon: Building2,
  },
  {
    label: "Atelier",
    explication:
      "Un atelier correspond à une zone physique de production ou d’assemblage, où sont réalisées des opérations spécifiques.",
    icon: Factory,
  },
  {
    label: "Ligne",
    explication:
      "Une ligne est une suite organisée de postes ou de machines dans un atelier, dédiée à la fabrication d’un produit ou d’une gamme précise.",
    icon: Workflow,
  },
];

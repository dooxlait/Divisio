"use client";

import useApi from "@/hooks/useApi";
import Cookies from "js-cookie";
import styles from "./SiteSelect.module.css";

export default function SiteSelect() {
  const { status, data } = useApi({ endpoint: "factory/sites" });

  const handleSiteChange = (event) => {
    const siteId = event.target.value;
    if (siteId) {
      Cookies.set("site_id", siteId, { expires: 7, path: "/" });
    }
  };

  if (status === "loading") {
    return <p>⏳ Chargement des sites...</p>;
  }

  if (status === "error") {
    return <p style={{ color: "red" }}>❌ Impossible de charger les sites</p>;
  }

  return (
    <select
      name="select-site"
      id="select-site"
      className={styles.select}
      required
      onChange={handleSiteChange}
    >
      <option value="">-- Sélectionner un site</option>
      {data?.payload?.map((site) => (
        <option key={site.id} value={site.id}>
          {site.name} – {site.city}
        </option>
      ))}
    </select>
  );
}

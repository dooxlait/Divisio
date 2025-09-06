"use client";
import { useState } from "react";
import styles from "./SiteForm.module.css";
import InputText from "../../ui/InputText";
import Checkbox from "../../ui/Checkbox";
import TextArea from "../../ui/TextArea";
export default function SiteForm({ formData, onChange, onSubmit }) {
  return (
    <form onSubmit={onSubmit}>
      <InputText
        label="Nom du site"
        name="siteName"
        value={formData?.siteName}
        onChange={onChange}
        required
      />
      <InputText
        label="Localisation"
        name="location"
        value={formData?.location}
        onChange={onChange}
      />
      <Checkbox
        label="Site actif"
        name="active"
        checked={formData?.active}
        onChange={onChange}
      />
      <TextArea
        label="Notes"
        name="notes"
        value={formData?.notes}
        onChange={onChange}
        placeholder="Infos complémentaires..."
      />
      <button type="submit" className="button button-primary">
        Créer le site
      </button>
    </form>
  );
}

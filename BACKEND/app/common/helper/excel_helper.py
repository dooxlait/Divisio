import pandas as pd

def lire_excel(fichier):
    """Lit le fichier Excel et renvoie un DataFrame"""
    print("[INFO] Lecture du fichier Excel pour l'importation des articles.")
    try:
        df = pd.read_excel(fichier)
        return df
    except Exception as e:
        raise ValueError(f"Erreur lors de la lecture du fichier Excel : {str(e)}")



def fusionner_onglets_excel(fichier):
    """Lit tous les onglets du fichier Excel et ajoute la colonne 'sheetname'. Renvoi un DataFrame fusionné."""
    print("[INFO] Enrichissement du template d'importation des articles.")
    try:
        # Lire tous les onglets du fichier Excel
        xls = pd.ExcelFile(fichier)
        dfs = []
        for nom_onglet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=nom_onglet)
            df['sheet_name'] = nom_onglet  # Ajout de la colonne 'sheet_name' avec le nom de l'onglet
            dfs.append(df)

        # Concaténer tous les DataFrames
        df_total = pd.concat(dfs, ignore_index=True)
        print(df_total.columns)
        return df_total
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'enrichissement du template : {str(e)}")
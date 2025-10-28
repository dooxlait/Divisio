import pandas as pd
import math
from marshmallow import ValidationError
from app.core.extensions import db
from app.modules.articles.models import Unite, Category, Article, Marque, Fournisseur
from app.modules.articles.schemas.article.article_schema import ArticleSchema

article_schema = ArticleSchema()

# Fonctions de lecture / extraction

def lire_excel(fichier):
    """Lit le fichier Excel et renvoie un DataFrame en ignorant les deux premières lignes."""
    print("[INFO] Lecture du fichier Excel pour l'importation des articles (titres à la ligne 3).")
    try:
        df = pd.read_excel(fichier)
        return df
    except Exception as e:
        raise ValueError(f"Erreur lors de la lecture du fichier Excel : {str(e)}")


def traiter_onglets_excel(fichier):
    """Lit tous les onglets du fichier Excel et ajoute la colonne 'marque'."""
    print("[INFO] Enrichissement du template d'importation des articles.")
    try:
        marques = pd.ExcelFile(fichier).sheet_names
        dfs = []
        for nom in marques:
            df = pd.read_excel(fichier, sheet_name=nom, header=2)
            df["MARQUE"] = nom
            dfs.append(df)
        df_total = pd.concat(dfs, ignore_index=True)
        print(df_total.columns)
        return df_total
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'enrichissement du template : {str(e)}")


# Fonctions de transformation et validation

def rajouter_marques_reference(df): 
    """Ajoute les marques de référence aux articles existants en base et commit."""
    print("[INFO] Ajout des marques de référence au DataFrame.")
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE ARTICLE"] = df["CODE ARTICLE"].astype(str).str.strip()
        df["MARQUE"] = df["MARQUE"].astype(str).str.strip()
        articles_modifies = []

        for idx, row in df.iterrows():
            code_article = row.get("CODE ARTICLE")
            nom_marque = row.get("MARQUE")
            if pd.isna(code_article) or pd.isna(nom_marque):
                print(f"[WARN] Ligne {idx} ignorée : CODE ARTICLE ou MARQUE manquant.")
                continue

            marque = Marque.query.filter_by(nom=nom_marque.upper()).first()
            if not marque:
                print(f"[WARN] Ligne {idx} : Marque '{nom_marque}' non trouvée.")
                continue

            article = Article.query.filter_by(code=str(code_article)).first()
            if not article:
                print(f"[WARN] Article avec code '{code_article}' non trouvé en base.")
                continue

            article.id_marque = marque.id
            articles_modifies.append(article)

        if articles_modifies:
            db.session.commit()

        return len(articles_modifies)

    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de l'ajout des marques de référence : {str(e)}")

def rajouter_information_pot_set(df):
    """
    Récupère un dataframe et ajoute les informations de pot aux articles existants en base.
    Renvoie le nombre d'articles modifiés.
    """

    print(f'[INFO] Ajout des informations de pot aux articles.')
    
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE POT"] = df["CODE POT"].astype(str).str.strip()
        articles_modifies = []

        for idx, row in df.iterrows():
            code_article = row.get("CODE POT")  # ou "CODE ARTICLE" si c'est le bon
            pot_marque = row.get("FOURNISSEUR")
            
            if pd.isna(code_article) or pd.isna(pot_marque):
                print(f"[WARN] Ligne {idx} ignorée : CODE ARTICLE ou POT/SET manquant.")
                continue
            
            article = Article.query.filter_by(code=str(code_article)).first()
            if not article:
                print(f"[WARN] Article avec code '{code_article}' non trouvé en base.")
                continue    
            
            fournisseur = Fournisseur.query.filter_by(nom=str(pot_marque).upper()).first()
            if not fournisseur:
                print(f"[WARN] Ligne {idx} : Fournisseur '{pot_marque}' non trouvé. Création d'un nouveau fournisseur.")
                fournisseur = Fournisseur(nom=str(pot_marque).upper())
                db.session.add(fournisseur)
                db.session.flush()  # id généré disponible
            
            article.id_fournisseur = fournisseur.id
            articles_modifies.append(article)
        if articles_modifies:
            db.session.commit()
        return len(articles_modifies)
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de l'ajout des informations de pot/set : {str(e)}")

def convertir_en_articles(df):
    """Transforme un DataFrame en liste d'objets Article validés."""
    print("[INFO] Conversion des données Excel en objets Article.")
    articles = []
    df = df.dropna(how="all")

    for idx, row in df.iterrows():
        if pd.isna(row.get("code")) or pd.isna(row.get("designation")):
            print(f"[WARN] Ligne {idx} ignorée : code ou designation manquant.")
            continue

        ean_value = row.get("ean")
        if pd.isna(ean_value) or (isinstance(ean_value, float) and math.isnan(ean_value)):
            ean_value = None
        elif isinstance(ean_value, float) and ean_value.is_integer():
            ean_value = str(int(ean_value))
        else:
            ean_value = str(ean_value)

        unite_id = None
        if not pd.isna(row.get("unite_code")):
            unite = Unite.query.filter_by(code=str(row["unite_code"])).first()
            if unite:
                unite_id = unite.id
            else:
                print(f"[WARN] Ligne {idx} : Unité '{row['unite_code']}' non trouvée.")

        categorie_id = None
        if not pd.isna(row.get("categorie_nom")):
            categorie = Category.query.filter_by(name=str(row["categorie_nom"])).first()
            if categorie:
                categorie_id = categorie.id
            else:
                print(f"[WARN] Ligne {idx} : Catégorie '{row['categorie_nom']}' non trouvée.")

        data = {
            "code": str(row["code"]),
            "designation": str(row["designation"]),
            "ean": ean_value,
            "is_active": row.get("is_active") if not pd.isna(row.get("is_active")) else True,
            "id_unite": str(unite_id) if unite_id else None,
            "id_categorie": str(categorie_id) if categorie_id else None,
        }

        try:
            article = article_schema.load(data)
            articles.append(article)
        except ValidationError as err:
            print(f"[ERROR] Ligne {idx} invalide : {err.messages}")

    return articles


# Fonctions d’enregistrement et de lecture en base

def enregistrer_articles(articles):
    """Ajoute les objets Article en base et valide la transaction."""
    print("[INFO] Enregistrement des articles en base de données.")
    try:
        db.session.add_all(articles)
        db.session.commit()
        return len(articles)
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de l'insertion en base : {str(e)}")

def modifier_articles(articles):
    """Modifie les objets Article en base et valide la transaction."""
    print("[INFO] Modification des articles en base de données.")
    try:
        db.session.commit()
        return len(articles)
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de la modification en base : {str(e)}")


def lire_articles():
    """Lit tous les articles en base de données."""
    print("[INFO] Lecture de tous les articles en base de données.")
    try:
        return Article.query.all()
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la lecture des articles : {str(e)}")


# Fonctions orchestratrices / cas d’usage

def create_article_by_list(fichier):
    """Orchestre l'import Excel en lecture, validation et persistance."""
    df = lire_excel(fichier)
    articles = convertir_en_articles(df)
    return enregistrer_articles(articles)


def enrichir_template(fichier):
    """Génère un template d'import enrichi avec les marques de référence."""
    print("[INFO] Génération du template d'importation des articles.")
    try:
        df_enrichi = traiter_onglets_excel(fichier)
        count_marque = rajouter_marques_reference(df_enrichi)
        count_pot = rajouter_information_pot_set(df_enrichi)
        total = count_marque + count_pot
        return total
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la génération du template : {str(e)}")

# Fonction d’export

def export_to_excel(articles_data, output_file):
    """Exporte une liste de dictionnaires vers un fichier Excel."""
    print(f"[INFO] Exportation des articles vers le fichier {output_file}")
    try:
        df = pd.DataFrame(articles_data)
        df.to_excel(output_file, index=False)
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'exportation vers Excel : {str(e)}")

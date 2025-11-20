import pandas as pd
import math
from marshmallow import ValidationError
from typing import Dict, List, Optional, Any
from sqlalchemy import and_
from app.core.extensions import db
from app.modules.articles.models import Unite, Category, Article, Marque, Fournisseur, ArticleComposition, Palettisation, CaracteristiqueArticle
from app.modules.articles.schemas.article.article_schema import ArticleSchema

article_schema = ArticleSchema()

# Fonctions de lecture / extraction

def lire_excel(fichier):
    """Lit le fichier Excel et renvoie un DataFrame en ignorant les deux premières lignes."""
    print("[INFO] Lecture du fichier Excel pour l'importation des articles.")
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

def ecrire_informations_caracteristiques_article(df):
    """Écrit les informations des caractéristiques des articles à partir d'un DataFrame."""
    print("[INFO] Écriture des caractéristiques des articles.")
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE ARTICLE"] = df["CODE ARTICLE"].astype(str).str.strip()
        df["PCB"] = df["PCB"].astype(float)
        df["GENCOD"] = df["GENCOD"].astype(str).str.strip()
        articles_modifies = []
        for idx, row in df.iterrows():
            code_article = row.get("CODE ARTICLE")
            pcb_value = row.get("PCB")
            ean_value = row.get("GENCOD")
            if pd.isna(code_article):
                print(f"[WARN] Ligne {idx} ignorée : CODE ARTICLE manquant.")
                continue

            article = Article.query.filter_by(code=str(code_article)).first()
            if not article:
                print(f"[WARN] Article avec code '{code_article}' non trouvé en base.")
                continue

            if not article.caracteristique:
                caracteristique = CaracteristiqueArticle(id_article=article.id)
                article.caracteristique = caracteristique

            if not pd.isna(pcb_value):
                article.caracteristique.pcb = int(pcb_value)

            if not pd.isna(ean_value) and ean_value.lower() != 'nan':
                # méthode sûre pour garder les codes commençant par 0
                article.caracteristique.ean = str(ean_value).rstrip(".0")

            articles_modifies.append(article)
        if articles_modifies:
            db.session.commit()
        return len(articles_modifies)
        
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'écriture des caractéristiques des articles : {str(e)}")


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
    
def rajouter_information_opercules(df):
    """ 
    Récupère un dataframe et ajoute les informations d'opercules aux articles existants en base.
    Renvoie le nombre d'articles modifiés.
    """
    print(f'[INFO] Ajout des informations d\'opercules aux articles.')
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE OPERCULE"] = df["CODE OPERCULE"].astype(str).str.strip()
        articles_modifies = []

        for idx, row in df.iterrows():
            code_article = row.get("CODE OPERCULE")  # ou "CODE ARTICLE" si c'est le bon
            opercule_marque = row.get("FOURNISSEUR.1")
            
            if pd.isna(code_article) or pd.isna(opercule_marque):
                print(f"[WARN] Ligne {idx} ignorée : CODE ARTICLE ou OPERCULE manquant.")
                continue
            
            article = Article.query.filter_by(code=str(code_article)).first()
            if not article:
                print(f"[WARN] Article avec code '{code_article}' non trouvé en base.")
                continue    
            
            fournisseur = Fournisseur.query.filter_by(nom=str(opercule_marque).upper()).first()
            if not fournisseur:
                print(f"[WARN] Ligne {idx} : Fournisseur '{opercule_marque}' non trouvé. Création d'un nouveau fournisseur.")
                fournisseur = Fournisseur(nom=str(opercule_marque).upper())
                db.session.add(fournisseur)
                db.session.flush()  # id généré disponible
            
            article.id_fournisseur = fournisseur.id
            articles_modifies.append(article)
        if articles_modifies:
            db.session.commit()
        return len(articles_modifies)
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de l'ajout des informations de l'opercule : {str(e)}")


def rajouter_information_pot(df):
    """
    Récupère un dataframe et ajoute les informations de pot aux articles existants en base.
    Renvoie le nombre d'articles modifiés.
    """

    print(f'[INFO] Ajout des informations de pot aux articles.')
    
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE POT"] = df["CODE POT"].astype(str).str.strip()
        df = df.drop_duplicates(subset=["CODE POT", "FOURNISSEUR"])
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
    
def rajouter_information_couvercle(df):
    """
    Récupère un dataframe et ajoute les informations de fournisseur de couvercles aux articles existants en base.
    Renvoie le nombre d'articles modifiés.
    """

    print(f'[INFO] Ajout des informations de fournisseurs de couvercles aux articles.')
    
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE COUVERCLE"] = df["CODE COUVERCLE"].astype(str).str.strip()
        df = df.drop_duplicates(subset=["CODE COUVERCLE", "FOURNISSEUR.2"])
        articles_modifies = []

        for idx, row in df.iterrows():
            code_article = row.get("CODE COUVERCLE")  # ou "CODE ARTICLE" si c'est le bon
            pot_marque = row.get("FOURNISSEUR.2")
            
            if pd.isna(code_article) or pd.isna(pot_marque):
                print(f"[WARN] Ligne {idx} ignorée : CODE ARTICLE ou COUVERCLE manquant.")
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
        raise RuntimeError(f"Erreur lors de l'ajout des informations du fournisseur couvercle : {str(e)}")
    
def rajouter_information_coiffe(df):
    """
    Récupère un dataframe et ajoute les informations de fournisseur de coiffes aux articles existants en base.
    Renvoie le nombre d'articles modifiés.
    """

    print(f'[INFO] Ajout des informations de fournisseur de coiffes aux articles.')
    
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE COIFFE"] = df["CODE COIFFE"].astype(str).str.strip()
        df = df.drop_duplicates(subset=["CODE COIFFE", "FOURNISSEUR.3"])
        articles_modifies = []

        for idx, row in df.iterrows():
            code_article = row.get("CODE COIFFE")  # ou "CODE ARTICLE" si c'est le bon
            coiffe_marque = row.get("FOURNISSEUR.3")
            
            if pd.isna(code_article) or pd.isna(coiffe_marque):
                print(f"[WARN] Ligne {idx} ignorée : CODE ARTICLE ou COIFFE manquant.")
                continue
            
            article = Article.query.filter_by(code=str(code_article)).first()
            if not article:
                print(f"[WARN] Article avec code '{code_article}' non trouvé en base.")
                continue    
            
            fournisseur = Fournisseur.query.filter_by(nom=str(coiffe_marque).upper()).first()
            if not fournisseur:
                print(f"[WARN] Ligne {idx} : Fournisseur '{coiffe_marque}' non trouvé. Création d'un nouveau fournisseur.")
                fournisseur = Fournisseur(nom=str(coiffe_marque).upper())
                db.session.add(fournisseur)
                db.session.flush()  # id généré disponible
            
            article.id_fournisseur = fournisseur.id
            articles_modifies.append(article)
        if articles_modifies:
            db.session.commit()
        return len(articles_modifies)
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de l'ajout des informations du fourisseur de coiffe : {str(e)}")
    
def rajouter_information_carton(df):
    """
    Récupère un dataframe et ajoute les informations de carton aux articles existants en base.
    Renvoie le nombre d'articles modifiés.
    """

    print(f'[INFO] Ajout des informations des fournisseur de carton aux articles.')
    
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE CARTON"] = df["CODE CARTON"].astype(str).str.strip()
        df = df.drop_duplicates(subset=["CODE CARTON", "FOURNISSEUR.4"])
        articles_modifies = []

        for idx, row in df.iterrows():
            code_article = row.get("CODE CARTON")  # ou "CODE ARTICLE" si c'est le bon
            carton_marque = row.get("FOURNISSEUR.4")
            
            if pd.isna(code_article) or pd.isna(carton_marque):
                print(f"[WARN] Ligne {idx} ignorée : CODE ARTICLE ou CARTON manquant.")
                continue
            
            article = Article.query.filter_by(code=str(code_article)).first()
            if not article:
                print(f"[WARN] Article avec code '{code_article}' non trouvé en base.")
                continue    
            
            fournisseur = Fournisseur.query.filter_by(nom=str(carton_marque).upper()).first()
            if not fournisseur:
                print(f"[WARN] Ligne {idx} : Fournisseur '{carton_marque}' non trouvé. Création d'un nouveau fournisseur.")
                fournisseur = Fournisseur(nom=str(carton_marque).upper())
                db.session.add(fournisseur)
                db.session.flush()  # id généré disponible
            
            article.id_fournisseur = fournisseur.id
            articles_modifies.append(article)
        if articles_modifies:
            db.session.commit()
        return len(articles_modifies)
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de l'ajout des informations du fournisseur de carton : {str(e)}")
    
def rajouter_information_conditionnement_a_chaud(df):
    """ Récupère un dataframe et ajoute les informations de conditionnement à chaud aux articles existants en base."""
    print(f'[INFO] Ajout des informations de conditionnement à chaud aux articles.')
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE ARTICLE"] = df["CODE ARTICLE"].astype(str).str.strip()
        articles_modifies = []

        for idx, row in df.iterrows():
            code_article = row.get("CODE ARTICLE")
            conditionnement_value = row.get("CONDI_A_CHAUD")
            if pd.isna(code_article) or pd.isna(conditionnement_value):
                print(f"[WARN] Ligne {idx} ignorée : CODE ARTICLE ou CONDITIONNEMENT A CHAUD manquant.")
                continue

            article = Article.query.filter_by(code=str(code_article)).first()
            if not article:
                print(f"[WARN] Article avec code '{code_article}' non trouvé en base.")
                continue

            if not article.caracteristique:
                caracteristique = CaracteristiqueArticle(id_article=article.id)
                article.caracteristique = caracteristique

            article.caracteristique.conditionnement_a_chaud = bool(conditionnement_value)
            articles_modifies.append(article)

        if articles_modifies:
            db.session.commit()
        return len(articles_modifies)
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de l'ajout des informations de conditionnement à chaud : {str(e)}")

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

def etablir_relation_entre_article(df):
    """Établit les relations entre articles basées sur des codes spécifiques."""
    print("[INFO] Établissement des relations entre articles.")
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE ARTICLE"] = df["CODE ARTICLE"].astype(str).str.strip()
        df = df.drop_duplicates(subset=["CODE ARTICLE"])
        relations_etablies = 0

        # Liste des composants et la colonne correspondante dans le DataFrame
        composants_info = [
            ("CODE OPERCULE", "PCB"),
            ("CODE POT", "PCB"),
            ("CODE COUVERCLE", "PCB"),
            ("CODE COIFFE", "PCB"),
            ("CODE CARTON", "PCB")
        ]

        for idx, row in df.iterrows():
            code_article = row.get("CODE ARTICLE")
            article = Article.query.filter_by(code=str(code_article)).first()

            if not article:
                print(f"[WARN] Article avec code '{code_article}' non trouvé en base.")
                continue

            for code_col, qty_col in composants_info:
                code_composant = row.get(code_col)
                if pd.isna(code_composant):
                    continue

                composant = Article.query.filter_by(code=str(code_composant)).first()
                if not composant:
                    print(f"[WARN] Composant avec code '{code_composant}' non trouvé pour l'article '{code_article}'.")
                    continue

                quantity = row.get(qty_col, 1) if code_col != "CODE CARTON" else 1
                article_composition = ArticleComposition(
                    article_id=article.id,
                    component_id=composant.id,
                    quantity=quantity
                )
                db.session.add(article_composition)
                relations_etablies += 1

        db.session.commit()
        return relations_etablies

    except Exception as e:
        raise RuntimeError(f"Erreur lors du traitement du DataFrame pour les relations : {str(e)}")

def etablir_plan_palettisation(df):
    print("[INFO] Établissement des plans de palettisation pour les articles.")
    try:
        df = df.dropna(how="all")
        df.columns = df.columns.str.strip()
        df["CODE ARTICLE"] = df["CODE ARTICLE"].astype(str).str.strip()
        df = df.drop_duplicates(subset=["CODE ARTICLE"])
        palettisations_creees = 0

        for _, row in df.iterrows():
            code_article = row.get("CODE ARTICLE")
            article = Article.query.filter_by(code=code_article).first()
            if not article:
                print(f"[WARN] Article avec code '{code_article}' non trouvé en base.")
                continue

            nb_colis_par_couche = row.get("NOMBRE DE COLIS/COUCHE")
            nb_couches_par_palette = row.get("NOMBRE DE COUCHE/PALETTE")


            if pd.isna(nb_colis_par_couche) or pd.isna(nb_couches_par_palette):
                print(f"[WARN] Données de palettisation incomplètes pour l'article '{code_article}'.")
                continue

            palettisation = article.palettisation or Palettisation(id_article=article.id)
            article.palettisation = palettisation  # assure la relation

            palettisation.nb_colis_par_couche = int(nb_colis_par_couche)
            palettisation.nb_couches_par_palette = int(nb_couches_par_palette)

            db.session.add(palettisation)
            palettisations_creees += 1

        db.session.commit()
        return palettisations_creees

    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Erreur lors de l'établissement des plans de palettisation : {str(e)}")


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

def lire_articles_filter(filters: Optional[Dict[str, Any]] = None) -> List[Article]:
    """
    Lit les articles en base de données avec filtres optionnels.

    Exemples d'utilisation :
        lire_articles()                              → tous les articles
        lire_articles(filters={"code": "PF123"})     → un seul article par code
        lire_articles(filters={"is_active": True})   → tous les articles actifs
        lire_articles(filters={"code": "PF123", "is_active": True})

    Args:
        filters: dictionnaire de filtres (clé = nom du champ, valeur = valeur recherchée)

    Returns:
        List[Article]: liste d'articles (1 seul si filtre par code, plusieurs sinon)
    """
    print("[INFO] Lecture des articles en base de données avec filtres :", filters or "aucun")

    query = Article.query

    if filters:
        # Construction dynamique des conditions
        conditions = []
        for key, value in filters.items():
            if hasattr(Article, key):
                conditions.append(getattr(Article, key) == value)
            else:
                print(f"[WARN] Filtre ignoré : le champ '{key}' n'existe pas sur Article")
        
        if conditions:
            query = query.filter(and_(*conditions))

    try:
        results = query.all()
        if filters and "code" in filters:
            # Si on cherche par code → on s'attend à 0 ou 1 résultat
            return results[0] if results else None
        return results
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
        count_pot = rajouter_information_pot(df_enrichi)
        count_opercule = rajouter_information_opercules(df_enrichi)
        count_couvercle = rajouter_information_couvercle(df_enrichi)
        count_coiffe = rajouter_information_coiffe(df_enrichi)
        count_carton = rajouter_information_carton(df_enrichi)
        count_relation = etablir_relation_entre_article(df_enrichi)
        count_palettisation = etablir_plan_palettisation(df_enrichi)
        count_caracteristique = ecrire_informations_caracteristiques_article(df_enrichi)
        count_conditionnement = rajouter_information_conditionnement_a_chaud(df_enrichi)
        total = count_marque + count_pot
        return {
            "total": total,
            "count_marque": count_marque,
            "count_pot": count_pot,
            "count_opercule": count_opercule,
            "count_couvercle": count_couvercle,
            "count_coiffe": count_coiffe,
            "count_carton": count_carton,
            "count_relation": count_relation,
            "count_palettisation": count_palettisation,
            "count_caracteristique": count_caracteristique,
            "count_conditionnement": count_conditionnement
        }
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

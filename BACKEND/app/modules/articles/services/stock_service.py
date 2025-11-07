# BACKEND\app\modules\articles\services\stock_service.py
import pandas as pd

from app.modules.articles.models import Stock, Article, Category, MouvementStock, TypeMouvement
from app.core.extensions import db

def ecrire_en_stock(**data):
    """
    Service pour écrire les informations de stock d'un article.
    """
    new_stock = Stock(**data)
    db.session.add(new_stock)
    db.session.commit()
    return new_stock

def mise_a_jour_stock_optimisee(df, utilisateur=None):
    # -------------------------
    # Nettoyage du DataFrame
    # -------------------------
    df = df.dropna(how="all")
    df.columns = df.columns.str.strip()
    df["CODE ARTICLE"] = df["CODE ARTICLE"].astype(str).str.strip()
    df["DLC"] = pd.to_datetime(df["DLC"], format="%d/%m/%Y", errors="coerce")
    df = df.sort_values(by=["CODE ARTICLE", "DLC"], na_position="last").reset_index(drop=True)

    # -------------------------
    # Précharger articles et stocks
    # -------------------------
    articles_dict = {a.code: a for a in Article.query.all()}
    stocks_dict = {(s.code_article, s.dlc): s for s in Stock.query.all()}

    mouvements_enregistres = []

    # -------------------------
    # Boucle sur le DataFrame (itertuples = plus rapide)
    # -------------------------
    for row in df.itertuples(index=False):
        code = getattr(row, "CODE ARTICLE")
        dlc = getattr(row, "DLC")
        quantite = getattr(row, "QUANTITE", 0)
        emplacement = getattr(row, "EMPLACEMENT", "Inconnu")

        # Vérifications rapides
        if pd.isna(quantite) or quantite <= 0:
            continue
        article = articles_dict.get(code)
        if not article:
            print(f"Article inconnu : {code}")
            continue

        cle_stock = (code, dlc)
        stock_existant = stocks_dict.get(cle_stock)

        if stock_existant:
            # Stock existant → déterminer type de mouvement
            if stock_existant.quantite == quantite and stock_existant.emplacement == emplacement:
                continue  # Aucun changement
            elif stock_existant.quantite == quantite and stock_existant.emplacement != emplacement:
                # Mouvement interne
                mouvement = MouvementStock(
                    id_stock=stock_existant.id,
                    type_mouvement=TypeMouvement.MOUVEMENT,
                    quantite=quantite,
                    motif=f"Déplacement interne vers {emplacement}",
                    utilisateur=utilisateur
                )
                stock_existant.emplacement = emplacement
            elif stock_existant.quantite < quantite:
                # Entrée
                delta = quantite - stock_existant.quantite
                mouvement = MouvementStock(
                    id_stock=stock_existant.id,
                    type_mouvement=TypeMouvement.ENTREE,
                    quantite=delta,
                    motif="Entrée en stock",
                    utilisateur=utilisateur
                )
                stock_existant.quantite = quantite
            else:
                # Sortie
                delta = stock_existant.quantite - quantite
                mouvement = MouvementStock(
                    id_stock=stock_existant.id,
                    type_mouvement=TypeMouvement.SORTIE,
                    quantite=delta,
                    motif="Sortie de stock",
                    utilisateur=utilisateur
                )
                stock_existant.quantite = quantite

            db.session.add(mouvement)
            mouvements_enregistres.append(mouvement)

        else:
            # Nouveau stock
            nouveau_stock = Stock(
                code_article=code,
                dlc=dlc,
                quantite=quantite,
                emplacement=emplacement
            )
            db.session.add(nouveau_stock)
            db.session.flush()  # récupérer ID avant ajout du mouvement

            mouvement = MouvementStock(
                id_stock=nouveau_stock.id,
                type_mouvement=TypeMouvement.ENTREE,
                quantite=quantite,
                motif="Création de stock",
                utilisateur=utilisateur
            )
            db.session.add(mouvement)
            mouvements_enregistres.append(mouvement)

    # Commit final
    db.session.commit()
    return mouvements_enregistres

            
        
    
def obtenir_tout_le_stock():
    """
    Service pour récupérer toutes les informations de stock.
    """
    return Stock.query.all()

def obtenir_stock_par_id(stock_id):
    """
    Service pour récupérer les informations de stock par ID.
    """
    return Stock.query.get(stock_id)

def mettre_a_jour_stock(stock_id, **data):
    """
    Service pour mettre à jour les informations de stock existantes.
    """
    stock = Stock.query.get(stock_id)
    if not stock:
        return None

    for key, value in data.items():
        setattr(stock, key, value)

    db.session.commit()
    return stock

def creer_liste_article_stock():
    """
    Service pour créer une liste des articles en stock.
    """
    # récuperer la liste des articles produit fini
    stocks_pf = (
    db.session.query(Stock)
        .join(Stock.article)
        .join(Article.category)
        .filter(Category.code == 'PF')
        .all()
)
    print(f"Stocks PF: {stocks_pf}")
    return stocks_pf
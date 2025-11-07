# BACKEND\app\modules\articles\services\stock_service.py
import pandas as pd

from app.modules.articles.models import Stock, Article, Category
from app.core.extensions import db

def ecrire_en_stock(**data):
    """
    Service pour écrire les informations de stock d'un article.
    """
    new_stock = Stock(**data)
    db.session.add(new_stock)
    db.session.commit()
    return new_stock

def ecrire_stock_par_excel(df):
    """
    Service pour écrire des entrées de stock à partir d'un fichier Excel.
    """
    df = df.dropna(how="all")
    df.columns = df.columns.str.strip()
    df["CODE ARTICLE"] = df["CODE ARTICLE"].astype(str).str.strip()
    stocks = []
    for _, row in df.iterrows():
        code_article = row.get("CODE ARTICLE")
        # trouver l'article correspondant dans la base de données
        article = Article.query.filter_by(code=code_article).first()
        if not article:
            print(f'Code article inconnu pour la ligne: {row} / {row.get("CODE ARTICLE")}')
            continue
        # test de présence de la quantité
        quantite = row.get("QUANTITE", 0)
        emplacement = row.get("EMPLACEMENT", "Inconnu")
        dlc = row.get("DLC", None)
        if pd.isna(quantite) or quantite <= 0:
            print(f'Quantité invalide pour la ligne: {row} / {quantite}')
            continue
        if pd.isna(emplacement):
            emplacement = "Inconnu"
            print(f'Emplacement manquant pour la ligne: {row}, défini sur "Inconnu"')
        if pd.isna(dlc):
            dlc = None
            print(f'DLC manquante pour la ligne: {row}, définie sur None')
        
        existing_stock = Stock.query.filter_by(article_id=article.id, dlc=dlc).first()
        # le stock existe déjà, on met à jour la quantité
        if existing_stock:
            a terminer...

            
        
    
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
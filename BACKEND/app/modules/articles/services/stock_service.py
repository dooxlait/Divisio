# BACKEND\app\modules\articles\services\stock_service.py
from app.modules.articles.models.stock import Stock
from app.core.extensions import db

def ecrire_en_stock(**data):
    """
    Service pour écrire les informations de stock d'un article.
    """
    new_stock = Stock(**data)
    db.session.add(new_stock)
    db.session.commit()
    return new_stock

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
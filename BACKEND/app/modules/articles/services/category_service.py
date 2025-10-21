from app.core.extensions import db
from app.modules.articles.models import Category

def readAllCategories():
    """
    Récupère toutes les catégories d'articles depuis la base de données.

    Returns:
        list: Une liste d'objets Category.
    """
    return db.session.query(Category).all()

def readCategoryById(category_id):
    """
    Récupère une catégorie d'articles par son ID.

    Args:
        category_id (int): L'ID de la catégorie à récupérer.

    Returns:
        Category: L'objet Category correspondant à l'ID fourni, ou None s'il n'existe pas.
    """
    return db.session.query(Category).filter(Category.id == category_id).first()

def createCategory(category):
    """
    Crée une nouvelle catégorie d'articles dans la base de données.

    Args:
        category (Category): L'objet Category à ajouter à la base de données.

    Returns:
        Category: L'objet Category nouvellement créé.
    """
    db.session.add(category)
    db.session.commit()
    return category

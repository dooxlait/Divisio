from app.modules.articles.models import Unite
from app.core.extensions import db

def create_unite(unite_data):
    """
    Service pour créer une nouvelle unité.
    """
    new_unite = Unite(**unite_data)
    db.session.add(new_unite)
    db.session.commit()
    return new_unite

def lire_unites_filter(filters=None):
    query = db.session.query(Unite)
    if filters:
        for attr, value in filters.items():
            query = query.filter(getattr(Unite, attr) == value)
    return query.first()

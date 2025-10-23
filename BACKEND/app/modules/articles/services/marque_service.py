def create_marque(**data):
    """
    Service pour créer une nouvelle marque.
    """
    from app.modules.articles.models import Marque
    from app.core.extensions import db

    new_marque = Marque(**data)
    db.session.add(new_marque)
    db.session.commit()
    return new_marque

def get_all_marques():
    """
    Service pour récupérer toutes les marques.
    """
    from app.modules.articles.models import Marque

    return Marque.query.all()

def get_marque_by_id(marque_id):
    """
    Service pour récupérer une marque par son ID.
    """
    from app.modules.articles.models import Marque

    return Marque.query.get(marque_id)

def update_marque(marque_id, **data):
    """
    Service pour mettre à jour une marque existante.
    """
    from app.modules.articles.models import Marque
    from app.core.extensions import db

    marque = Marque.query.get(marque_id)
    if not marque:
        return None

    for key, value in data.items():
        setattr(marque, key, value)

    db.session.commit()
    return marque
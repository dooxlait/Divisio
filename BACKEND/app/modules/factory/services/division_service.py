# BACKEND\app\modules\factory\services\division_service.py
from sqlalchemy import and_

from app.core.extensions import db
from app.modules.factory.models.division import Division

def get_all_divisions(filters: dict = None, sort: str = None):
    """
    Récupère les divisions avec filtres dynamiques et tri optionnel.

    Args:
        filters (dict, optional): dictionnaire de filtres {champ: valeur}.
        sort (str, optional): nom du champ pour trier (ex: "name", "type").

    Returns:
        List[Division]: liste des divisions correspondant aux critères.
    """
    query = Division.query

    # Application des filtres dynamiques
    if filters:
        conditions = []
        for key, value in filters.items():
            if hasattr(Division, key):
                conditions.append(getattr(Division, key) == value)
            else:
                print(f"[WARN] Filtre ignoré : le champ '{key}' n'existe pas sur Division")
        if conditions:
            query = query.filter(and_(*conditions))

    # Tri optionnel
    if sort and hasattr(Division, sort):
        query = query.order_by(getattr(Division, sort).asc())

    return query.all()


def update_division_service(division_id: str, data: dict):
    division = Division.query.get(division_id)
    if not division:
        return None

    for key, value in data.items():
        if hasattr(division, key):
            setattr(division, key, value)

    db.session.commit()
    return division


def create_division_service(division):
    try:
        db.session.add(division)
        db.session.commit()
        return division
    except Exception as e:
        db.session.rollback()
        print(f"[ERREUR] Échec création division: {e}")
        return None

    
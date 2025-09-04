# BACKEND\app\modules\factory\services\division_service.py
from app.core.extensions import db
from app.modules.factory.models.division import Division

def get_all_divisions(div_type=None, sort=None):
    query = Division.query

    if div_type:
        query = query.filter(Division.type == div_type)

    if sort:
        if sort == "name":
            query = query.order_by(Division.name.asc())
        elif sort == "type":
            query = query.order_by(Division.type.asc())

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

    
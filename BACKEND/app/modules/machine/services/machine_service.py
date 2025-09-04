# BACKEND\app\modules\machine\services\machine_service.py

from app.modules.machine.models.machine import Machine
from app.core.extensions import db

def get_all_machines(machine_type=None, sort=None):
    """Retourne toutes les machines avec possibilité de filtrer et trier."""
    query = Machine.query

    # Filtre par type de machine
    if machine_type:
        query = query.filter(Machine.type == machine_type)

    # Tri
    if sort:
        if sort == "name":
            query = query.order_by(Machine.name.asc())
        elif sort == "type":
            query = query.order_by(Machine.type.asc())
        else:
            # Ignore le tri inconnu (optionnel: lever une exception ou logguer)
            pass

    return query.all()

def update_machine_service(machine_id: str, data: dict):
    """Met à jour une machine existante"""
    machine_obj = Machine.query.get(machine_id)
    if not machine_obj:
        return None

    for key, value in data.items():
        if hasattr(machine_obj, key):
            setattr(machine_obj, key, value)

    db.session.commit()
    return machine_obj

def create_machine_service(machine):
    try:
        db.session.add(machine)
        db.session.commit()
        return machine
    except Exception as e:
        db.session.rollback()
        print(f"[ERREUR] Échec création machine: {e}")
        return None
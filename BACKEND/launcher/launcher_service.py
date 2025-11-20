# launcher/launcher_service.py

from app.core.extensions import db

def insert_if_empty(Model, schema, raw_data_list, entity_name="éléments", partial=False):
    if not raw_data_list:
        return False

    instances = schema.load(raw_data_list, many=True)
    
    added = 0
    for instance in instances:
        if not getattr(instance, "id", None):  # nouvel objet → pas encore en base
            db.session.add(instance)
            added += 1

    if added:
        db.session.commit()
        print(f"[SUCCÈS] {added} {entity_name} inséré(s)")
        return True
    else:
        print(f"[INFO] Tous les {entity_name} existent déjà")
        return False
# BACKEND\launcher\launcher_service.py

import traceback
from app.core.extensions import db

def insert_if_empty(model, schema, raw_data_list, label, bypass):
    """
    Insère des enregistrements dans la table `model` seulement si elle est vide,
    après validation et normalisation via un schéma Marshmallow.
    Compatible avec SQLAlchemySchema(load_instance=True) ou Schema classique.
    """
    try:
        if not model.query.first() or bypass is True:
            print(f"[INFO] Création des {label}")

            validated_data = [schema.load(raw_data) for raw_data in raw_data_list]

            # Cas 1 : le schema renvoie déjà un objet SQLAlchemy
            if validated_data and hasattr(validated_data[0], "__table__"):
                objects = validated_data
            else:
                # Cas 2 : le schema renvoie un dict → on instancie le modèle
                objects = [model(**data) for data in validated_data]

            db.session.add_all(objects)
            db.session.commit()

            print(f"[INFO] Création des {label} avec succès")
            return True
        else:
            print(f"[INFO] Aucun ajout : {label} déjà existants")
            return False
    except Exception as e:
        db.session.rollback()
        print(f"[ERREUR] Échec de l'initialisation : {e}")
        traceback.print_exc()
        return False

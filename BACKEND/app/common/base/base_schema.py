# BACKEND/app/common/base/base_schema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.core.extensions import db

class BaseSchema(SQLAlchemyAutoSchema):
    """
    Schéma de base pour tous les modèles.
    Contient les champs communs : id, created_at, updated_at.
    """
    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        load_instance = True  # Permet de créer directement des instances SQLAlchemy
        include_fk = True     # Inclut les clés étrangères dans la sérialisation
        sqla_session = db.session  # Facilite certaines opérations de load/dump

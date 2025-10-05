# BACKEND\app\modules\article\schemas\articles_types\articletype_schema_creation.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.modules.article.models import ArticleType
from app.core.extensions import db

class ArticleTypeCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ArticleType
        load_instance = True  # Permet de charger une instance du modèle
        include_fk = True  # Inclut les clés étrangères (si elles existent)
        sqla_session = db.session  # Utilise la session de la base de données

    designation = fields.String(required=True)  # Définir explicitement le champ 'designation'
    description = fields.String(required=True)  # Définir explicitement le champ 'description'
# BACKEND\app\modules\article\schemas\articles\article_schema.py

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.modules.article.models import Article
from app.core.extensions import db

class ArticleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        load_instance = True
        include_fk = True
        sqla_session = db.session

    nom_article = fields.String(required=True)
    code_externe = fields.String(required=True)  # Assurez-vous que c'est une chaîne de caractères
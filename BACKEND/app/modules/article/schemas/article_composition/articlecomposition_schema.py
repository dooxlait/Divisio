from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.modules.article.models import ArticleComposition
from app.core.extensions import db

class ArticleCompositionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ArticleComposition
        load_instance = True
        include_fk = True
        sqla_session = db.session

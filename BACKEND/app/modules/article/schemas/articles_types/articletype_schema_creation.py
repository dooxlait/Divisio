from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.modules.article.models import Article
from app.core.extensions import db
class ArticleTypeCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: Article
        load_instance: True
        include_fk = True 
        sqla_session = db.session 

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Article(BaseModel): 
    __tablename__ = "articles"

    nom_article = db.Column(db.String(100), nullable=False, unique=True)
    code_externe = db.Column(db.String(100), nullable=False, unique=True)
    type_id = db.Column(db.String(36), ForeignKey("articles_type.id"), nullable=False)

    # relation vers ArticleType
    type = relationship("ArticleType", back_populates="articles")

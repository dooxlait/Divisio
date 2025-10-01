from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Article(BaseModel): 
    __tablename__ = "articles"

    nom_article = db.Column(db.String(36), db.ForeignKey("divisions.id"), nullable=False, unique=True) # exemple : Amande nature 2x100gr Mo'Rice
    code_externe = db.Column(db.String(36), db.ForeignKey("divisions.id"), nullable=False) # exemple : 1204973

    # clé étrangère
    type_id = db.Column(db.Integer, ForeignKey("articles_type.id"), nullable=False)

    # relation vers ArticleType
    type = relationship("ArticleType", back_populates="articles")

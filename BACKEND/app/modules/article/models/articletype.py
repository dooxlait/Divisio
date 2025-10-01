from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy.orm import relationship

class ArticleType(BaseModel):
    __tablename__ = "articles_type"
    
    designation = db.Column(db.String(50), nullable=False, unique=True) # exemple : Produits fini, MP, emballages....
    description = db.Column(db.String(255), nullable=False) # definition du produit

    articles = relationship("Article", back_populates="type")

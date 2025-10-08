# BACKEND\app\modules\article\models\articletype.py

from app.common.base.base_model import BaseModel
from app.core.extensions import db
from sqlalchemy.orm import relationship

class ArticleType(BaseModel):
    __tablename__ = "articles_type"
    
    designation = db.Column(db.String(50), nullable=False, unique=True)  # ex: Produit fini, MP, Emballage...
    description = db.Column(db.String(255), nullable=False)

    # Relation vers Article
    articles = relationship("Article", back_populates="type")

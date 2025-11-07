from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Unite(BaseModel):
    """
    Modèle représentant une unité de mesure pour les articles.
    Par exemple : kilogramme, litre, pièce, etc.
    """
    __tablename__ = 'unites'

    code = db.Column(db.String(100), nullable=False, unique=True)
    libelle = db.Column(db.String(255), nullable=True)
    type_unite = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)

    # Relations
    articles = db.relationship("Article", back_populates="unite")
    stocks = db.relationship("Stock", back_populates="unite", cascade="all, delete-orphan")
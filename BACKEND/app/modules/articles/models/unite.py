from app.common.base.base_model import BaseModel
from app.core.extensions import db

class Unite(BaseModel):
    """
    Modèle représentant une unité de mesure pour les articles.
    Par exemple : kilogramme, litre, pièce, etc.
    """
    __tablename__ = 'unites'

    code = db.Column(db.String(100), nullable=False, unique=True) # Code unique de l'unité
    libelle = db.Column(db.String(255), nullable=True) # Libellé descriptif de l'unité
    type_unite = db.Column(db.String(50), nullable=True) # Type d'unité (ex: poids, volume, longueur, etc.)
    description = db.Column(db.Text, nullable=True) # Description détaillée de l'unité

    # Relations
    articles = db.relationship("Article", back_populates="unite")
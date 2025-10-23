# BACKEND\app\modules\articles\models\marques.py

from app.core.extensions import db
from app.common.base.base_model import BaseModel

class Marque(BaseModel):
    """
    Modèle représentant une marque d'article.
    Par exemple : PROTT, les prairies d'Ariege, MORICE, etc.
    """
    __tablename__ = 'marques'

    nom = db.Column(db.String(100), nullable=False, unique=True)  # Nom unique de la marque
    description = db.Column(db.Text, nullable=True)  # Description détaillée de la marque
    is_active = db.Column(db.Boolean, default=True)  # Indique si la marque est active

    # Relations
    articles = db.relationship("Article", back_populates="marque")
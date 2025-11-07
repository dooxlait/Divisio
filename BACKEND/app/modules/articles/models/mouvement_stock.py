# BACKEND\app\modules\articles\models\mouvement_stock.py

from sqlalchemy import Integer, Enum, DateTime, func
from app.core.extensions import db
from app.common.base.base_model import BaseModel
import enum

class TypeMouvement(enum.Enum):
    ENTREE = "ENTREE"
    SORTIE = "SORTIE"
    AJUSTEMENT = "AJUSTEMENT"
    MOUVEMENT = "MOUVEMENT INTERNE"

class MouvementStock(BaseModel):
    __tablename__ = "mouvements_stock"

    id_stock = db.Column(
        db.String(36),
        db.ForeignKey("stocks.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
    )

    type_mouvement = db.Column(
        Enum(TypeMouvement),
        nullable=False
    )

    quantite = db.Column(Integer, nullable=False)

    date_mouvement = db.Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    motif = db.Column(db.String(255), nullable=True)
    utilisateur = db.Column(db.String(100), nullable=True)

    # Relation vers Stock
    stock = db.relationship("Stock", back_populates="mouvements")

    # Relation vers Unite (facultatif, si tu veux l’unité du mouvement)
    id_unite = db.Column(db.Integer, db.ForeignKey("unites.id"), nullable=True)
    unite = db.relationship("Unite", back_populates="mouvements_stock")


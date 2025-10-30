# BACKEND\app\modules\articles\models\palettisation.py
from sqlalchemy import Column, Integer, ForeignKey
from app.core.extensions import db
from app.common.base.base_model import BaseModel

class Palettisation(BaseModel):
    __tablename__ = "palettisations"

    id_article = Column(
        db.String(36),
        ForeignKey("articles.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False
    )
    
    nb_colis_par_couche = Column(Integer, nullable=True)
    nb_couches_par_palette = Column(Integer, nullable=True)

    # Relation vers Article
    article = db.relationship(
        "Article",
        back_populates="palettisation",
        uselist=False
    )

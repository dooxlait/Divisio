from app.common.base.base_model import BaseModel
from app.core.extensions import db

class CaracteristiqueArticle(BaseModel):
    __tablename__ = "caracteristiques_articles"

    id_article = db.Column(db.String(36), db.ForeignKey("articles.id"), unique=True)
    pcb = db.Column(db.Integer)
    ean = db.Column(db.String(20))
    duree_vie_jours = db.Column(db.Integer)
    conditionnement_a_chaud = db.Column(db.Boolean, default=False)
    id_unite = db.Column(db.Integer, db.ForeignKey("unites.id"))

    article = db.relationship("Article", back_populates="caracteristique")
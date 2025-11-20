from app.common.base.base_model import BaseModel
from app.core.extensions import db

class CaracteristiqueArticle(BaseModel):
    __tablename__ = "caracteristiques_articles"

    id_article = db.Column(db.String(36), db.ForeignKey("articles.id"), unique=True)
    pcb = db.Column(db.Integer)
    ean = db.Column(db.String(20))
    DLC = db.Column(db.Integer)
    DGR = db.Column(db.Integer)
    conditionnement_a_chaud = db.Column(db.Boolean, default=False)
    id_unite = db.Column(db.Integer, db.ForeignKey("unites.id"))
    gamme = db.Column(db.String(100), nullable=True)
    article = db.relationship("Article", back_populates="caracteristique")
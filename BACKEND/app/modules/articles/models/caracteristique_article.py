from app.common.base.base_model import BaseModel
from app.core.extensions import db

class CaracteristiqueArticle(BaseModel):
    __tablename__ = "caracteristiques_articles"

    # Relation 1:1 forcée par unique=True
    id_article = db.Column(db.String(36), db.ForeignKey("articles.id"), unique=True, nullable=False)
    
    # Données Logistiques / Vente
    pcb = db.Column(db.Integer) # Par Combien (Colisage)
    ean = db.Column(db.String(20)) # Code barre
    
    # Données Temporelles (CRITIQUES pour le calcul)
    DLC = db.Column(db.Integer) # Remplace le dlc_std_jours que j'avais proposé
    DGR = db.Column(db.Integer) # DGR "Standard" (celle du client prévaudra souvent)
    
    # Données Techniques
    conditionnement_a_chaud = db.Column(db.Boolean, default=False)
    etiquette_sur_chaque_colis = db.Column(db.Boolean, default=True)
    gamme = db.Column(db.String(100), nullable=True)

    # Unité spécifique (ex: si le stock est en KG mais la caractéristique en COLIS)
    # Attention: Je passe en String(36) pour matcher vos autres IDs
    id_unite = db.Column(db.String(36), db.ForeignKey("unites.id"))

    # Relations
    article = db.relationship("Article", back_populates="caracteristique")
    unite = db.relationship("Unite")
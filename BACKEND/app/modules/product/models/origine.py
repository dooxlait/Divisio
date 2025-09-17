from app.core.extensions import db
from app.common.base.base_model import BaseModel


class Origine(BaseModel):
    __tablename__ = "origines"

    nom = db.Column(db.String(50), nullable=False, unique=True)   # Brebis, Vache, Soja
    code_interne = db.Column(db.String(10), unique=True, nullable=True)
    description = db.Column(db.Text, nullable=True)

    region_principale = db.Column(db.String(100), nullable=True)
    unite_mesure = db.Column(db.String(10), nullable=True)  # kg, L, T
    poids_specifique = db.Column(db.Float, nullable=True)

    statut = db.Column(db.String(20), default="actif")  # actif / inactif / test
    date_validation = db.Column(db.Date, nullable=True)
    notes_internes = db.Column(db.Text, nullable=True)

    # Relations
    produits = db.relationship("ProduitFini", back_populates="origine", lazy=True)
    # fournisseur_id = db.Column(db.Integer, db.ForeignKey("fournisseurs.id"))

    def __repr__(self):
        return f"<Origine {self.nom} - {self.code_interne}>"

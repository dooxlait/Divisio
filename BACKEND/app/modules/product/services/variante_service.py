# BACKEND/app/modules/product/services/variante_service.py

from app.core.extensions import db
from app.modules.product.models.variante import Variante

class VarianteService:
    """Service pur pour gérer les variantes de produits"""

    def get_all(self):
        """Retourne toutes les variantes"""
        return Variante.query.all()

    def get_by_id(self, variante_id):
        """Retourne une variante par son ID"""
        return Variante.query.get(variante_id)

    def create(self, data):
        """
        Crée une variante de produit.
        data doit être validé par le schema (VarianteCreateSchema)
        """
        variante = Variante(**data)
        db.session.add(variante)
        db.session.commit()
        return variante

    def update(self, variante_id, data):
        """
        Met à jour une variante existante.
        data doit être validé par le schema (VarianteUpdateSchema)
        """
        variante = self.get_by_id(variante_id)
        if not variante:
            return None
        for key, value in data.items():
            setattr(variante, key, value)
        db.session.commit()
        return variante

    def delete(self, variante_id):
        """Supprime une variante"""
        variante = self.get_by_id(variante_id)
        if not variante:
            return False
        db.session.delete(variante)
        db.session.commit()
        return True

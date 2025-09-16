# BACKEND/app/modules/product/services/produit_emballage_service.py

from app.core.extensions import db
from app.modules.product.models.produit_emballage import ProduitEmballage

class ProduitEmballageService:
    """Service pur pour gérer les emballages des produits"""

    def get_all(self):
        """Retourne tous les emballages"""
        return ProduitEmballage.query.all()

    def get_by_id(self, emballage_id):
        """Retourne un emballage par son ID"""
        return ProduitEmballage.query.get(emballage_id)

    def create(self, data):
        """Créer un emballage, data doit être validé par le schema"""
        emballage = ProduitEmballage(**data)
        db.session.add(emballage)
        db.session.commit()
        return emballage

    def update(self, emballage_id, data):
        """Mettre à jour un emballage existant, data doit être validé par le schema"""
        emballage = self.get_by_id(emballage_id)
        if not emballage:
            return None
        for key, value in data.items():
            setattr(emballage, key, value)
        db.session.commit()
        return emballage

    def delete(self, emballage_id):
        """Supprimer un emballage"""
        emballage = self.get_by_id(emballage_id)
        if not emballage:
            return False
        db.session.delete(emballage)
        db.session.commit()
        return True

# BACKEND/app/modules/product/services/produit_fini_service.py

from app.core.extensions import db
from app.modules.product.models.produit_fini import ProduitFini

class ProduitFiniService:
    """Service pur pour gérer les produits finis"""

    def get_all(self):
        """Retourne tous les produits finis"""
        return ProduitFini.query.all()

    def get_by_id(self, produit_id):
        """Retourne un produit fini par son ID"""
        return ProduitFini.query.get(produit_id)

    def create(self, data):
        """
        Crée un produit fini.
        data doit être validé par le schema et peut contenir :
        type_produit_id, variante_id, origine_id, emballages (liste), etc.
        """
        produit = ProduitFini(**data)
        db.session.add(produit)
        db.session.commit()
        return produit

    def update(self, produit_id, data):
        """
        Met à jour un produit fini existant.
        data doit être validé par le schema.
        """
        produit = self.get_by_id(produit_id)
        if not produit:
            return None
        for key, value in data.items():
            setattr(produit, key, value)
        db.session.commit()
        return produit

    def delete(self, produit_id):
        """Supprime un produit fini"""
        produit = self.get_by_id(produit_id)
        if not produit:
            return False
        db.session.delete(produit)
        db.session.commit()
        return True

    # Méthodes supplémentaires possibles pour la logique métier
    def get_by_type(self, type_produit_id):
        """Retourne tous les produits finis d’un type spécifique"""
        return ProduitFini.query.filter_by(type_produit_id=type_produit_id).all()

    def get_by_variante(self, variante_id):
        """Retourne tous les produits finis d’une variante spécifique"""
        return ProduitFini.query.filter_by(variante_id=variante_id).all()

    def get_by_origine(self, origine_id):
        """Retourne tous les produits finis d’une origine spécifique"""
        return ProduitFini.query.filter_by(origine_id=origine_id).all()

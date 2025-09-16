# BACKEND/app/modules/product/services/type_produit_service.py

from app.core.extensions import db
from app.modules.product.models.type_produit import TypeProduit

class TypeProduitService:
    """Service pur pour gérer les types de produits"""

    def get_all(self):
        """Retourne tous les types de produit"""
        return TypeProduit.query.all()

    def get_by_id(self, type_produit_id):
        """Retourne un type de produit par son ID"""
        return TypeProduit.query.get(type_produit_id)

    def create(self, data):
        """
        Crée un type de produit.
        data doit être validé par le schema (TypeProduitCreateSchema)
        """
        type_produit = TypeProduit(**data)
        db.session.add(type_produit)
        db.session.commit()
        return type_produit

    def update(self, type_produit_id, data):
        """
        Met à jour un type de produit existant.
        data doit être validé par le schema (TypeProduitUpdateSchema)
        """
        type_produit = self.get_by_id(type_produit_id)
        if not type_produit:
            return None
        for key, value in data.items():
            setattr(type_produit, key, value)
        db.session.commit()
        return type_produit

    def delete(self, type_produit_id):
        """Supprime un type de produit"""
        type_produit = self.get_by_id(type_produit_id)
        if not type_produit:
            return False
        db.session.delete(type_produit)
        db.session.commit()
        return True

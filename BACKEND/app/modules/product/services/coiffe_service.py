# BACKEND/app/modules/product/services/coiffe_service.py

from app.core.extensions import db
from app.modules.product.models.coiffe import Coiffe

class CoiffeService:
    """Service pur pour gérer les coiffes des produits"""

    def get_all(self):
        """Retourne toutes les coiffes"""
        return Coiffe.query.all()

    def get_by_id(self, coiffe_id):
        """Retourne une coiffe par son ID"""
        return Coiffe.query.get(coiffe_id)

    def create(self, data):
        """
        Crée une coiffe.
        data doit être validé par le schema (CoiffeCreateSchema)
        """
        coiffe = Coiffe(**data)
        db.session.add(coiffe)
        db.session.commit()
        return coiffe

    def update(self, coiffe_id, data):
        """
        Met à jour une coiffe existante.
        data doit être validé par le schema (CoiffeUpdateSchema)
        """
        coiffe = self.get_by_id(coiffe_id)
        if not coiffe:
            return None
        for key, value in data.items():
            setattr(coiffe, key, value)
        db.session.commit()
        return coiffe

    def delete(self, coiffe_id):
        """Supprime une coiffe"""
        coiffe = self.get_by_id(coiffe_id)
        if not coiffe:
            return False
        db.session.delete(coiffe)
        db.session.commit()
        return True

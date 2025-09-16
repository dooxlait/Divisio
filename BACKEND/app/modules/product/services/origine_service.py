# BACKEND/app/modules/product/services/origine_service.py

from app.core.extensions import db
from app.modules.product.models.origine import Origine

class OrigineService:
    """Service pur pour gérer les origines des produits"""

    def get_all(self):
        """Retourne toutes les origines"""
        return Origine.query.all()

    def get_by_id(self, origine_id):
        """Retourne une origine par son ID"""
        return Origine.query.get(origine_id)

    def create(self, data):
        """Créer une origine, data doit être validé par le schema"""
        origine = Origine(**data)
        db.session.add(origine)
        db.session.commit()
        return origine

    def update(self, origine_id, data):
        """Mettre à jour une origine existante, data doit être validé par le schema"""
        origine = self.get_by_id(origine_id)
        if not origine:
            return None
        for key, value in data.items():
            setattr(origine, key, value)
        db.session.commit()
        return origine

    def delete(self, origine_id):
        """Supprimer une origine"""
        origine = self.get_by_id(origine_id)
        if not origine:
            return False
        db.session.delete(origine)
        db.session.commit()
        return True

# BACKEND/app/modules/product/services/carton_service.py

from app.core.extensions import db
from app.modules.product.models.carton import Carton

class CartonService:
    """Service pur pour gérer les cartons"""

    def get_all(self):
        """Retourne tous les cartons"""
        return Carton.query.all()

    def get_by_id(self, carton_id):
        """Retourne un carton par son ID"""
        return Carton.query.get(carton_id)

    def create(self, data):
        """Créer un carton, data doit être validé par le schema"""
        carton = Carton(**data)
        db.session.add(carton)
        db.session.commit()
        return carton

    def update(self, carton_id, data):
        """Mettre à jour un carton existant, data doit être validé par le schema"""
        carton = self.get_by_id(carton_id)
        if not carton:
            return None
        for key, value in data.items():
            setattr(carton, key, value)
        db.session.commit()
        return carton

    def delete(self, carton_id):
        """Supprimer un carton"""
        carton = self.get_by_id(carton_id)
        if not carton:
            return False
        db.session.delete(carton)
        db.session.commit()
        return True

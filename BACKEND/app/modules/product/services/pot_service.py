# BACKEND/app/modules/product/services/pot_service.py

from app.core.extensions import db
from app.modules.product.models.pot import Pot

class PotService:
    """Service pur pour gérer les pots des produits"""

    def get_all(self):
        """Retourne tous les pots"""
        return Pot.query.all()

    def get_by_id(self, pot_id):
        """Retourne un pot par son ID"""
        return Pot.query.get(pot_id)

    def create(self, data):
        """
        Crée un pot.
        data doit être validé par le schema (PotCreateSchema)
        """
        pot = Pot(**data)
        db.session.add(pot)
        db.session.commit()
        return pot

    def update(self, pot_id, data):
        """
        Met à jour un pot existant.
        data doit être validé par le schema (PotUpdateSchema)
        """
        pot = self.get_by_id(pot_id)
        if not pot:
            return None
        for key, value in data.items():
            setattr(pot, key, value)
        db.session.commit()
        return pot

    def delete(self, pot_id):
        """Supprime un pot"""
        pot = self.get_by_id(pot_id)
        if not pot:
            return False
        db.session.delete(pot)
        db.session.commit()
        return True

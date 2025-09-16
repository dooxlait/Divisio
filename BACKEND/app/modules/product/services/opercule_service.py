# BACKEND/app/modules/product/services/opercule_service.py

from app.core.extensions import db
from app.modules.product.models.opercule import Opercule

class OperculeService:
    """Service pur pour gérer les opercules des produits"""

    def get_all(self):
        """Retourne tous les opercules"""
        return Opercule.query.all()

    def get_by_id(self, opercule_id):
        """Retourne un opercule par son ID"""
        return Opercule.query.get(opercule_id)

    def create(self, data):
        """
        Crée un opercule.
        data doit être validé par le schema (OperculeCreateSchema)
        """
        opercule = Opercule(**data)
        db.session.add(opercule)
        db.session.commit()
        return opercule

    def update(self, opercule_id, data):
        """
        Met à jour un opercule existant.
        data doit être validé par le schema (OperculeUpdateSchema)
        """
        opercule = self.get_by_id(opercule_id)
        if not opercule:
            return None
        for key, value in data.items():
            setattr(opercule, key, value)
        db.session.commit()
        return opercule

    def delete(self, opercule_id):
        """Supprime un opercule"""
        opercule = self.get_by_id(opercule_id)
        if not opercule:
            return False
        db.session.delete(opercule)
        db.session.commit()
        return True

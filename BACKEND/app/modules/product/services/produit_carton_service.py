# BACKEND/app/modules/product/services/produit_carton_service.py

from app.core.extensions import db
from app.modules.product.models.produit_carton import ProduitCarton

class ProduitCartonService:
    """Service pur pour gérer les liaisons produit ↔ carton"""

    def get_all(self):
        return ProduitCarton.query.all()

    def get_by_id(self, pc_id):
        return ProduitCarton.query.get(pc_id)

    def create(self, data):
        pc = ProduitCarton(**data)
        db.session.add(pc)
        db.session.commit()
        return pc

    def update(self, pc_id, data):
        pc = self.get_by_id(pc_id)
        if not pc:
            return None
        for key, value in data.items():
            setattr(pc, key, value)
        db.session.commit()
        return pc

    def delete(self, pc_id):
        pc = self.get_by_id(pc_id)
        if not pc:
            return False
        db.session.delete(pc)
        db.session.commit()
        return True

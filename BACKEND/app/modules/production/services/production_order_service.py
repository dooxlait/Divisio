from app.core.extensions import db
from app.modules.production.models.production_order import ProductionOrder

def create_order(**data):
    new_production_order = ProductionOrder(**data)
    db.session.add(new_production_order)
    db.session.commit()
    return new_production_order

def read_orders(filters=None):
    query = ProductionOrder.query
    if filters:
        query = query.filter_by(**filters)
    return query.all()
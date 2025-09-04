# BACKEND\app\common\utils.py

from datetime import datetime

def normalize_date(value):
    """Convertit JJ/MM/AAAA ou YYYY-MM-DD en ISO."""
    if not value:
        return None
    if isinstance(value, datetime):
        return value.date().isoformat()
    if "/" in value:
        return datetime.strptime(value, "%d/%m/%Y").date().isoformat()
    return value
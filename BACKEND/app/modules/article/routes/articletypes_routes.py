from flask import Blueprint

from app.common.response.response import success_response, error_response

articletype_bp = Blueprint('articletype', __name__, url_prefix="/articletype")
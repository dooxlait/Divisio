from flask import Blueprint

from app.common.response.response import success_response, error_response

articletype_bp = Blueprint('articletype', __name__, url_prefix="/articletype")

@articletype_bp.routes("/articletype", methods=['GET'])
def getArticleType_route():
    pass

@articletype_bp.routes('/articletype', methods=['POST'])
def readArticleType_route():
    pass
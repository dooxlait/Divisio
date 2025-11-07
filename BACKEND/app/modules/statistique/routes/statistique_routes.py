from flask import Blueprint, request, send_file
from datetime import datetime
import os

from app.common.response.response import success_response, error_response

statistique_bp = Blueprint('statistique_bp', __name__, url_prefix='/statistiques')

@statistique_bp.route("/summary", methods=["GET"])
def get_statistics_summary():
    return success_response({
        "payload": None,
        "message": "Statistics summary endpoint is under construction."
    })
        
# BACKEND\app\common\response\response.py

from flask import jsonify
from .response_schema import APIResponseSchema

response_schema = APIResponseSchema()

def success_response(data=None, message=None, status_code=200):
    payload = {
        "status": "success",
        "payload": data,
        "message": message
    }
    # Validation avant retour
    response_schema.load(payload)
    return jsonify(payload), status_code

def error_response(message, status_code=400, data=None):
    payload = {
        "status": "error",
        "payload": data,
        "message": message
    }
    response_schema.load(payload)
    return jsonify(payload), status_code

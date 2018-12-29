import jwt

from instance.config import secret_key
from flask import request, jsonify
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
        if not token:
            return jsonify({"result": "Token not found"}), 401
        try:
            token = jwt.decode(token,secret_key, algorithms='HS256'), 401
        except:
            return jsonify({"result": "Invalid token"})
        return f(*args, **kwargs)
    return decorated

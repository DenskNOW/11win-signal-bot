from functools import wraps
from flask import request, Response

ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "1234"

def check_auth(username, password):
    return username == ADMIN_LOGIN and password == ADMIN_PASSWORD

def authenticate():
    return Response(
        'Authentication required.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
from flask import request
from functools import wraps
import jwt
from app import app
from app.models.DB.user import User



def token_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        token = None

        if not "token" in request.headers:
            return "Token is missing!",400
        token = request.headers['token']
        
        
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except jwt.ExpiredSignatureError:
            return "Session Expired",401
        except:
            return "Invalid token!",401
        
        if "type" in data:
            return {'token': token},307 

        current_user = User.query.get(data["user"]["id"])
        if not current_user.is_active:
            return "Usuário inativo!",401

        kwargs["current_user"] = current_user

        return function(*args, **kwargs)
        
    return wrapper

def temp_token_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        token = None

        if not "token" in request.headers:
            return "Token is missing!",400
        token = request.headers['token']
        
        
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except jwt.ExpiredSignatureError:
            return "Session Expired",401
        except:
            return "Invalid token!",401
        
        if "type" in data:
            current_user = User.query.get(data["user_id"])
        else:
            current_user = User.query.get(data["user"]["id"])

        kwargs["current_user"] = current_user

        return function(*args, **kwargs)
        
    return wrapper


def admin_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        if not kwargs["current_user"].is_admin:
            return "Permissão negada",401

        return function(*args, **kwargs)
        
    return wrapper


from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app,resources={r'*':{'origins':'http://localhost:4200'}})
ma = Marshmallow(app)
db = SQLAlchemy(app)
# jwt = JWTManager(app)


from app.controllers import *
from app.controllers.auth import *
from app.controllers.users import *


from app.Functions.system_init import *

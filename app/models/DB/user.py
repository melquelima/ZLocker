from app import db,ma
from sqlalchemy import Float,Column,Integer,String,ForeignKey,DateTime,Time,Boolean,Date
from datetime import datetime,date,timedelta
from marshmallow import Schema, fields
from app.models.Others.mallow import mallow
from app.models.Others.sql_uteis import auxDB

class User(db.Model,auxDB):
    __tablename__ = "users"

    username            = Column(String(255),nullable = False,unique=True)
    name                = Column(String(255))
    password            = Column(String(512),nullable = False)
    is_admin            = Column(Boolean,nullable = False)
    level               = Column(String(512))
    email               = Column(String(255))
    phone               = Column(String(255))
    is_active           = Column(Boolean(255),nullable = False)
    description         = Column(String(512))
    last_reset          = Column(DateTime())
    Roles               = db.relationship("UserRole",backref="user")

    def toJson(self,schema = None):
        return mallow(schema if schema else UserSchema,self)
    
    def get_roles(self):
        return [{"role":r.Role.name,"role_aux":r.Role.aux_rule} for r in self.Roles]

class UserSchema(ma.Schema):
    id          = fields.Integer()
    username    = fields.String()
    name        = fields.String()
    email       = fields.String()
    level       = fields.String()
    phone       = fields.String()
    is_active   = fields.Boolean()
    is_admin    = fields.Boolean()
    description = fields.String()
    roles       = fields.Function(lambda x:x.get_roles())

a = 1
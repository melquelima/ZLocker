from app import db,ma
from sqlalchemy import *
from marshmallow import fields
from app.models.Others.mallow import mallow
from app.models.Others.sql_uteis import auxDB

class Role(db.Model,auxDB):
    __tablename__ = "roles"

    name                = Column(String(255),nullable = False,unique=True)
    aux_rule            = Column(String(255))

    def toJson(self,schema = None):
        return mallow(schema if schema else RoleSchema,self)

class UserRole(db.Model,auxDB):
    __tablename__ = "user_roles"

    id_user             = Column(Integer,ForeignKey('users.id'),nullable=False)
    id_role             = Column(Integer,ForeignKey('roles.id'),nullable=False)
    Role                = db.relationship("Role",foreign_keys=id_role)


class RoleSchema(ma.Schema):
    id       = fields.Integer()
    name     = fields.String()
    aux_rule = fields.String()

a = 1
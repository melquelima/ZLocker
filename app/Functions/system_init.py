from app import db
from app.models.DB.user import User
# from app.models.DB.roles import *
from glob import glob
from datetime import datetime as dt

from sqlalchemy import inspect

# default_roles = ['client_viewer','client_editor','user_viewer','user_editor']

if not db.engine.table_names():
    db.create_all()

    
    # for role in default_roles:
    #     Role(name=role).save()
    
    #def_user = User(username="admin",level="user",is_active=True,is_admin=True)
    #def_user.set_password("admin")
    #def_user.save()

    # def_user = User(username="admin2",name="Admin2",email="admin2@email.com",phone="(11)9.2222-2222",level="Administrador",is_active=True,is_admin=True)
    # def_user.set_password("admin")
    # def_user.save()

    a = 1




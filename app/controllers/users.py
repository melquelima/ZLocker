from flask.json import jsonify
from app import app
from app.models.DB.user import User
from app.models.Decorators.auth import admin_required, token_required
from app.models.Decorators.fields import *

@app.route('/api/users')
@token_required
def all_users(current_user):
    users = User.query.all()
    return jsonify([x.toJson() for x in users])


@app.route('/api/user/<id_user>',methods=['POST'])
@token_required
@admin_required
@fields_get()
@fields_required({"name":str,"level":str,"email":str,"phone":str,"username":str,"is_active":bool,"description":str,"roles":list})
@fields_notEmpty(["name","level","email","phone","username","is_active"])
@fields_ValidateList('roles',str)
def edit_user(current_user,id_user,fields):

    user = User.query.get(id_user)
    if not user: return "User not found!",404

    if not fields["is_active"] and str(current_user.id) == id_user:
        return "Ação inválida!",400


    roles = fields.pop("roles")

    for x in fields:
        setattr(user,x,fields[x])
    
    user.save()

    return jsonify(user.toJson())
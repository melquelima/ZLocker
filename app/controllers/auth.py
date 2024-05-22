
from app import app,lm
from werkzeug.security import check_password_hash as CPH
from flask import request,make_response,url_for,redirect,flash,render_template,redirect
from app.models.DB.user import User,UserSchema
from flask_login import login_user,login_required,current_user,logout_user
from datetime import timedelta
from datetime import datetime
import jwt
from werkzeug.security import check_password_hash as CPH
from dateUts import *

from app.models.Decorators.auth import temp_token_required
from app.models.Decorators.fields import fields_get, fields_notEmpty, fields_required
from app.models.Forms.login import LoginForm
from glob import glob


@app.route('/create_admin',methods=['POST','GET'])
def create_admin():
    if glob('./app/data/done'): return redirect('home')
    if current_user.is_authenticated: return redirect("home")
    if User.query.count() >0: return redirect('home')

    form = LoginForm()
    if form.validate_on_submit():
        usr = User(username=form.username.data,level="user",is_active=True,is_admin=True)
        usr.set_password(form.password.data)
        usr.save()
        login_user(usr)
        open('./app/data/done','+w').close()
        return redirect('home') 

    if form.username.data is None: 
        form.username.data = 'admin'

    return render_template("create_admin_user.html",form=form,user=current_user)

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return "Please insert username and password",401

    user:User = User.query.filter_by(username=auth.username).first()

    if not user:
        return "Usuário ou senha invalida!",401


    if user.check_password(auth.password):
        if not user.is_active:
            return "Usuário inativo!",401
        if not user.last_reset or interval(today(),tomorrow().date,in_days=True)>10:
            temp_token = jwt.encode({'user_id':user.id,'type':'change-pwd','exp':datetime.utcnow() + timedelta(minutes=5)},app.config['SECRET_KEY'])
            rsp = make_response({'token': temp_token.decode('UTF-8')})
            return rsp,307
        token = jwt.encode({'user':user.toJson(),'exp':datetime.utcnow() + app.config['JWT_ACCESS_TOKEN_EXPIRES']},app.config['SECRET_KEY'])
        rsp = make_response({'token': token.decode('UTF-8'),'user':user.toJson()})
        return rsp
    else:
        return "Usuário ou senha invalida!",401


@app.route('/reset_password',methods=['POST'])
@temp_token_required
@fields_get()
@fields_required({'old_pwd':str,'new_pwd':str})
@fields_notEmpty(['old_pwd','new_pwd'])
def reset_password(current_user,fields):
    if(current_user.check_password(fields['old_pwd'])):
        current_user.set_password(fields['new_pwd'])
        current_user.last_reset = now().date
        current_user.save()
        token = jwt.encode({'user_id':current_user.id,'exp':datetime.utcnow() + app.config['JWT_ACCESS_TOKEN_EXPIRES']},app.config['SECRET_KEY'])
        rsp = make_response({'token': token.decode('UTF-8'),'user':current_user.toJson()})
        return rsp
    return 'Senha incorreta!',410
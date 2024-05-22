
from app import app,lm
from werkzeug.security import check_password_hash as CPH
from flask import render_template,send_from_directory,request,flash,redirect
from glob import glob
from flask_login import login_required, current_user
from app.models.Forms.login import LoginForm

@app.before_request
def show_teardown():
    if "/static" in request.url: return
    if "/create_admin" in request.url: return
    if not glob('./app/data/done'):
       return redirect('create_admin')

@app.route('/')
@login_required
def home(path=None):
  return render_template('home.html')


# @app.route('/assets/<path:path>', methods=['GET'])
# def static_proxy(path):
#   return send_from_directory('./static/assets', path)
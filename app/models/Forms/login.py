from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,MultipleFileField,SelectField,FileField
from wtforms.validators import DataRequired,ValidationError
from flask_wtf.file import FileAllowed, FileRequired

def MatchPassword(form, field):
    if form.password.data.strip() != field.data:
        raise ValidationError('Senha nao confere!')

class LoginForm(FlaskForm):
    username = StringField("userName",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    confirm_password = PasswordField("confirm_password",validators=[DataRequired(),MatchPassword])




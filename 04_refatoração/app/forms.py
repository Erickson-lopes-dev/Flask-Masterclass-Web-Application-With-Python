from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import PasswordField, BooleanField, SubmitField


class LoginForm(FlaskForm):
    email = EmailField('Email')
    password = PasswordField('Senha')
    remember = BooleanField('Permanecer conectado')
    submit = SubmitField('Logar')

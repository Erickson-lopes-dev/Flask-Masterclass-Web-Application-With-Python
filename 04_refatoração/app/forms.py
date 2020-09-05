from flask_wtf import FlaskForm
from wtforms.fields import (BooleanField, PasswordField, StringField,
                            SubmitField, SelectField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length
from app.models import Book


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters.")
    ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        DataRequired("o campo é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 á 6 caracters.")
    ])
    submit = SubmitField("Cadastrar")


class BookForm(FlaskForm):
    name = StringField("Nome do livro", validators=[
        DataRequired("o campo é obrigatório")
    ])
    submit = SubmitField("Salvar")


class UserBookForm(FlaskForm):
    book = SelectField("Livro", coerce=int)
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book.choices = [ 
            (book.id, book.name) for book in Book.query.all()
        ]
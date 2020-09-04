from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# tipo de banco de dados que ira usar / sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# parâmetros obrigadorio para o sqlalchemy rodas na aplicação
db = SQLAlchemy(app)


# modelo de dados dos registros
class User(db.Model):
    # nome da tabela
    __tablename__ = "users"
    # colunas
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255))
    profile = db.relationship('Profile', backref='user', uselist=False)

    def __str__(self):
        return self.name


# modelo de dados dos registros
class Profile(db.Model):
    # nome da tabela
    __tablename__ = "profiles"
    # colunas
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Unicode(124), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __str__(self):
        return self.name


@app.route("/")
def index():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route("/user/delete/<int:id>")
def delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect('/')


@app.route('/user/<int:id>')
def index_user(id):
    user = User.query.filter_by(id=id).first()
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

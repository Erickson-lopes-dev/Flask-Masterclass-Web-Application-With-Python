from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# tipo de banco de dados que ira usar / sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

# parâmetros obrigadorio para o sqlalchemy rodas na aplicação
db = SQLAlchemy(app)

login_manager = LoginManager(app)


@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)


# modelo de dados dos registros
class User(db.Model, UserMixin):
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
@login_required
def index_user(id):
    user = User.query.filter_by(id=id).first()
    return render_template('user.html', user=user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User()
        user.name = request.form['name']
        user.email = request.form['email']
        user.password = generate_password_hash(request.form['password'])

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    errors = {}
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        errors = {}

        # se não existir redireciona
        if not user:
            flash('Credênciais inválidas.')
            return redirect(url_for('login'))

        # verifica se a senha esta correta
        if not check_password_hash(user.password, password):
            flash('Credênciais inválidas.')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html', errors=errors)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

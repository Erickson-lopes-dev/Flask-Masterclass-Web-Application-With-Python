from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# parâmetros obrigadorio para o sqlalchemy rodas na aplicação
db = SQLAlchemy(app)

# tipo de banco de dados que ira usar / sqlite3
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/")
def index():
    return 'Página em branco'


if __name__ == '__main__':
    app.run(debug=True, port=8000)

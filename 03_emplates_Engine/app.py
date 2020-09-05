from datetime import datetime

from Templates_Engine.filtros import format_date


from flask import Flask, render_template, flash

app = Flask(__name__, template_folder='templates_aula', static_folder='static')
app.config['SECRET_KEY'] = 'sserve'
app.jinja_env.filters["formatdate"] = format_date


@app.route('/templates')
def templates():
    flash("Usuário criado com sucesso!")

    usuarios = True
    # flash("passei por aqui!")
    return render_template('index.html', user=usuarios)


@app.route('/users')
def users():
    users_list = [{
        'name': 'Marcus',
        'anos': 99,
        'email': 'oi@gmauil.com',
        'active': True,
        'since': datetime.utcnow()
    },
        {
            'name': 'CAPS',
            'anos': 99,
            'email': 'oi@gmauil.com',
            'active': False,
            'since': datetime.utcnow()
        },

    ]
    flash(message="Users Routes", category='success')
    return render_template('users.html', users_list=users_list)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

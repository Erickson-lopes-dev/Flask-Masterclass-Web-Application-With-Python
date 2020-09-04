from flask import Flask, render_template, flash

app = Flask(__name__, template_folder='templates_aula')
app.config['SECRET_KEY'] = 'sserve'

@app.route('/templates')
def templates():
    users = {
        'name': 'Marcus',
        'anos': 99,
        'email': 'oi@gmauil.com'
    }

    flash("Usuário criado com sucesso!")
    # flash("passei por aqui!")
    return render_template('index.html', user=users)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

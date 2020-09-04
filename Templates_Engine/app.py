from flask import Flask, render_template


app = Flask(__name__, template_folder='templates_aula')


@app.route('/templates')
def templates():
    users = {
        'name': 'Marcus',
        'anos': 99,
        'email': 'oi@gmauil.com'
    }
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

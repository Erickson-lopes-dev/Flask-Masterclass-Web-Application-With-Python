from flask import Flask, render_template


app = Flask(__name__, template_folder='templates_aula')


@app.route('/templates')
def templates():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)

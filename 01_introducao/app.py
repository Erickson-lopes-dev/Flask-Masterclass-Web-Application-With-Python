from flask import Flask, request, jsonify, Response, redirect, render_template
from flask_bootstrap import Bootstrap

# indicando a aplicação
app = Flask(__name__)
Bootstrap(app)


# templates_aula
@app.route('/template')
def template():
    return render_template('index.html')


# o Flask lida com response automaticamente
@app.route("/response")
def response():
    headers = {
        "Content-Type": "text/html"
    }
    return Response(f"Uma resposta do servidor {headers}", 200, headers=headers)


# Criando Rota
@app.route("/")
def index():
    return "<a href='/posts'>Posts</a>"


# redirect
@app.route("/redirect")
def redirect_url():
    return redirect("/response")


# Recebendo dados da url e request
@app.route("/posts")
@app.route("/posts/<int:id>")
def posts(id):
    # ?titulo=mensagem
    titulo = request.args.get("titulo")

    data = dict(
        path=request.path,
        referrer=request.referrer,
        content_type=request.content_type,
        method=request.method,
        titulo=titulo,
        id=id
    )
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

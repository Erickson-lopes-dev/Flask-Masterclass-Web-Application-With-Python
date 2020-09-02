from flask import Flask, request, jsonify, Response

# indicando a aplicação
app = Flask(__name__)


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

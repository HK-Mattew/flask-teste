from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return """
    Olá, Aqui está minha home page!

    <a href="/painel">Meu Painel</a>
    """



@app.route('/painel', methods=['GET'])
def painel():
    name = request.args.get('name', '')
    return f'Aqui é seu painel {name} ;)'

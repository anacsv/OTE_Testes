from flask import Flask

# -- criação de um objeto flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "Meu cadastro de produtos"

@app.route('/usuario')
def usuario():
    return "Usuario"

@app.route('/pessoa_juridica')
def pessoa_juridica():
    return "Pessoa Juridica"

@app.route('/produto')
def produto():
    return "Produto"
    
app.run()
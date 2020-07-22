from flask import Flask

# -- criação de um objeto flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "Meu cadastro de produtos"

@app.route('/usuario')
def usuario():
    return "Usuario"

    
app.run()
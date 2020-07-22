from flask import Flask, render_template

# -- criação de um objeto flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/usuario')
def usuario():
    return "Usuario"

@app.route('/pessoa_fisica')
def pessoa_fisica():
    rreturn render_template('pessoa_fisica.html')

@app.route('/pessoa_juridica')
def pessoa_juridica():
    return "Pessoa Juridica"

@app.route('/produto')
def produto():
    return "Produto"

    
app.run()
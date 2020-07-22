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
    return "pessoa_fisica"

@app.route('/pessoa_juridica')
def pessoa_juridica():
    return render_template('pessoa_juridica.html')

@app.route('/produto')
def produto():
    return render_template('produto.html')
    
app.run()
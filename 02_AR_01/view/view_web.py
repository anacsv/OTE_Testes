import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from flask import Flask, render_template

from model.usuario import Usuario
from model.produto import Produto
from dao.usuario_dao import UsuarioDao
from model.pessoa_fisica import PessoaFisica
from dao.pessoa_fisica_dao import PessoaFisicaDao
from dao.produto_dao import ProdutoDao
from dao.pessoa_juridica_dao import PessoaJuridicaDao


# -- criação de um objeto flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/usuario')
def usuario():
    dao = UsuarioDao()
    lista = dao.read()
    return render_template("usuario.html", usuarios=lista )

@app.route('/pessoa_fisica')
def pessoa_fisica():
    dao = PessoaFisicaDao()
    lista = dao.read()
    return render_template("pessoa_fisica.html", pessoa_fisica=lista)

@app.route('/pessoa_juridica')
def pessoa_juridica():
    dao = PessoaJuridicaDao()
    lista = dao.read()
    return render_template('pessoa_juridica.html', pessoa_juridica=lista)

@app.route('/produto')
def produto():
    dao = ProdutoDao()
    lista = dao.read()
    return render_template('produto.html', produtos=lista)
    
app.run()
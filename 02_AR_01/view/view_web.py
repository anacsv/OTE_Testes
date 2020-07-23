import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from flask import Flask, render_template, request

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

#----------- usuarios 
@app.route('/usuario')
def usuario():
    dao = UsuarioDao()
    lista = dao.read()
    return render_template("usuario.html", usuarios=lista )

@app.route('/usuario/usuario_edit')
def usuario_edit():
    # lendo parametros get(url)
    id = request.args.get('id')
    dao = UsuarioDao()
    u = dao.read(id)
    return render_template("usuario_edit.html", usuario = u ) 

#----------- usuarios fim
@app.route('/pessoa_fisica')
def pessoa_fisica():
    dao = PessoaFisicaDao()
    lista = dao.read()
    return render_template("pessoa_fisica.html", pessoa_fisica=lista)

#----------- pessoa física fim
@app.route('/pessoa_juridica')
def pessoa_juridica():
    dao = PessoaJuridicaDao()
    lista_pessoa_juridica = dao.read()
    return render_template('pessoa_juridica.html', pessoas_juridicas=lista_pessoa_juridica)

@app.route('/pessoa_juridica/pessoa_juridica_edit')
def pessoa_juridica_edit():
    id = request.args.get('id')
    dao = PessoaJuridicaDao()
    pjd = dao.read(id)
    return render_template('pessoa_juridica_edit.html', pessoa_juridica=pjd)

#------------ pessoa jurídica fim
@app.route('/produto')
def produto():
    dao = ProdutoDao()
    lista = dao.read()
    return render_template('produto.html', produtos=lista)
    
app.run()
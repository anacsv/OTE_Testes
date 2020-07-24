import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from flask import Flask, render_template, request, redirect

from model.usuario import Usuario
from model.produto import Produto
from dao.usuario_dao import UsuarioDao
from model.pessoa_fisica import PessoaFisica
from dao.pessoa_fisica_dao import PessoaFisicaDao
from dao.produto_dao import ProdutoDao
from dao.pessoa_juridica_dao import PessoaJuridicaDao
from model.pessoa_juridica import PessoaJuridica


# -- criação de um objeto flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

#------------------------------------------- usuarios 
# ----- Listar
@app.route('/usuario')
def usuario():
    msg = request.args.get('msg')
    if not msg:
        msg = ''
    dao = UsuarioDao()
    lista = dao.read()
    return render_template("usuario.html", usuarios=lista, msg=msg )

# ----- Editar
@app.route('/usuario/read')
def read():
    # lendo parametros get(url)
    id = request.args.get('id')
    dao = UsuarioDao()
    u = dao.read(id)
    return render_template("usuario_read.html", usuario = u ) 

@app.route('/usuario/usuario_edit')
def usuario_edit():
    # lendo parametros get(url)
    u = Usuario()
    u.id = request.args.get('id')
    u.email = request.args.get('email')
    u.senha = request.args.get('senha')
    dao = UsuarioDao()
    result = dao.update(u)
    return render_template("usuario_read.html", usuario = u,  msg = result ) 

# ----- Fim Editar

# ----- Criar
# ----- Fim Criar

# ----- Deletar 
@app.route('/usuario/delete')
def delete():
    # lendo parametros get(url)
    id = request.args.get('id')
    dao = UsuarioDao()
    result = dao.delete(id)
    return redirect(f'/usuario?msg={result}')
#------------------------------------------- usuarios fim
@app.route('/pessoa_fisica')
def pessoa_fisica():
    dao = PessoaFisicaDao()
    lista = dao.read()
    return render_template("pessoa_fisica.html", pessoa_fisica=lista)

#----------- pessoa física fim

#------------------------------------------- pessoa juridica
# ----- Listar
@app.route('/pessoa_juridica')
def pessoa_juridica():
    msg_pjd = request.args.get('msg_pjd')
    if not msg_pjd:
        msg_pjd = ''
    dao = PessoaJuridicaDao()
    lista_pessoa_juridica = dao.read()
    return render_template('pessoa_juridica.html', pessoas_juridicas=lista_pessoa_juridica, msg_pjd=msg_pjd)

# ----- Editar
@app.route('/pessoa_juridica/read')
def pessoa_juridica_read():
    # lendo parametros get(url)
    id = request.args.get('id')
    dao = PessoaJuridicaDao()
    pjd = dao.read(id)
    return render_template("pessoa_juridica_read.html", pessoa_juridica = pjd ) 


@app.route('/pessoa_juridica/pessoa_juridica_edit')
def pessoa_juridica_edit():
    pjd = PessoaJuridica()
    pjd.id = request.args.get('id')
    pjd.nome = request.args.get('nome')
    pjd.data = request.args.get('data')
    pjd.cnpj = request.args.get('cnpj')
    dao = PessoaJuridicaDao()
    result = dao.update(pjd)
    return render_template('pessoa_juridica_read.html', pessoa_juridica=pjd, msg_pjd = result)
# ----- Fim Editar

# ----- Criar
# ----- Fim Criar

# ----- Deletar 
@app.route('/pessoa_juridica/delete')
def pessoa_juridica_delete():
    # lendo parametros get(url)
    id = request.args.get('id')
    dao = PessoaJuridicaDao()
    result = dao.delete(id)
    return redirect(f'/pessoa_juridica?msg={result}')

#------------------------------------------- pessoa juridica fim

#----------- produtos

@app.route('/produto')
def produto():
    dao = ProdutoDao()
    lista = dao.read()
    return render_template('produto.html', produtos=lista)

@app.route('/produto/produto_edit')
def produto_edit():
    id = request.args.get('id')
    dao = ProdutoDao()
    p = dao.read(id)
    return render_template('produto_edit.html', produto = p)
#----------- produtos fim
    
app.run()
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

@app.route('/usuario/usuario_edit', methods=['post'])
def usuario_edit():
    # lendo parametros get(url)
    u = Usuario()
    u.id = request.form.get('id')
    u.email = request.form.get('email')
    u.senha = request.form.get('senha')
    dao = UsuarioDao()
    result = dao.update(u)
    return render_template("usuario_read.html", usuario = u,  msg = result ) 

# ----- Fim Editar

# ----- Criar
@app.route('/usuario/create')
def usuario_create():
    return render_template("usuario_create.html")
# ----- Fim Criar
@app.route('/usuario/salvar', methods=['post'])
def usuario_salvar():
    u = Usuario()
    u.id = request.form.get('id')
    u.email = request.form.get('email')
    u.senha = request.form.get('senha')
    dao = UsuarioDao()
    result = dao.create(u)
    return render_template("usuario_create.html", msg = result)
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

#-----------pessoa juridica
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
#-----------pessoa juridica fim

#------------------------------------------- produtos

# '-'*10 Listar
@app.route('/produto')
def produto():
    msg = request.args.get('msg')
    if not msg:
        msg = ''
    dao = ProdutoDao()
    lista = dao.read()
    return render_template('produto.html', produtos = lista, msg = msg)

# '-'*10 Fim Listar

# '-'*10 Editar
@app.route('/produto/read')
def produto_read():
    id = request.args.get('id')
    dao = ProdutoDao()
    p = dao.read(id)
    return render_template('produto_read.html', produto = p)

@app.route('/produto/edit', methods = ['post'])
def produto_edit():
    p = Produto()
    p.id = request.form.get('id')
    p.nome = request.form.get('nome')
    p.preco = request.form.get('preco')
    p.descricao = request.form.get('descricao')
    dao = ProdutoDao()
    result = dao.update(p)
    return render_template('produto_read.html', produto = p, msg = result)

# '-'*10 Fim Editar

# '-'*10 Criar
@app.route('/produto/create')
def produto_create():
    return render_template('produto_create.html')

@app.route('/produto/salvar', methods = ['post'])
def produto_salvar():
    p = Produto()
    p.id = request.form.get('id')
    p.nome = request.form.get('nome')
    p.preco = request.form.get('preco')
    p.descricao = request.form.get('descricao')
    dao = ProdutoDao()
    result = dao.create(p)
    return render_template('produto_create.html', msg = result)
# '-'*10 Fim Criar

# '-'*10 Deletar
@app.route('/produto/delete')
def produto_delete():
    id = request.args.get('id')
    dao = ProdutoDao()
    result = dao.delete(id)
    return redirect(f'/produto?msg={result}')
# '-'*10 Fim Deletar
#------------------------------------------- produtos fim
    
app.run(debug=True)
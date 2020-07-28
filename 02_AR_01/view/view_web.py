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
from dao.message_dao import MessageDao
from model.message import Message
from model.message_type import MessageType
from dao.message_type_dao import MessageTypeDao


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

@app.route('/usuario/usuario_edit', methods=["post"])
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
    msg_pf = request.args.get('msg_pf')
    if not msg_pf:
        msg_pf = ''
    dao_pf = PessoaFisicaDao()
    lista_pf = dao_pf.read()
    return render_template("pessoa_fisica.html", pessoa_fisica = lista_pf, msg_pf = msg_pf)

@app.route('/pessoa_fisica/read')
def pessoa_fisica_read():
    #lendo parametros get(url)
    id = request.args.get('id')
    dao_pf = PessoaFisicaDao()
    pf = dao_pf.read(id)
    return render_template("pessoa_fisica_read.html", pessoa_fisica = pf)

@app.route('/pessoa_fisica/pessoa_fisica_edit', methods = ["POST"])
def pessoa_fisica_edit():
    #lendo parametros get(url)
    pf = PessoaFisica()
    pf.id = request.form.get('id')
    pf.nome = request.form.get('nome')
    pf.data = request.form.get('data')
    pf.rg = request.form.get('rg')
    pf.cpf = request.form.get('cpf')
    dao_pf = PessoaFisicaDao()
    result_pf = dao_pf.update(pf)
    return render_template("pessoa_fisica_read.html", pessoa_fisica = pf, msg_pf = result_pf)

@app.route('/pessoa_fisica/delete')
def pessoa_fisica_delete():
    #lendo parametros get(url)
    id = request.args.get('id')
    dao_pf = PessoaFisicaDao()
    result_pf = dao_pf.delete(id)
    return redirect(f'/pessoa_fisica?msg_pf={result_pf}')

@app.route('/pessoa_fisica/create')
def pessoa_fisica_create():
    return render_template('pessoa_fisica_create.html')

@app.route('/pessoa_fisica/salvar', methods = ["POST"])
def pessoa_fisica_save():
    pf = PessoaFisica()
    pf.id = request.form.get('id')
    pf.nome = request.form.get('nome')
    pf.data = request.form.get('data')
    pf.rg = request.form.get('rg')
    pf.cpf = request.form.get('cpf')
    dao_pf = PessoaFisicaDao()
    result_pf = dao_pf.create(pf)
    return render_template('pessoa_fisica_create.html', msg_pf = result_pf)

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


@app.route('/pessoa_juridica/pessoa_juridica_edit', methods=["post"])
def pessoa_juridica_edit():
    pjd = PessoaJuridica()
    pjd.id = request.form.get('id')
    pjd.nome = request.form.get('nome')
    pjd.data = request.form.get('data')
    pjd.cnpj = request.form.get('cnpj')
    dao = PessoaJuridicaDao()
    result = dao.update(pjd)
    return render_template('pessoa_juridica_read.html', pessoa_juridica=pjd, msg_pjd = result)
# ----- Fim Editar

# ----- Criar
@app.route('/pessoa_juridica/create')
def pessoa_juridica_create():
    return render_template('pessoa_juridica_create.html')

# ----- Fim Criar
@app.route('/pessoa_juridica/salvar', methods =["post"])
def pessoa_juridica_salvar():
    pjd = PessoaJuridica()
    pjd.id = request.form.get('id')
    pjd.nome = request.form.get('nome')
    pjd.data = request.form.get('data')
    pjd.cnpj = request.form.get('cnpj')
    dao = PessoaJuridicaDao()
    result = dao.create(pjd)
    return render_template('pessoa_juridica_create.html', msg_pjd = result)

# ----- Deletar 
@app.route('/pessoa_juridica/delete')
def pessoa_juridica_delete():
    # lendo parametros get(url)
    id = request.args.get('id')
    dao = PessoaJuridicaDao()
    result = dao.delete(id)
    return redirect(f'/pessoa_juridica?msg={result}')

#------------------------------------------- pessoa juridica fim

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
    
#------------------------------------------- Message
#----------------Listar

@app.route('/message')
def message():
    msg = request.args.get('msg')
    if not msg:
        msg = ''
    dao = MessageDao()
    lista_message = dao.read()
    return render_template('message.html', message=lista_message, msg=msg)

#----------------Editar
@app.route('/message/read')
def message_read():
    id = request.args.get('id')
    dao = MessageDao()
    msg = dao.read(id)
    return render_template('message_read.html', message=msg)

@app.route('/message/message_edit', methods=['POST'])
def message_edit():
    msg_class = Message()
    msg_class.id = request.form.get('id')
    msg_class.code = request.form.get('code')
    msg_class.text_message = request.form.get('text_message')
    msg_class.message_type = request.form.get('message_type')
    dao = MessageDao()
    result = dao.update(msg_class)
    return render_template('message_read.html', message=msg_class, msg=result)
#------------------Fim Editar

#------------------Criar
@app.route('/message/create')
def message_create():
    return render_template('message_create.html')


@app.route('/message/salvar', methods=['POST'])
def message_salvar():
    msg_class = Message()
    msg_class.id = request.form.get('id')
    msg_class.code = request.form.get('code')
    msg_class.text_message = request.form.get('text_message')
    msg_class.message_type = request.form.get('message_type')
    dao = MessageDao()
    result = dao.create(msg_class)
    return render_template('message_create.html', msg = result)
#------------------Fim criar

#------------------Deletar
@app.route('/message/delete')
def message_delete():
    id = request.args.get('id')
    dao = MessageDao()
    result = dao.delete(id)
    return redirect(f'/message?msg={result}')

#----------- Message Type inicio
@app.route('/message_type')
def message_type():
    msg_mt = request.args.get('msg_mt')
    if not msg_mt:
        msg_mt = ''
    dao_mt = MessageTypeDao()
    lista_mt = dao_mt.read()
    return render_template("message_type.html", message_type = lista_mt, msg_mt = msg_mt)

@app.route('/message_type/read')
def message_type_read():
    #lendo parametros get(url)
    id = request.args.get('id')
    dao_mt = MessageTypeDao()
    mt = dao_mt.read(id)
    return render_template('message_type_read.html', message_type = mt)

@app.route('/message_type/edit', methods = ["POST"])
def message_type_edit():
    #lendo parametros get(url)
    mt = MessageType()
    mt.id = request.form.get('id')
    mt.name = request.form.get('name')
    mt.description = request.form.get('description')
    dao_mt = MessageTypeDao()
    result_mt = dao_mt.update(mt)
    return render_template("message_type_read.html", message_type = mt, msg_mt = result_mt)

@app.route('/message_type/delete')
def message_type_delete():
    #lendo parametros get(url)
    id = request.args.get('id')
    dao_mt = MessageTypeDao()
    result_mt = dao_mt.delete(id)
    return redirect(f'/message_type?msg_mt={result_mt}')

@app.route('/message_type/create')
def message_type_create():
    return render_template('message_type_create.html')

@app.route('/message_type/salvar', methods = ["POST"])
def message_type_save():
    mt = MessageType()
    mt.id = request.form.get('id')
    mt.name = request.form.get('name')
    mt.description = request.form.get('description')
    dao_mt = MessageTypeDao()
    result_mt = dao_mt.create(mt)
    return render_template("message_type_create.html", msg_mt = result_mt)
  
app.run(debug=True)
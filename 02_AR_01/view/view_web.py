import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from flask import Flask, render_template, request, redirect, url_for, session
import json

from model.user import User
from model.produto import Produto
from dao.user_dao import UserDao
from model.pessoa_fisica import PessoaFisica
from dao.pessoa_fisica_dao import PessoaFisicaDao
from dao.produto_dao import ProdutoDao
from dao.legal_person_dao import LegalPersonDao
from model.legal_person import LegalPerson
from dao.message_dao import MessageDao
from model.message import Message
from model.message_type import MessageType
from dao.message_type_dao import MessageTypeDao


# -- criação de um objeto flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'CALYPSO'

def session_msg():
    if 'msg' in session:
        msg = Message.from_json(json.loads(session['msg']))
        session.pop('msg', None)
    else:
        msg = ''
    return msg

@app.route('/')
def inicio():
    return render_template('index.html')

#------------------------------------------- usuarios
def make_user_from_form():
    user = User()
    user.id = request.form.get('id')
    user.email = request.form.get('email')
    user.password = request.form.get('password')
    return user

# ----- Listar
@app.route('/user')
def user():
    dao = UserDao()
    users = dao.read()
    return render_template("users/users.html", users = users, msg = session_msg())

# ----- Editar
@app.route('/user/read')
def user_read():
    # lendo parametros get(url)
    id = request.args.get('id')
    dao = UserDao()
    user = dao.read(id)
    return render_template("users/user_read.html", user = user) 

@app.route('/user/edit', methods=["post"])
def user_edit():
    # lendo parametros get(url)
    user = make_user_from_form()
    dao = UserDao()
    result = dao.update(user)
    return render_template("users/user_read.html", user = user, msg = result)

# ----- Criar
@app.route('/user/create')
def user_create():
    return render_template("users/user_create.html")

@app.route('/user/save', methods=['post'])
def user_save():
    user = make_user_from_form()
    dao = UserDao()
    result = dao.create(user)
    return render_template("users/user_create.html", msg = result)
# ----- Deletar 
@app.route('/user/delete')
def user_delete():
    # lendo parametros get(url)
    id = request.args.get('id')
    dao = UserDao()
    result = dao.delete(id)
    session['msg'] = json.dumps(result.__dict__)
    return redirect(url_for('user'))
#------------------------------------------- usuarios fim

@app.route('/pessoa_fisica')
def pessoa_fisica():
    dao_pf = PessoaFisicaDao()
    lista_pf = dao_pf.read()
    return render_template("person/pessoa_fisica.html", pessoa_fisica = lista_pf, msg = session_msg())

@app.route('/pessoa_fisica/read')
def pessoa_fisica_read():
    #lendo parametros get(url)
    id = request.args.get('id')
    dao_pf = PessoaFisicaDao()
    pf = dao_pf.read(id)
    return render_template("person/pessoa_fisica_read.html", pessoa_fisica = pf)

@app.route('/pessoa_fisica/pessoa_fisica_edit', methods = ["POST"])
def pessoa_fisica_edit():
    #lendo parametros get(url)
    pf = PessoaFisica()
    pf.id = request.form.get('id')
    pf.name = request.form.get('name')
    pf.date = request.form.get('date')
    pf.rg = request.form.get('rg')
    pf.cpf = request.form.get('cpf')
    dao_pf = PessoaFisicaDao()
    result_pf = dao_pf.update(pf)
    return render_template("person/pessoa_fisica_read.html", pessoa_fisica = pf, msg = result_pf)

@app.route('/pessoa_fisica/delete')
def pessoa_fisica_delete():
    #lendo parametros get(url)
    id = request.args.get('id')
    dao_pf = PessoaFisicaDao()
    result = dao_pf.delete(id)
    session['msg'] = json.dumps(result.__dict__)
    return redirect(url_for('pessoa_fisica'))

@app.route('/pessoa_fisica/create')
def pessoa_fisica_create():
    return render_template('person/pessoa_fisica_create.html')

@app.route('/pessoa_fisica/salvar', methods = ["POST"])
def pessoa_fisica_save():
    pf = PessoaFisica()
    pf.id = request.form.get('id')
    pf.name = request.form.get('name')
    pf.date = request.form.get('date')
    pf.rg = request.form.get('rg')
    pf.cpf = request.form.get('cpf')
    dao_pf = PessoaFisicaDao()
    result_pf = dao_pf.create(pf)
    return render_template('person/pessoa_fisica_create.html', msg = result_pf)

#----------- pessoa física fim

#------------------------------------------- legal person
# ----- List
@app.route('/legal_person')
def legal_person():
    dao = LegalPersonDao()
    legal_person_list = dao.read()
    return render_template('legal_person/legal_person.html', legal_persons=legal_person_list, msg=session_msg())

# ----- Edit
@app.route('/legal_person/read')
def legal_person_read():
    # reading parameters get(url)
    id = request.args.get('id')
    dao = LegalPersonDao()
    pjd = dao.read(id)
    return render_template("legal_person/legal_person_read.html", legal_person = pjd ) 


@app.route('/legal_person/legal_person_edit', methods=["POST"])
def legal_person_edit():
    pjd = LegalPerson()
    pjd.id = request.form.get('id')
    pjd.name = request.form.get('name')
    pjd.date = request.form.get('date')
    pjd.cnpj = request.form.get('cnpj')
    dao = LegalPersonDao()
    result = dao.update(pjd)
    return render_template('legal_person/legal_person_read.html', legal_person=pjd, msg = result)
# ----- End Edit

# ----- Create
@app.route('/legal_person/create')
def legal_person_create():
    return render_template('legal_person/legal_person_create.html')

# ----- End Create
@app.route('/legal_person/save', methods =["POST"])
def legal_person_save():
    pjd = LegalPerson()
    pjd.id = request.form.get('id')
    pjd.name = request.form.get('name')
    pjd.date = request.form.get('date')
    pjd.cnpj = request.form.get('cnpj')
    dao = LegalPersonDao()
    result = dao.create(pjd)
    return render_template('legal_person/legal_person_create.html', msg = result)

# ----- Delete 
@app.route('/legal_person/delete')
def legal_person_delete():
    # lendo parametros get(url)
    id = request.args.get('id')
    dao = LegalPersonDao()
    result = dao.delete(id)
    session['msg'] = json.dumps(result.__dict__)
    return redirect( url_for('legal_person'))

#------------------------------------------- End Legal person

#------------------------------------------- produtos

# '-'*10 Listar
@app.route('/produto')
def produto():
    dao = ProdutoDao()
    lista = dao.read()
    return render_template(
        'products/produto.html', produtos = lista, msg = session_msg()
    )

# '-'*10 Fim Listar

# '-'*10 Editar
@app.route('/produto/read')
def produto_read():
    id = request.args.get('id')
    dao = ProdutoDao()
    p = dao.read(id)
    return render_template('products/produto_read.html', produto = p)

@app.route('/produto/edit', methods = ['post'])
def produto_edit():
    p = Produto()
    p.id = request.form.get('id')
    p.nome = request.form.get('nome')
    p.preco = request.form.get('preco')
    p.descricao = request.form.get('descricao')
    dao = ProdutoDao()
    result = dao.update(p)
    return render_template('products/produto_read.html', produto = p, msg = result)

# '-'*10 Fim Editar

# '-'*10 Criar
@app.route('/produto/create')
def produto_create():
    return render_template('products/produto_create.html')

@app.route('/produto/salvar', methods = ['post'])
def produto_salvar():
    p = Produto()
    p.id = request.form.get('id')
    p.nome = request.form.get('nome')
    p.preco = request.form.get('preco')
    p.descricao = request.form.get('descricao')
    dao = ProdutoDao()
    result = dao.create(p)
    return render_template('products/produto_create.html', msg = result)
# '-'*10 Fim Criar

# '-'*10 Deletar
@app.route('/produto/delete')
def produto_delete():
    id = request.args.get('id')
    dao = ProdutoDao()
    result = dao.delete(id)
    session['msg'] = json.dumps(result.__dict__)
    return redirect(url_for('produto'))
# '-'*10 Fim Deletar
#------------------------------------------- produtos fim
    
#------------------------------------------- Message
#----------------Listar

@app.route('/message')
def message():
    dao = MessageDao()
    lista_message = dao.read()
    return render_template('messages/message.html', message=lista_message, msg = session_msg())

#----------------Editar
@app.route('/message/read')
def message_read():
    id = request.args.get('id')
    dao = MessageDao()
    msg = dao.read(id)
    return render_template('messages/message_read.html', message=msg)

@app.route('/message/message_edit', methods=['POST'])
def message_edit():
    msg_class = Message()
    msg_class.id = request.form.get('id')
    msg_class.code = request.form.get('code')
    msg_class.text_message = request.form.get('text_message')
    msg_class.message_type = request.form.get('message_type')
    dao = MessageDao()
    result = dao.update(msg_class)
    return render_template('messages/message_read.html', message=msg_class, msg=result)
#------------------Fim Editar

#------------------Criar
@app.route('/message/create')
def message_create():
    return render_template('messages/message_create.html')


@app.route('/message/salvar', methods=['POST'])
def message_salvar():
    msg_class = Message()
    msg_class.id = request.form.get('id')
    msg_class.code = request.form.get('code')
    msg_class.text_message = request.form.get('text_message')
    msg_class.message_type = request.form.get('message_type')
    dao = MessageDao()
    result = dao.create(msg_class)
    return render_template('messages/message_create.html', msg = result)
#------------------Fim criar

#------------------Deletar
@app.route('/message/delete')
def message_delete():
    id = request.args.get('id')
    dao = MessageDao()
    result = dao.delete(id)
    session['msg'] = json.dumps(result.__dict__)
    return redirect( url_for('message'))

#----------- Message Type inicio
@app.route('/message_type')
def message_type():
    dao_mt = MessageTypeDao()
    lista_mt = dao_mt.read()
    return render_template("msg_type/message_type.html", message_type = lista_mt, msg = session_msg())

@app.route('/message_type/read')
def message_type_read():
    #lendo parametros get(url)
    id = request.args.get('id')
    dao_mt = MessageTypeDao()
    mt = dao_mt.read(id)
    return render_template('msg_type/message_type_read.html', message_type = mt)

@app.route('/message_type/edit', methods = ["POST"])
def message_type_edit():
    #lendo parametros get(url)
    mt = MessageType()
    mt.id = request.form.get('id')
    mt.name = request.form.get('name')
    mt.description = request.form.get('description')
    dao_mt = MessageTypeDao()
    result_mt = dao_mt.update(mt)
    return render_template("msg_type/message_type_read.html", message_type = mt, msg = result_mt)

@app.route('/message_type/delete')
def message_type_delete():
    #lendo parametros get(url)
    id = request.args.get('id')
    dao_mt = MessageTypeDao()
    result = dao_mt.delete(id)
    session['msg'] = json.dumps(result.__dict__)
    return redirect( url_for('msg_type/message_type')  )

@app.route('/message_type/create')
def message_type_create():
    return render_template('msg_type/message_type_create.html')

@app.route('/message_type/salvar', methods = ["POST"])
def message_type_save():
    mt = MessageType()
    mt.id = request.form.get('id')
    mt.name = request.form.get('name')
    mt.description = request.form.get('description')
    dao_mt = MessageTypeDao()
    result_mt = dao_mt.create(mt)
    return render_template("msg_type/message_type_create.html", msg = result_mt)

app.run(debug=True)
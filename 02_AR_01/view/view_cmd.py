import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from model.pessoa_fisica import PessoaFisica
from model.pessoa_juridica import PessoaJuridica
from model.user import User
from model.produto import Produto
from model.message import Message
from model.message_type import MessageType

from dao.pessoa_fisica_dao import PessoaFisicaDao
from dao.pessoa_juridica_dao import PessoaJuridicaDao
from dao.user_dao import UserDao
from dao.produto_dao import ProdutoDao
from dao.message_dao import MessageDao

# print(pfd.update('paulo', pf))
# pj = PessoaJuridica(1, 'matheus', '22-11-2001', '2222222222')
#pj = PessoaJuridica('paulo', '05/05/2005', '08471017970', '2')
u = User('mdg@olist.com','444444',1)

from dao.message_type_dao import MessageTypeDao

# print(pfd.update('paulo', pf))
# pj = PessoaJuridica(1, 'matheus', '22-11-2001', '2222222222')
#u = User('mdg@olist.com','444444',1)


#p = Produto('mouse', 10.0, 'mouse do chines ', 2)

m = Message('404', 'not found', 'not found', 1)

#teste p/ pessoa fisica

# pf = PessoaFisica(1,'maykon','05-11-86','44444444','55555555555')
# pfd = PessoaFisicaDao()

#pf = PessoaFisica(1,'maykon','05-11-86','44444444','55555555555')
#pfd = PessoaFisicaDao()

#print(pfd.create(pf))
#print(pfd.read_by_id())
#print(pfd.delete(pf))

m = MessageType('teste','testestestesteste',1)
md = MessageTypeDao()
#print(md.create(m))
print(md.read(1))
#print(md.update(m))
#print(md.delete(m))

# pfd = PessoaFisicaDao()
#pjd = PessoaJuridicaDao()
# ud = UserDao()
# pd = ProdutoDao()
# mg = MessageDao()
# print(mg.create(m))
# pjd = PessoaJuridicaDao(PessoaJuridica)  ---> ????
#ud = UserDao()
#pd = ProdutoDao()

#print(pd.create(p))
#print(pd.delete(2))
#print(pd.read())
#print(pd.read_by_id('1'))
#pd.update(p)
#print(pd.read())
# print(mg.read(1))

# print(pd.create(p))
# print(pd.read_by_id('1'))
 
#print(pjd.create(pj))
#pd.read_all()

#print(pd.create(p))
#print(pd.read_by_id('1'))
# print(ud.read())
#print(ud.read())
#print(pjd.create(pj))


#print(pfd.create(pf))
#print(pfd.delete(pf))





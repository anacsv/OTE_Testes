import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from model.pessoa_fisica import PessoaFisica
from model.pessoa_juridica import PessoaJuridica
from model.usuario import Usuario
from model.produto import Produto
from model.message import Message

from dao.pessoa_fisica_dao import PessoaFisicaDao
from dao.pessoa_juridica_dao import PessoaJuridicaDao
from dao.usuario_dao import UsuarioDao
from dao.produto_dao import ProdutoDao
from dao.message_dao import MessageDao

# print(pfd.update('paulo', pf))
# pj = PessoaJuridica(1, 'matheus', '22-11-2001', '2222222222')
u = Usuario('mdg@olist.com','444444',1)

p = Produto('mouse', 10.0, 'mouse do chines ', 2)

m = Message('404', 'not found', '1', 1)

#teste p/ pessoa fisica
pf = PessoaFisica(1,'maykon','05-11-86','44444444','55555555555')
pfd = PessoaFisicaDao()
#print(pfd.create(pf))
#print(pfd.read_by_id())
#print(pfd.delete(pf))

# pfd = PessoaFisicaDao()
# pjd = PessoaJuridicaDao(PessoaJuridica)  ---> ????
# ud = UsuarioDao()
# pd = ProdutoDao()
mg = MessageDao()
print(mg.create())

#print(pd.create(p))
#print(pd.delete(2))
#print(pd.read())
#print(pd.read_by_id('1'))
#pd.update(p)
#print(pd.read())
#print(mg.read())

# print(pd.create(p))
# print(pd.read_by_id('1'))
 
# print(pjd.read_by_id('1'))
#pd.read_all()

#print(pd.create(p))
#print(pd.read_by_id('1'))
# print(ud.read())
#print(pjd.create(pj))


#print(pfd.create(pf))
#print(pfd.delete(pf))



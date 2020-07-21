import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from model.pessoa_fisica import PessoaFisica
from model.pessoa_juridica import PessoaJuridica
from model.usuario import Usuario
from model.produto import Produto

from dao.pessoa_fisica_dao import PessoaFisicaDao
from dao.pessoa_juridica_dao import PessoaJuridicaDao
from dao.usuario_dao import UsuarioDao
from dao.produto_dao import ProdutoDao

pf = PessoaFisica(1,'maykon','05-11-86','44444444','55555555555')
pj = PessoaJuridica(1, 'matheus', '22-11-2001', '2222222222')
u = Usuario('mdg@zuplae.com','123456',10)
p = Produto('mouse', 100.0, 'mouse de plastico', 1)

#teste p/ pessoa fisica
#pfd = PessoaFisicaDao(PessoaFisica)
#print(pfd.create(pf))
#print(pfd.read_by_id('1'))
#print(pfd.delete(pf))

# pfd = PessoaFisicaDao()
# pjd = PessoaJuridicaDao(PessoaJuridica)  ---> ????
# ud = UsuarioDao()
# pd = ProdutoDao()

print(pd.read())
#print(pd.create(p))
#print(pd.read_by_id('1'))


# print(pd.create(p))
# print(pd.read_by_id('1'))
 
# print(pjd.read_by_id('1'))
#pd.read_all()

#print(pd.create(p))
print(pd.read_by_id('1'))
#print(ud.create(u) )
#print(pjd.create(pj))


#print(pfd.create(pf))
#print(pfd.delete(pf))


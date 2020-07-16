import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from model.pessoa_fisica import PessoaFisica
from model.pessoa_juridica import PessoaJuridica
from model.usuario import Usuario

from dao.pessoa_fisica_dao import PessoaFisicaDao
from dao.pessoa_juridica_dao import PessoaJuridicaDao
from dao.usuario_dao import UsuarioDao

pf = PessoaFisica(1,'maykon','05-11-86','44444444','55555555555')
pj = PessoaJuridica(1, 'matheus', '22-11-2001', '2222222222')
u = Usuario('mdg@zuplae.com','123456',10)

pfd = PessoaFisicaDao()
pjd = PessoaJuridicaDao()
ud = UsuarioDao()

print(ud.create(u) )

#print(pfd.create(pf))

# #print(pfd.delete(pf))

# pjd = PessoaJuridicaDao()

# pj = PessoaJuridica(1,'maykon','05-11-86','55555555555')

# print(pjd.delete(pj))

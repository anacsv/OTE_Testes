import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from model.pessoa_fisica import PessoaFisica
from model.pessoa_juridica import PessoaJuridica
from dao.pessoa_fisica_dao import PessoaFisicaDao
from dao.pessoa_juridica_dao import PessoaJuridicaDao

pfd = PessoaFisicaDao()
pjd = PessoaJuridicaDao()

pf = PessoaFisica(1,'maykon','05-11-86','44444444','55555555555')
pj = PessoaJuridica(1, 'matheus', '22-11-2001', '2222222222')

# print(pfd.create(pf))
# print(pfd.read_all())
# print(pfd.read('maykon\n'))

print(pjd.create(pj))
# print(pjd.read_all())
# print(pjd.read('maykon\n'))
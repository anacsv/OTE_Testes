import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from model.pessoa_fisica import PessoaFisica
from dao.pessoa_fisica_dao import PessoaFisicaDao

from model.pessoa_juridica import PessoaJuridica
from dao.pessoa_juridica_dao import PessoaJuridicaDao

pfd = PessoaFisicaDao()

pf = PessoaFisica(1,'maykon','05-11-86','44444444','55555555555')

#print(pfd.create(pf))

#print(pfd.delete(pf))

pjd = PessoaJuridicaDao()

pj = PessoaJuridica(1,'maykon','05-11-86','55555555555')

print(pjd.delete(pj))
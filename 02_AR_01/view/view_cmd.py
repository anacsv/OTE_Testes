import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from model.pessoa_fisica import PessoaFisica
from dao.pessoa_fisica_dao import PessoaFisicaDao

pf = PessoaFisica(1,'maykon','05-11-86','44444444','55555555555')
pfd = PessoaFisicaDao()
#print(pfd.create(pf))


print(pfd.update('paulo', pf))
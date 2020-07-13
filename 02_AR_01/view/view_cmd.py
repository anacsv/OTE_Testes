from model.pessoa_fisica import PessoaFisica
from dao.pessoa_fisica_dao import PessoaFisicaDao

pf = PessoaFisica(1,'maykon','05-11-86','44444444','55555555555')
pfd = PessoaFisicaDao()
print(pfd.create(pf))

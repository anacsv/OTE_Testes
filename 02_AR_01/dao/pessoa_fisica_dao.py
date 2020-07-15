# DAO
# Data Access Object
# Data -> Object | Object -> Data
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from model.pessoa_fisica import PessoaFisica

class PessoaFisicaDao:
    # --- CRUD 
    def create(self, pessoa_fisica:PessoaFisica):
        #---- salvando a pessoa_fisica
        # logica de persistencia da pessoa fisica
        with open('pessoa_fisica.txt','a') as file :
            file.write(pessoa_fisica.nome)
            file.close()
        
        return 'salvo'

    def read(self, id):
         #---- listando uma pessoa_fisica
        return 'lido'

    def read_all(self):
         #---- listando uma lista pessoa_fisica
        return 'listar todos'

    def update(self, name_updated, pessoa_fisica:PessoaFisica):
         #---- alterando a pessoa_fisica
        with open('pessoa_fisica.txt', 'r+') as file:
            for nome in file:
                if nome == pessoa_fisica.nome:
                    file.write(pessoa_fisica.nome)
                    return 'alterado'
                else:
                    return 'This name doesn´t exist!'

    def delete(self):
         #---- deletando a pessoa_fisica
        return 'excluído'
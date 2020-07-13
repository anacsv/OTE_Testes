# DAO
# Data Access Object
# Data -> Object | Object -> Data

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

    def update(self):
         #---- alterando a pessoa_fisica
        return 'alterado'

    def delete(self):
         #---- deletando a pessoa_fisica
        return 'excluído'
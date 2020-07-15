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
            file.write(pessoa_fisica.nome+"\n")
        
        return 'salvo'

    def read(self, id):
         #---- listando uma pessoa_fisica
        with open('pessoa_fisica.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line == id:
                    return line

        return 'nao encontrado'

    def read_all(self):
         #---- listando uma lista pessoa_fisica
        lista = []
        with open('pessoa_fisica.txt', 'r') as file:
            lista = list(file)

        return lista

    def update(self):
         #---- alterando a pessoa_fisica
        return 'alterado'

    def delete(self):
         #---- deletando a pessoa_fisica
        return 'excluído'
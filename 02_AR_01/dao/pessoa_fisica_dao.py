# DAO
# Data Access Object
# Data -> Object | Object -> Data

from model.pessoa_fisica import PessoaFisica
from dao.base_dao import BaseDao

class PessoaFisicaDao(BaseDao):
    # --- CRUD 
    def create(self, model:PessoaFisica):
        #---- salvando a pessoa_fisica
        # logica de persistencia da pessoa fisica        
        super().create(model)
        return 'salvo'

    def read_id(self, id):
         #---- listando uma pessoa_fisica
        return super.read_by_id(id)       

    def read_all(self):
         #---- listando uma lista pessoa_fisica
        lista = []
        with open('pessoa_fisica.txt', 'r') as file:
            lista = list(file)

        return lista

    def update(self):
         #---- alterando a pessoa_fisica
        return 'alterado'

    def delete(self, pessoa_fisica: PessoaFisica):
         #---- deletando a pessoa_fisica
        
        file = open('pessoa_fisica.txt', "r")

        lines = file.readlines()
        file.close()
        
        new_file = open('pessoa_fisica.txt', "w")
        found = False
        for line in lines:
            if not line == pessoa_fisica.nome+'\n':
                new_file.write(line)
            else:    
                 found = True
        
        new_file.close()       
        if not found:
           return 'Item não encontrado.' 
        else:
           return 'Item deletado.'
                
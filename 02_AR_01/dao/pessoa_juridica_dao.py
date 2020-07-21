from model.pessoa_juridica import PessoaJuridica
from dao.base_dao import BaseDao

class PessoaJuridicaDao(BaseDao):
    # --- CRUD 
    def create(self, model:PessoaJuridica):
        #---- salvando a pessoa_juridica
        # logica de persistencia da pessoa juridica
        
        return super().create(model)
        

    def read_by_id(self, id):
         #---- listando uma pessoa_juridica
        
        return super().read_by_id(id)
        

    def read_all(self):
         #---- listando uma lista pessoa_juridica
        lista = []
        with open('pessoa_juridica.txt', 'r') as file:
            lista = list(file)

        return lista

    def update(self):
         #---- alterando a pessoa_juridica
        return 'alterado'

    def delete(self, pessoa_juridica:PessoaJuridica):
         #---- deletando a pessoa_juridica

        file = open('pessoa_juridica.txt', "r")

        lines = file.readlines()
        file.close()
        
        new_file = open('pessoa_juridica.txt', "w")
        found = False
        for line in lines:
            if not line == pessoa_juridica.nome+'\n':
                new_file.write(line)
            else:    
                 found = True
        
        new_file.close()       
        if not found:
           return 'Item não encontrado.' 
        else:
           return 'Item deletado.'

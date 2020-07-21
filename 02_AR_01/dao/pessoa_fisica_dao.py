# DAO
# Data Access Object
# Data -> Object | Object -> Data
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from model.pessoa_fisica import PessoaFisica
from dao.base_dao import BaseDao

class PessoaFisicaDao(BaseDao):
    # --- CRUD 
    def create(self, model:PessoaFisica):
        #---- salvando a pessoa_fisica
        # logica de persistencia da pessoa fisica        
        super().create(model)
        return 'salvo'

    def read_by_id(self, id):
         #---- listando uma pessoa_fisica
        return super.read_by_id(id)       

    def read_all(self):
         #---- listando uma lista pessoa_fisica
        lista = []
        with open('pessoa_fisica.txt', 'r') as file:
            lista = list(file)

        return lista


    def update_m(self, name, pessoa_fisica: PessoaFisica):
         #---- alterando a pessoa_fisica
        with open('pessoa_fisica.txt', 'r+') as file:
            names = file.readlines()
            index = names.index(f'{pessoa_fisica.nome}\n')
            names.remove(f'{pessoa_fisica.nome}\n')
            names.insert(index, f'{name}\n')

            file.seek(0)
            file.truncate()
            file.writelines(names)

        return 'alterado'

    def update(self, name_updated, pessoa_fisica:PessoaFisica):
        #---- alterando a pessoa_fisica
        # enum = 1
        with open('pessoa_fisica.txt', 'r+') as file:
            for nome in file:
                file.readline()
                if nome == pessoa_fisica.nome:
                    file.seek(0, 0)
                    file.write(name_updated)
                    file.truncate()
                    return 'alterado'
                else:
                    return 'This name doesn´t exist!'


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

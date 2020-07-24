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
    def __init__(self):
        super().__init__(PessoaFisica)    
    
    def read(self, id = None):
        result = super().read(id)
        if type(result) == list:
            lista_pf = []
            for item in result:
                pf = self.__obj_converter(item)
                lista_pf.append(pf)
            return lista_pf
        return self.__obj_converter(result)

    def __obj_converter(self, item_str:str) -> PessoaFisica :
        pessoa_fisica = PessoaFisica()
        obj_array = item_str.split(';')
        pessoa_fisica.id = obj_array[0]
        pessoa_fisica.nome = obj_array[1]
        pessoa_fisica.data = obj_array[2]
        pessoa_fisica.rg = obj_array[3]
        pessoa_fisica.cpf = obj_array[4]
        return pessoa_fisica
     





    
"""     def create(self, model:PessoaFisica):
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
           return 'Item deletado.' """

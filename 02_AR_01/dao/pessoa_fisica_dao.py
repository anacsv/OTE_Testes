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
     





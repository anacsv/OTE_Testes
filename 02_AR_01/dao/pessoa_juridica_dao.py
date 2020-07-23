from model.pessoa_juridica import PessoaJuridica
from dao.base_dao import BaseDao

class PessoaJuridicaDao(BaseDao):
    # --- CRUD 

    def __init__(self):
        super().__init__(PessoaJuridica)

    def read(self, id = None, nome=None, data=None, cnpj=None):
        result = super().read(id)
        if type(result) == list:
            lista_pessoa_juridica = []
            for item in result:
                pjd = self.__obj_converter(item)
                lista_pessoa_juridica.append(pjd)
            return lista_pessoa_juridica
        return self.__obj_converter(result)

    def __obj_converter(self, item_str:str) -> PessoaJuridica :
        pessoa_juridica = PessoaJuridica()
        obj_array = item_str.split(';')
        pessoa_juridica.id = obj_array[0]
        pessoa_juridica.nome = obj_array[1]
        pessoa_juridica.data = obj_array[2]
        pessoa_juridica.cnpj = obj_array[3]
        return pessoa_juridica
    

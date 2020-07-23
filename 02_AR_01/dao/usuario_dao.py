
from model.usuario import Usuario
from dao.base_dao import BaseDao

class UsuarioDao(BaseDao):
    def __init__(self):
        super().__init__(Usuario)

    def read(self, id = None):
        result = super().read(id)
        if type(result) == list:
            lista_usuario = []
            for item in result:
                u = self.__obj_converter(item)
                lista_usuario.append(u)
            return lista_usuario
        return self.__obj_converter(result)

    def __obj_converter(self, item_str:str) -> Usuario :
        usuario = Usuario()
        obj_array = item_str.split(';')
        usuario.id = obj_array[0]
        usuario.email = obj_array[1]
        usuario.senha = obj_array[2]
        return usuario
    

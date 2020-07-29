from model.usuario import Usuario
#from dao.base_dao import BaseDao
from dao.base_dao_sql import BaseDao

class UsuarioDao(BaseDao):
    def __init__(self):
        self.__table_name = 'users'
        super().__init__()

    #read
    def read(self, id=None):
        sql_select = ''
        sql_select = f'SELECT id, mail, password FROM {self.__table_name}'
        if id:
            sql_select += f' WHERE id= {id} '

        data = super().read(sql_select)
        return self.__convert_data_object(data)

    #create
    def create(self, model:Usuario)->str:
        sql_insert = f'''INSERT INTO {self.__table_name}
                    VALUES
                    (
                        0
                        ,'{model.email}'
                        ,'{model.senha}'
                    )
                    ;'''
        return super().create(sql_insert)

    #update
    def update(self, model:Usuario)->str:
        sql_update = f'''UPDATE {self.__table_name} 
                    set
                    mail = '{model.email}'
                    ,password = '{model.senha}'
                    where id = {model.id}; '''
        return super().update(sql_update)

    #delete
    def delete(self, id:int)->str:
        sql_delete = f'DELETE FROM {self.__table_name} where id = {id}'
        return super().delete(sql_delete)

    def __convert_data_object(self, data):
        if type(data) == list:
            list_users = []
            for item in data:
                user = self.__obj_converter(item)
                list_users.append(user)
            return list_users
        user = self.__obj_converter(data)
        return user

    def __obj_converter(self, item_tuple:tuple) -> Usuario :
        model = Usuario()
        model.id = item_tuple[0]
        model.email = item_tuple[1]
        model.senha = item_tuple[2]
        return model 

    # def read(self, id = None):
    #     result = super().read(id)
    #     if type(result) == list:
    #         lista_usuario = []
    #         for item in result:
    #             u = self.__obj_converter(item)
    #             lista_usuario.append(u)
    #         return lista_usuario
    #     return self.__obj_converter(result)

    # def __obj_converter(self, item_str:str) -> Usuario :
    #     usuario = Usuario()
    #     obj_array = item_str.split(';')
    #     usuario.id = obj_array[0]
    #     usuario.email = obj_array[1]
    #     usuario.senha = obj_array[2]
    #     return usuario

    

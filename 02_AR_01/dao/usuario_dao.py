from model.usuario import Usuario
#from dao.base_dao import BaseDao
from dao.base_dao_sql import BaseDao

class UsuarioDao(BaseDao):

    def __init__(self):
        self.__table_name = 'users'
        super().__init__()

    #read
    def read(self, id = None):
        sql_select = f'SELECT id, mail, password FROM {self.__table_name}'
        if id:
            sql_select += f' WHERE id= {id} '

        data = super().read(sql_select)
        return self.__convert_data_object(data)

    #create
    def create(self, model:Usuario) -> str:
        sql_insert = f'''INSERT INTO {self.__table_name}
                    VALUES
                    (
                        0
                        ,'{model.email}'
                        ,'{model.password}'
                    )
                    ;'''
        return super().create(sql_insert)

    #update
    def update(self, model:Usuario) -> str:
        sql_update = f'''UPDATE {self.__table_name} 
                    SET
                    mail = '{model.email}'
                    ,password = '{model.password}'
                    WHERE id = {model.id}; '''
        return super().update(sql_update)

    #delete
    def delete(self, id:int)->str:
        sql_delete = f'DELETE FROM {self.__table_name} WHERE id = {id}'
        return super().delete(sql_delete)

    def __convert_data_object(self, data):
        if type(data) == list:
            users = []
            for item in data:
                user = self.__obj_converter(item)
                users.append(user)
            return users
        user = self.__obj_converter(data)
        return user

    def __obj_converter(self, item_tuple:tuple) -> Usuario:
        model = Usuario()
        model.id = item_tuple[0]
        model.email = item_tuple[1]
        model.password = item_tuple[2]
        return model 

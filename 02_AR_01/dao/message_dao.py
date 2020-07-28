from model.message import Message
from dao.base_dao import BaseDao

class MessageDao(BaseDao):

    def __init__(self):
        super().__init__(Message)

    def read(self, id = None):
        result = super().read(id)
        if type(result) == list:
            lista_message = []
            for item in result:
                message = self.__obj_converter(item)
                lista_message.append(message)
            return lista_message
        return self.__obj_converter(result)

    def __obj_converter(self, item_str:str) -> Message:
        message = Message()
        obj_array = item_str.split(';')
        message.id = obj_array[0]
        message.code = obj_array[1]
        message.text_message = obj_array[2]
        message.message_type = obj_array[3]
        return message
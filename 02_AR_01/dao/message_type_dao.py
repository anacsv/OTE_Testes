from model.message import MessageType
from dao.base_dao import BaseDao

class MessageTypeDao(BaseDao):
    def __init__(self):
        super().__init__(MessageType)

    def read(self, id = None):
        result = super().read(id)
        if type(result) == list:
            list_message_type = []
            for item_type in result:
                m = self.__obj_converter_type(item_type)
                list_message_type.append(m)
            return list_message_type
        return self.__obj_converter_type(result)

    def __obj_converter_type(self, item_type_str:str) -> MessageType :
        message_type = MessageType()
        obj_array_type = item_type_str.split(';')
        message_type.id = obj_array_type[0]
        message_type.name = obj_array_type[1]
        message_type.description = obj_array_type[2]
        return message_type    
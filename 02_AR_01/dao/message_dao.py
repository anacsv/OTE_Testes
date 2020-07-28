import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

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
                mg = self.__create_object(item)
                lista_message.append(mg)
            return lista_message
        return self.__create_object(result)

    def __create_object(self, item_str: str) -> Message:
        mgs = Message()
        obj_array = item_str.split(';')
        mgs.id = obj_array[0]
        mgs.code = obj_array[1]
        mgs.text_message = obj_array[2]
        mgs.message_type = obj_array[3]
        return mgs

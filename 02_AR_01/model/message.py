import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from model.base_model import Base

class Message(Base):
    def __init__(self, code:str = '', text_message:str = '', message_type:str = '', id:int = 0):
        self.__code = code
        self.__text_message = text_message
        self.__message_type =  message_type
        super().__init__(id)
        
    @property
    def code(self)->str:
        return self.__code

    @code.setter
    def code(self, code:str):
        self.__code = code
    
    @property
    def text_message(self)->str:
        return self.__text_message

    @text_message.setter
    def text_message(self, text_message:str):
        self.__text_message = text_message
    
    @property
    def message_type(self)->MessageType:
        return self.__message_type

    @message_type.setter
    def message_type(self, message_type:MessageType):
        self.__message_type = message_type

    def message_type(self)->str:
        return self.__message_type

    @message_type.setter
    def message_type(self, message_type:str):
        self.__message_type = message_type

    def __str__(self):
        return f'{self.id};{self.code};{self.text_message};{self.message_type}'

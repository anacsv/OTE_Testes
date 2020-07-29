from model.base_model import Base
from model.message_type import MessageType

class Message(Base):
    def __init__(self, code:str = '', text_message:str = '', 
        message_type:MessageType = None, id:int = 0):
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

    def __str__(self):
        return f'{self.id};{self.code};{self.text_message};{self.message_type}'
    
    @property  
    def __dict__(self):
        return {
            'id': self.id,
            'code':self.code,
            'text_message': self.text_message,
            'message_type': self.message_type.__dict__
        }
    
    @classmethod
    def from_json(cls, data: dict):
        message_type = MessageType.from_json(data["message_type"])
        data["message_type"] = message_type
        return cls(**data)

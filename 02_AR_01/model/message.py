from .base_model import Base
from .message_type import MessageType

class Message(Base):
    def __init__(self, code:str, text_message:str, message_type: MessageType, id = None):
        self.__code = code
        self.__text_message = text_message
        self.__message_type =  message_type
        super().__init__(id)
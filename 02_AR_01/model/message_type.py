from .base_model import Base

class MessageType(Base):
    def __init__(self, name, description ,id=None):
        self.__name = name
        self.__description = description
        super().__init__(id)

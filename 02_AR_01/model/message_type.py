from .base_model import Base

class MessageType(Base):
    def __init__(self, name:str='', description:str='' ,id=None):
        self.__name = name
        self.__description = description
        super().__init__(id)

    @property
    def name(self)->str:
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def description(self)->str:
        return self.__description

    @description.setter
    def description(self, description:str):
        self.__description = description

    def __str__(self):
        # interpolação de strings
        return f'{self.id};{self.name};{self.description}'
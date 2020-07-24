from .base_model import Base

class Pessoa(Base):

    def __init__(self, nome:str = '', data:str = '', id:int = 0 ):
        self.__nome = nome
        self.__data = data
        super().__init__(id)

    @property
    def nome(self)->str:
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    @property
    def data(self)->str:
        return self.__data

    @data.setter
    def data(self, data:str):
        self.__data = data


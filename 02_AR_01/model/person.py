from .base_model import Base

class Person(Base):

    def __init__(self, name:str = '', date:str = '', id:int = 0 ):
        self.__name = name
        self.__date = date
        super().__init__(id)

    @property
    def name(self)->str:
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def date(self)->str:
        return self.__date

    @date.setter
    def date(self, date:str):
        self.__date = date


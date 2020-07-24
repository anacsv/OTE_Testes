from .base_model import Base

class Produto(Base):

    def __init__(self, nome: str = '', preco: float = 0.0,
                descricao: str = '', id:int = 0):
        self.__nome = nome
        self.__preco = preco
        self.__descricao = descricao
        super().__init__(id)

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco: float) -> None:
        self.__preco = preco

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self.__descricao = descricao

    def __str__(self):
        return f'{self.__id};{self.__nome};{self.__preco};{self.__descricao}'

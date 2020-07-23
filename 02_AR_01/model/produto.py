class Produto:

    def __init__(self, nome = '', preco = 0.0, descricao = '', id = None):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def __str__(self):
        return f'{self.__id};{self.__nome};{self.__preco};{self.__descricao}'
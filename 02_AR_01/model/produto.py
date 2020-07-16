class Produto:

    def __init__(self, nome, preco, descricao, id = None):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__descricao = descricao
    
    def __str__(self):
        return f'{self.__id};{self.__nome};{self.__preco};{self.__descricao}'
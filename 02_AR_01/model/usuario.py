
class Usuario:
    def __init__(self, email, senha, id=None):
        self.__id = id
        self.__email = email
        self.__senha = senha

    def __str__(self):
        # interpolação de strings
        return f'{self.__id};{self.__email};{self.__senha}'
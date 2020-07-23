
class Usuario:
    def __init__(self, email="", senha="", id=None):
        self.__id = id
        self.__email = email
        self.__senha = senha

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    def __str__(self):
        # interpolação de strings
        return f'{self.__id};{self.__email};{self.__senha}'
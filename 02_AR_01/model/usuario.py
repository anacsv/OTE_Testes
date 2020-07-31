class Usuario:
    def __init__(self, email = "", password = "", id = None):
        self.__id = id
        self.__email = email
        self.__password = password

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
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        # interpolação de strings
        return f'{self.__id};{self.__email};{self.__password}'

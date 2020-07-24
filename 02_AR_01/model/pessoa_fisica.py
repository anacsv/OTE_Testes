from .pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome='', data, rg='', cpf='', id=None):
        self.__id = id
        self.__nome = nome
        self.__data = data
        self.__rg = rg
        self.__cpf = cpf

#inicio id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

#inicio Nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

#inicio Data
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

#inicio RG
    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg

#inicio CPF
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def __str__(self):
        # interpolação de strings
        return f'{self.id};{self.nome};{self.data};{self.rg};{self.cpf}'
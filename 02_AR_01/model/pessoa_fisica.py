from .pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome:str = "", data:str = "", rg:str = "", cpf:str = "", id:int = 0):
        self.__rg = rg
        self.__cpf = cpf
        super().__init__(nome, data, id)

#inicio id
"""    
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
"""
#inicio RG
    @property
    def rg(self)->str:
        return self.__rg

    @rg.setter
    def rg(self, rg:str):
        self.__rg = rg

#inicio CPF
    @property
    def cpf(self)->str:
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf:str):
        self.__cpf = cpf

#interpolação de strings
    def __str__(self):
        return f'{self.id};{self.nome};{self.data};{self.rg};{self.cpf}'
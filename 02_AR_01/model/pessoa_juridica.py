from .pessoa import Pessoa

class PessoaJuridica(): 
    def __init__(self, nome='', data='', cnpj='', id=None):
        self.__nome = nome
        self.__data = data
        self.__cnpj = cnpj
        self.__id = id
    
    #------__id
    @property 
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id 
    
    #-------__nome
    @property 
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    #--------__data
    @property 
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
    
    #--------__cnpj
    @property 
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj    

    #-----------interpolação de strings
    def __str__(self):
        return f'{self.__id};{self.__nome};{self.__data};{self.__cnpj}'
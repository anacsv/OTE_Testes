from .pessoa import Pessoa

class PessoaJuridica(): 
    def __init__(self, nome="", data="", cnpj="", id=None):
        self.id = id
        self.nome = nome
        self.data = data
        self.cnpj = cnpj
    
    #------id
    @property 
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.id = id 
    
    #-------nome
    @property 
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome
    
    #--------data
    @property 
    def data(self):
        return self.data

    @data.setter
    def data(self, data):
        self.data = data
    
    #--------cnpj
    @property 
    def cnpj(self):
        return self.cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.cnpj = cnpj    

    #-----------interpolação de strings
    def __str__(self):
        return f'{self.id};{self.nome};{self.data};{self.cnpj}'
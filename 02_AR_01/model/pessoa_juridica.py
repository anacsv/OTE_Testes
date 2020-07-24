from .pessoa import Pessoa

class PessoaJuridica(Pessoa): 
    def __init__(self, nome:str = '', data:str = '', cnpj:str = '', id:int = 0):
        self.__cnpj = cnpj
        super().__init__(nome, data, id)
       
    #--------__cnpj
    @property 
    def cnpj(self)->str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj:str):
        self.__cnpj = cnpj    

    #-----------interpolação de strings
    def __str__(self):
        return f'{self.__id};{self.__nome};{self.__data};{self.__cnpj}'
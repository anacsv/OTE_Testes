from .person import Person

class PessoaFisica(Person):
    def __init__(self, name:str = "", date:str = "", rg:str = "", cpf:str = "", id:int = 0):
        self.__rg = rg
        self.__cpf = cpf
        super().__init__(name, date, id)

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
        return f'{self.id};{self.name};{self.date};{self.rg};{self.cpf}'
from .person import Person

class LegalPerson(Person): 
    def __init__(self, name:str = '', date:str = '', cnpj:str = '', id:int = 0):
        self.__cnpj = cnpj
        super().__init__(name, date, id)
       
    #--------__cnpj
    @property 
    def cnpj(self)->str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj:str):
        self.__cnpj = cnpj    

    #-----------interpolação de strings
    def __str__(self):
        return f'{self.id};{self.name};{self.date};{self.cnpj}'
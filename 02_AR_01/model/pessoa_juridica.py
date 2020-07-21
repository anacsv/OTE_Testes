from .pessoa import Pessoa

class PessoaJuridica(Pessoa): 
    def __init__(self, id, nome, data, cnpj):
        super().__init__(id, nome, data)
        self.cnpj = cnpj

    @property 
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj    

    def __str__(self):
        # interpolação de strings
        return f'{self.id};{self.nome};{self.data};{self.cnpj}'
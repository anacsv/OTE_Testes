from .pessoa import Pessoa

class PessoaFisica(Pessoa):

    def __init__(self, id, nome, data, rg, cpf):
        super().__init__(id, nome, data)
        self.__rg = rg
        self.__cpf = cpf

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def __str__(self):
        # interpolação de strings
        return f'{self.id};{self.nome};{self.data};{self.rg};{self.cpf}'
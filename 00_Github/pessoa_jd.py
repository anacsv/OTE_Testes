class PessoaJuridica(): 
    def __init__(self, id, nome, data, cnpj):
        super().__init__(id, nome, data)
        self.cnpj = cnpj

    @property 
    def CNPJ(self):
        return self.__cnpj

    @cnpj.setter
    def CNPJ(self, cnpj):
        self.__cnpj = cnpj    


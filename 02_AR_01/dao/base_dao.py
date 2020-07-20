
class BaseDao:  
    def __init__(self, classe):
        self.__caminho_arquivo = f'02_AR_01/dao/db/{classe.__name__}.txt'

    # --- CRUD
    def create(self, model):
        # logica de persistencia de um model generico
        # criando o nome do arquivo de forma generica
        with open(self.__caminho_arquivo,'a') as file :
            file.write(str(model)+"\n")        
        return 'salvo'

    def read_by_id(self, id):

        with open(self.__caminho_arquivo, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line == id:
                    return line

        return 'nao encontrado'

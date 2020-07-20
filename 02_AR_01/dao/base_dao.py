
class BaseDao:  
    def __init__(self):
        self.__caminho_arquivo = '02_AR_01/dao/db/'

    # --- CRUD 
    def create(self, model):
        # logica de persistencia de um model generico
        # criando o nome do arquivo de forma generica
        
        nome_arquivo = f'{type(model).__name__}.txt' 
        with open(caminho_pasta+nome_arquivo,'a') as file :
            file.write(str(model)+"\n")        
        return 'salvo'

    def read_by_id(self, id):
        
        with open('pessoa_fisica.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line == id:
                    return line

        return 'nao encontrado'


class BaseDao:  
    def __init__(self, classe):
        self.__caminho_arquivo = f'02_AR_01/dao/db/{classe.__name__}.txt'

    # --- CRUD ----------------------
    #create
    def create(self, model):
        with open(self.__caminho_arquivo,'a') as file :
            file.write(str(model)+"\n")        
        return 'salvo'

    #read_all
    def read_by_id(self, id=None):
        with open(self.__caminho_arquivo, 'r') as file:
            formated = []
            lines = file.readlines()
            for line in lines:
                if line.split(';')[0] == id:
                    return line.strip()
                formated.append(line.strip())
            return formated
        return 'nao encontrado'
        
    #update
    def update(self, model):
        pass

    #delete
    def delete(self, id):
        pass
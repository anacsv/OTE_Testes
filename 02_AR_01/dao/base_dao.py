
class BaseDao:  
    def __init__(self, classe):
        self.__caminho_arquivo = f'02_AR_01/dao/db/{classe.__name__}.txt'

    # --- CRUD ----------------------
    #create
    def create(self, model):
        with open(self.__caminho_arquivo,'a') as file :
            file.write(str(model)+"\n")        
        return 'salvo'

    #read_by_id
    def read(self, id=None):
        with open(self.__caminho_arquivo, 'r') as file:
            lines = file.readlines()
            formated = []
            for line in lines:
                if id != None:
                    if line.split(';')[0] == id:
                        return line.strip()
                else:
                    formated.append(line.strip())
                    return formated

    #read_all
    def read_all(self):
        with open(self.__caminho_arquivo, 'r') as file:
            lines = file.readlines()
            formated = []
            for line in lines:
                formated.append(line.strip())
            return formated
        

    #update
    def update(self, model):
        pass

    #delete
    def delete(self, id):
        pass
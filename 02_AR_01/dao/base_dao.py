
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
    def __read_by_id(self, id, lines):
        for line in lines:
            if line.split(';')[0] == id:
                return line.strip()
        return 'nao encontrado'

    #read_all
    def __read_all(self, lines) -> list:
        formated = []
        for line in lines:
            formated.append(line.strip())
        return formated

    #read
    def read(self, id = None):
        with open(self.__caminho_arquivo, 'r') as file:
            lines = file.readlines()
            if id:
                return self.__read_by_id(id, lines)
            return self.__read_all(lines)

    #update
    def update(self, model):
        pass

    #delete
    def delete(self, id):
        pass
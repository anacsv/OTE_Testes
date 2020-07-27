
class BaseDao:  
    def __init__(self, classe):
        self.__caminho_arquivo = f'02_AR_01/dao/db/{classe.__name__}.txt'

    # --- CRUD ----------------------
    #create
    def create(self, model):
        fields_missing = self.__validate_fields(model)
        if fields_missing:
            return fields_missing
        with open(self.__caminho_arquivo, 'a') as file:
            file.write(str(model)+"\n")        
        return 'salvo'

    #read_by_id
    def __read_by_id(self, id, lines):
        index = self.__find_by_id(id, lines)
        if index >= 0:
            item = lines[index]
            return item.strip()
        return 'nao encontrado'
    
    #-- busca um elemento pelo id e retorna o elemento ou uma lista
    def __find_by_id(self, id, lines, model=None):
        for line in lines:
            line_id = line.split(';')[0]
            if line_id == str(id):
                index = lines.index(line)
                return index

    #read_all
    def __read_all(self, lines) -> list:
        formated = []
        for line in lines:
            formated.append(line.strip())
        return formated

    #read
    def read(self, id = None):
        lines = self.__read_file()
        if id:
            return self.__read_by_id(id, lines)
        return self.__read_all(lines)

    #update
    def update(self, model):
        lines = self.__read_file()
        if lines:
            index = self.__find_by_id(model.id, lines, model)
            lines.pop(index)
            line = str(model)+"\n"
            lines.insert(index, line)
            self.__rewrite_file(lines)
            return "alterado com sucesso"
        return 'documento vazio'

    #delete
    def delete(self, id):
        lines = self.__read_file()
        if lines:
            index = self.__find_by_id(id, lines)
            lines.pop(index)
            self.__rewrite_file(lines)
            return "deletado com sucesso"
        return 'documento vazio'

    def __rewrite_file(self,lines):
        with open(self.__caminho_arquivo, 'w') as file:
            file.writelines(lines)

    def __read_file(self):
        with open(self.__caminho_arquivo, 'r') as file:
            lines = file.readlines()
            return lines

    def __to_dict(self, model) -> dict:
        model_dict = dict((name, getattr(model, name)) 
            for name in dir(model) if not name.startswith('_'))
        return model_dict

    def __validate_fields(self, model) -> list:
        model_dict = self.__to_dict(model)
        fields_empty = []
        for key, value in model_dict.items():
            if not value:
                fields_empty.append(key)

        return fields_empty

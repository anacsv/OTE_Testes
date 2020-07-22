
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
        item = self.__find_by_id(id, lines)
        if item:
            return item
        return 'nao encontrado'

    def __find_by_id(self, id, lines, model=None):
        for line in lines:
            line_id = line.split(';')[0]
            if line_id == str(id):
                if model:
                    index = lines.index(line)
                    lines.remove(line)
                    line = str(model)+"\n"
                    lines.insert(index, line)
                    return lines
            return line.strip()

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
        lines = self.__find_by_id(model.id, lines, model)
        if lines:
            with open(self.__caminho_arquivo,'w') as file :
                file.writelines(lines)
                return "alterado com sucesso"
        return 'documento vazio'

    # def update_m(self, pessoa_fisica: PessoaFisica):
    #     with open('pessoa_fisica.txt', 'r+') as file:
    #         names = file.readlines()
    #         index = names.index(f'{pessoa_fisica.nome}\n')
    #         names.remove(f'{pessoa_fisica.nome}\n')
    #         names.insert(index, f'{name}\n')

    #         file.seek(0)
    #         file.truncate()
    #         file.writelines(names)

    #     return 'alterado'

    # def update(self, pessoa_fisica:PessoaFisica):
    #     with open('pessoa_fisica.txt', 'r+') as file:
    #         file.readline()
    #         for nome in file:
    #             if nome == pessoa_fisica.nome:
    #                 file.seek(0, 0)
    #                 file.write(name_updated)
    #                 file.truncate()
    #                 return 'alterado'
    #             else:
    #                 return 'This name doesn´t exist!'

    #delete
    def delete(self, id):
        pass

    def __read_file(self):
        with open(self.__caminho_arquivo, 'r') as file:
            lines = file.readlines()
            return lines

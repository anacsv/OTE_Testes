
class BaseDao:  

    # --- CRUD 
    def create(self, model):
        # logica de persistencia de um model generico
        # criando o nome do arquivo de forma generica
        nome_arquivo = f'{type(model).__name__}.txt' 
        with open(nome_arquivo,'a') as file :
            file.write(str(model)+"\n")        
        return 'salvo'

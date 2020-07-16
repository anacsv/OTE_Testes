from model.pessoa_juridica import PessoaJuridica

class PessoaJuridicaDao:
    # --- CRUD 
    def create(self, pessoa_juridica:PessoaJuridica):
        #---- salvando a pessoa_juridica
        # logica de persistencia da pessoa juridica
        return 'salvo'

    def read(self, id):
         #---- listando uma pessoa_juridica
        return 'lido'

    def read_all(self):
         #---- listando uma lista pessoa_juridica
        return 'listar todos'

    def update(self):
         #---- alterando a pessoa_juridica
        return 'alterado'

    def delete(self, pessoa_juridica:PessoaJuridica):
         #---- deletando a pessoa_juridica
        file = open('pessoa_juridica.txt', "r")

        lines = file.readlines()
        file.close()
        
        new_file = open('pessoa_juridica.txt', "w")
        found = False
        for line in lines:
            if not line == pessoa_juridica.nome+'\n':
                new_file.write(line)
            else:    
                 found = True
        
        new_file.close()       
        if not found:
           return 'Item não encontrado.' 
        else:
           return 'Item deletado.'
from model.pessoa_juridica import PessoaJuridica

class PessoaJuridicaDao:
    # --- CRUD 
    def create(self, pessoa_juridica:PessoaJuridica):
        #---- salvando a pessoa_juridica
        # logica de persistencia da pessoa juridica
        with open('pessoa_juridica.txt', 'a') as file:
            file.write(pessoa_juridica.nome+"\n")

        return 'salvo'

    def read(self, id):
         #---- listando uma pessoa_juridica
        with open('pessoa_juridica.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line == id:
                    return line

        return 'nao encontrado'

    def read_all(self):
         #---- listando uma lista pessoa_juridica
        return 'listar todos'

    def update(self):
         #---- alterando a pessoa_juridica
        return 'alterado'

    def delete(self):
         #---- deletando a pessoa_juridica
        return 'excluído'

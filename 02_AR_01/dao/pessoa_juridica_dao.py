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

    def delete(self):
         #---- deletando a pessoa_juridica
        return 'excluído'
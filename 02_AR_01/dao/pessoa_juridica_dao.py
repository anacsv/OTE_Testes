from model.pessoa_juridica import PessoaJuridica
from dao.base_dao import BaseDao

class PessoaJuridicaDao(BaseDao):
    # --- CRUD 

    def __init__(self):
        super().__init__(PessoaJuridica)

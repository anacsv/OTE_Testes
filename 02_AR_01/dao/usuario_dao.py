
from model.usuario import Usuario
from dao.base_dao import BaseDao

class UsuarioDao(BaseDao):
    def __init__(self):
        super().__init__(Usuario)

    

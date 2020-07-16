
from model.usuario import Usuario
from dao.base_dao import BaseDao

class UsuarioDao(BaseDao):
    def create(self, model:Usuario):
        super().create(model)

    

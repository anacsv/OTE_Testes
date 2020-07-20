from model.produto import Produto
from dao.base_dao import BaseDao

class ProdutoDao(BaseDao):

    def __init__(self, classe):
        super().__init__(classe)

    def create(self, produto: Produto):
        super().create(produto)

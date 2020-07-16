from model.produto import Produto
from dao.base_dao import BaseDao

class ProdutoDao(BaseDao):

    def create(self, produto: Produto):
        super().create(produto)

from model.produto import Produto
from dao.base_dao import BaseDao

class ProdutoDao(BaseDao):

    def __init__(self):
        super().__init__(Produto)

    def create(self, produto: Produto):
        return super().create(produto)

    def read_by_id(self, id):
        return super().read_by_id(id)

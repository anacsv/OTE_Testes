from model.produto import Produto
from dao.base_dao import BaseDao

class ProdutoDao(BaseDao):

    def __init__(self):
        super().__init__(Produto)

    def read(self, id = None):
        result = super().read(id)
        if type(result) == list:
            lista_produtos = []
            for item in result:
                produto = self.__create_object(item)
                lista_produtos.append(produto)
            return lista_produtos
        return self.__create_object(result)
    
    def __create_object(self, item_str: str) -> Produto:
        produto = Produto()
        obj_array = item_str.split(';')
        produto.id = obj_array[0]
        produto.nome = obj_array[1]
        produto.preco = obj_array[2]
        produto.descricao = obj_array[3]
        return produto

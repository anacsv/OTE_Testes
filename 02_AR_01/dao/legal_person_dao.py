from model.legal_person import LegalPerson
from dao.base_dao import BaseDao

class LegalPersonDao(BaseDao):
    # --- CRUD 

    def __init__(self):
        super().__init__(LegalPerson)

    def read(self, id = None):
        result = super().read(id)
        if type(result) == list:
            legal_person_list = []
            for item in result:
                pjd = self.__obj_converter(item)
                legal_person_list.append(pjd)
            return legal_person_list
        return self.__obj_converter(result)

    def __obj_converter(self, item_str:str) -> LegalPerson :
        legal_person = LegalPerson()
        obj_array = item_str.split(';')
        legal_person.id = obj_array[0]
        legal_person.name = obj_array[1]
        legal_person.date = obj_array[2]
        legal_person.cnpj = obj_array[3]
        return legal_person
    

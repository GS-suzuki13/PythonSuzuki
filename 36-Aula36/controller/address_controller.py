import sys
sys.path.append('/Users/900142/Desktop/PythonSuzuki/36-Aula36')

from dao.address_dao import AddressDao
from model.address import Address

class AddressController:
    dao = AddressDao()

    def list_all(self):
        return self.dao.list_all()
    def search_for_id(self, id):
        return self.dao.search_for_id(id)
    def save(self, address:Address):
        return self.dao.save(address)
    def change(self, address:Address):
        return self.dao.change(address)
    def delete(self, id):
        return self.dao.delete(id)

controller = AddressController()
a = controller.search_for_id(1)
print(a) 

































































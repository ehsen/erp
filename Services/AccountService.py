from DataModels.MongoModels import Account,IfrsCodes
from mongoengine import ValidationError
from Kernel import dummy_data
from Kernel import HelperFunc
from MongoService import MongoService
class AccountService:
    """
    This class will provide all logic related to an Account.
    """

    def new_account(self,acc_data:dict):
        """
        This function receive dict as input. The value type and keys of dict should exactly follow the
        Account in mongo models. It returns True If account successfully

        :param acc_data:dict
        :return:
        """
        try:
            #TODO Need to rethink whether I should validate data here

            mongo_obj = Account(**acc_data)

            mongo_obj.validate()

            return mongo_obj
        except ValidationError as e:
            invalid_fields=HelperFunc.parse_error(str(e),acc_data)
            return False,invalid_fields
        except Exception as e:
            return False,str(e)

    def new_ifrs_code(self,data:dict):
        """
        Creates a new IFRS code. Basically its just placeholder for consistency sake. Otherwise the ifrs data
        can be directly dumped to MongoDB without performing any validation, since pydantic will handle the validation
        part.
        :param data:
        :return:
        """
        mongo_obj = IfrsCodes(**data)
        return mongo_obj












HelperFunc.connect_db()
data = dummy_data.account_data[0]
x = AccountService()
obj = x.new_account(data)
result,id = MongoService.save_to_db(obj)
print(f"result = {result}, id = {type(id)}")


"""
HelperFunc.connect_db()
data = dummy_data.ifrs_data[0]
x= AccountService()
obj = x.new_ifrs_code(data)
MongoService.save_to_db(obj)
"""
#x= AccountService()
#x.parse_error("ofofo",{"acc_type":"hello","acc_group":"group"})











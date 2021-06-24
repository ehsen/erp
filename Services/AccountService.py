from DataModels.MongoModels import Account
from mongoengine import ValidationError
from Kernel import dummy_data
from Kernel import HelperFunc

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
            Account(**acc_data).validate()
            return True,acc_data
        except ValidationError as e:
            invalid_fields=HelperFunc.parse_error(str(e),acc_data)
            return False,invalid_fields
        except Exception as e:
            return False,str(e)

    def save_to_db(self,data):
        pass



"""
data = dummy_data.account_data[0]
x = AccountService()
print(x.new_account(data))
"""
#x= AccountService()
#x.parse_error("ofofo",{"acc_type":"hello","acc_group":"group"})











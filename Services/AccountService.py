from DataModels.MongoModels import Account
from mongoengine import ValidationError
from Kernel import dummy_data


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
            print(self.parse_error(str(e)))
            raise
        except Exception:
            raise

    def save_to_db(self,data):
        pass

    def parse_error(self,validation_error:str):
        error_str = validation_error.split("of")
        return error_str

"""
data = dummy_data.account_data[0]
x = AccountService()
print(x.new_account(data))
"""












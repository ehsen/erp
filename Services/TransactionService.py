import uuid

from dataclasses import dataclass
from datetime import datetime
from DataModels import MongoModels
from dummy_data import list_data





class Transaction:
    """"
    This class is the core of ERP. It generates accounting transactions plus it will be basis of
    any transaction where debits and credits are involved Such as Process Costing in a manufacturing
    enviorenement or stock movement etc...
    """

    def __init__(self,trans_data:list):

        self.uuid = uuid.uuid4()
        self.trans_data = trans_data






    def validate_transaction(self):
        for item in self.trans_data:
            pass
















    def gen_transaction(self):
        return self








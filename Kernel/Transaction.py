import uuid
from AccTypes import Side
from datetime import datetime
from pydantic import *

class Transaction:
    """"
    This class is the core of ERP. It generates accounting transactions plus it will be basis
    any transaction where debits and credits are involved Such as Process Costing in a manufacturing
    enviorenement.
    """
    """"
    def __init__(self,date_time:datetime,side:str,account:str,amount:float):
        self.uuid = uuid.uuid4()
        self.date_time = date_time
        self.side = side
        self.account = account
        self.amount = amount
    """



    def gen_transaction(self):
        return self










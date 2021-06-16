from dataclasses import dataclass
from enum import Enum
import uuid
from mongoengine.fields import *
from mongoengine import Document,connect
from AccTypes import AccType,AccGroup

"""
THIS IS THE STARTING POINT OF ERP. If you are reading code start from here

This file defines all the constructs (Models) of accounting entries which will be the 
core of ERP. We can produce 360 view using just various transactions or simply accounting
entries. Whether its process costing or fund accounting or anything else.

Problem is, programmers make ERP complicated. Being an accountant, I would try to implement 
using just simple accounting constructs, because I have plenty of stuff of worry about than just 
doing kung fu with python

AT THE MOMENT I WILL FOCUS ONLY ON TAX COMPLAINCE OF PAKISTAN and IFRS.
"""

class Account(Document):
    code = IntField()
    acc_group = EnumField(AccGroup)
    acc_type = EnumField(AccType)
    name = StringField(max_length=30)
    tax_code = StringField()
    ifrs_code = StringField()
    tags = DictField()


@dataclass
class Transaction:
    tranx_id = StringField()



class Item(Document):
    item_code = StringField(max_length=30)
    name = StringField(max_length=30)
    uuid = UUIDField(binary=False)

#x=Account(code = 1,name="Rent Account")
#x.save()

"""
for acc in Account.objects(acc_type = "Expense"):
    print(acc.name)
    print(type(acc.acc_group.value))
"""

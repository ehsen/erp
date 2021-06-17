from mongoengine.fields import *
from mongoengine import Document
from Kernel.AccTypes import AccType,AccGroup,Side

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
    doc_id = StringField(unique=True)

    acc_group = EnumField(AccGroup)
    acc_type = EnumField(AccType)
    name = StringField(max_length=30)
    tax_code = StringField()
    ifrs_code = StringField()
    tags = DictField()



class TransactionModel(Document):
    """
    This class defines structure of Transaction in database. account field should be a reference. But I want to
    avoid refrences. Data accuracy can be ensured at validation level.
    """
    doc_id = StringField(unique=True)
    uuid = UUIDField(primary_key=True,unique_with='doc_id')
    date_time = DateTimeField()
    side = EnumField(Side)
    account = StringField()
    amount = FloatField()
    round_off_diff = FloatField()

class Item(Document):
    doc_id = StringField(unique=True)
    item_code = StringField(max_length=30,unique=True)
    name = StringField(max_length=30)
    uuid = UUIDField(binary=False,unique=True)

#x=Account(code = 1,name="Rent Account")
#x.save()

"""
for acc in Account.objects(acc_type = "Expense"):
    print(acc.name)
    print(type(acc.acc_group.value))
"""

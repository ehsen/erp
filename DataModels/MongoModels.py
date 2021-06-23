from mongoengine.fields import *
from mongoengine import Document,connect
from Kernel.AccTypes import AccType,AccGroup,Side
from Kernel.dummy_data import list_data

"""
THIS IS THE STARTING POINT OF ERP. If you are reading code start from here

This file defines all the constructs (Models) of accounting entries which will be the 
core of ERP. We can produce 360 view using just various transactions or simply accounting
entries. Whether its process costing o
r fund accounting or anything else.

Problem is, programmers make ERP complicated. Being an accountant, I would try to implement 
using just simple accounting constructs, because I have plenty of stuff of worry about than just 
doing kung fu with python

AT THE MOMENT I WILL FOCUS ONLY ON TAX COMPLIANCE OF PAKISTAN and IFRS.
"""

class Account(Document):
    doc_id = SequenceField(unique=True)

    acc_group = StringField(required=True)
    acc_type = StringField(required=True)
    name = StringField(max_length=30)
    tax_code = StringField()
    ifrs_code = StringField()
    tags = DictField()
    meta = {'allow_inheritance':True}



class TransactionModel(Document):
    """
    This class defines structure of Transaction in database. account field should be a reference. But I want to
    avoid refrences. I can ensure the accuracy of account names seperately.
    """
    doc_id = IntField(unique=True)
    uuid = UUIDField(primary_key=True,unique_with='doc_id')
    trans_type = StringField(required=True)
    date_time = DateTimeField(required=True)
    side = EnumField(Side,required=True)
    account = StringField(required=True)
    amount = FloatField(required=True)
    round_off_diff = FloatField()

class Item(Document):
    doc_id = IntField(unique=True,required=True)
    item_code = StringField(max_length=30,unique=True)
    name = StringField(max_length=30,required=True)
    inventory_type = StringField(required=True)
    uuid = UUIDField(unique=True,required=True)

class InventoryTypes(Document):
    uuid = UUIDField(required=True)
    name = StringField(max_length=30,unique=True)


class TransSeq(Document):

    doc_id = SequenceField(unique=True)

class ItemSeq(Document):
    doc_id = SequenceField(unique=True)

class EntityModel(Document):
    uuid = UUIDField(required=True)
    entity_type = StringField(required=True)
    name = StringField(required=True)
    address = StringField()
    city = StringField()
    country = StringField()
    extra_data = DictField()

class StockEntryModel(TransactionModel):
    warehouse_name = StringField(required=True,max_length=30)
    item_name = StringField(required=True)

class AssetRegister(Document):
    pass








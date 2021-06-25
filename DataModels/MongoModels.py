from mongoengine.fields import *
from mongoengine import Document,connect,EmbeddedDocument
from Kernel.AccTypes import AccType,AccGroup,Side,TransTypes
from Kernel.HelperFunc import connect_db
from Kernel.dummy_data import list_data
from mongoengine.queryset.base import DENY


"""
THIS IS THE STARTING POINT OF ERP. If you are reading code start from here

This file defines all the constructs (Models) of accounting entries which will be the 
core of ERP. We can produce 360 view using just various transactions or simply accounting
entries. Whether its process costing o
r fund accounting or anything else.


AT THE MOMENT I WILL FOCUS ONLY ON TAX COMPLIANCE OF PAKISTAN and IFRS.
"""


class IfrsCodes(Document):
    ifrs_code = StringField(unqiue=True,required=True)
    description = StringField()

class Address(EmbeddedDocument):
    street_address = StringField()
    city = StringField()
    country = StringField()


class Customer(Document):
    customer_name = StringField(required=True)
    addresses = EmbeddedDocumentListField(Address)


class Account(Document):

    acc_code = SequenceField()
    acc_group = EnumField(AccGroup,required=True)
    acc_type = EnumField(AccType,required=True)
    name = StringField(max_length=30,required=True)
    tax_code = StringField()
    ifrs_code = StringField()
    tags = DictField()
    meta = {'allow_inheritance':True}



class TransactionModel(Document):
    """
    This class defines structure of Transaction in database. account field should be a reference. But I want to
    avoid refrences. I can ensure the accuracy of account names seperately.
    """
    doc_id = SequenceField(unique=True)
    uuid = UUIDField(primary_key=True,unique=True,required=True)
    trans_type = EnumField(TransTypes,required=True)
    date_time = DateTimeField(required=True)
    side = EnumField(Side,required=True)
    account = ReferenceField(Account,required=True)
    amount = FloatField(required=True)
    extra_data = DictField()
    meta = {'allow_inheritance': True}

class Item(Document):
    doc_id = SequenceField(unique=True,required=True)
    item_code = StringField(max_length=30,unique=True)
    name = StringField(max_length=30,required=True)
    inventory_type = StringField(required=True)
    sale_account = ReferenceField(Account,required=True)
    cogs_account = ReferenceField(Account,required=True)
    inventory_account = ReferenceField(Account,required=True)
    extra_data = DictField()
    meta = {'allow_inheritance':True}


class InventoryTypes(Document):

    name = StringField(max_length=30,unique=True)

"""
class TransSeq(Document):

    doc_id = SequenceField(unique=True)

class ItemSeq(Document):
    doc_id = SequenceField(unique=True)
"""
class EntityModel(Document):

    entity_type = StringField(required=True)
    name = StringField(required=True)
    address = StringField()
    city = StringField()
    country = StringField()
    extra_data = DictField()
    meta = {'allow_inheritance':True}

class Warehouse(Document):
    name = StringField(required=True)
    extra_data = DictField()



class StockEntryModel(TransactionModel):
    item = ReferenceField(Item,required=True)

class ReceiveableEntry(TransactionModel):
    customer = ReferenceField(Customer,required=True)

class AssetRegister(Document):
    pass










from dataclasses import dataclass
from enum import Enum


"""
THIS IS THE STARTING POINT OF ERP. If you are reading code start 

This file defines all the constructs of accounting entries which will be the 
core of ERP. We can produce 360 view using just various transactions or simply accounting
entries. Whether its process costing or fund accounting or anything else.

Problem is, programmers make ERP complicated. Being an accountant, I would try to implement 
using just simple accounting constructs, because I have plenty of stuff of worry about than just 
doing kung fu with python

AT THE MOMENT I WILL FOCUS ONLY ON TAX COMPLAINCE OF PAKISTAN and IFRS.
"""
class Side(Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class TransTypes(Enum):
    JournalEntry = "JournalEntry"
    CashEntry = "CashEntry"
    BankEntry = "BankEntry"
    StockEntry = "StockEntry"

@dataclass
class Account:
    code: int
    acc_type: str
    name: str
    category: str
    tax_code: str
    ifrs_code: str


@dataclass
class Transaction:
    pass

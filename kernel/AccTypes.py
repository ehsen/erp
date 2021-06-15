from dataclasses import dataclass
from enum import Enum

"""
This file defines various account types which will be used in ERP Accounting and other modules.
Generally, only a small set of account types is required for an ERP to function, and thats what most
accounting softwares and ERPs currently do. 

My view is we should precisely know the purpose of each account. Why? it would make automatic compliance
a lot more easier. For example let say  user defines Income Tax Withheld account with 
some funny name as regular Current Liability. There is no way we can ensure compliance with Tax 
authorities or IFRS (becuase we don't know the nature of current liability).

Let me give you an example In Pakistan we file WithHolding Tax Return Under Section 165.
By using correct accounts, its just a straightforward affair to generate that return automatically.
Similar compliance requirement also exists in US and UK. 


Furthermore, Unlike other softwares this ERP will follow recognition/derecognition/fair value measurement
principles of IFRS and in future US GAAP (Once I get comfortable with US regulatory system). 

Distributing Transactions in only Assets and Liabilities is High School Accounting.
Actual work is compliance & reporting, which is way more complex.


SO RULE OF THUMB IS : Explicit is better than implicit.  
"""



class AccType(Enum):
    CurrentAsset = "CurrentAsset"
    NonCurrentAsset = "NonCurrentAsset"
    CurrentLiability = "CurrentLiability"
    NonCurrentLiability = "NonCurrentLiability"
    Depreciation = "Depreciation"
    COGS = "COGS"
    Income = "Income"
    Expense = "Expense"
    IncomeTaxWithheld = "IncomeTaxWithheld"
    SalesTaxWithheld = "SalesTaxWithheld"
    Lease = "Lease"
    Inventory = "Inventory"
    Equity = "Equity"
    FinancialInstrument = "FinancialInstrument"
    Goodwill = "Goodwill" # This account will only be used for IFRS 3 Business Combinations
    ContigentConsideration = "ContigentConsideration" # This account will only be used for IFRS 3 Business Combinations
    Amortization = "Amortization"
    OpeningBalance = "OpeningBalance"
    DefferedIncome="DefferedIncome"
    TradeReceiveable = "TradeReceiveable"
    TradePayable = "TradePayable"
    ContractAsset = "ContractAsset"
    ContractLiablity = "ContractLiablity"
    DefferedTaxAsset = "DefferedTaxAsset" #IAS12
    DefferedTaxLiability = "DefferedTaxLiability" #IAS12
    InvestmentProperty = "InvestmentProperty" # IAS40

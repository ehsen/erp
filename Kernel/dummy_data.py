from datetime import datetime
import uuid

# Dummy Transaction data to test various functions
list_data = [{"date_time":datetime(2021,4,4),'side':"DEBIT",'account':"Sales1","amount":355.0,
        "uuid":uuid.uuid4(),"round_off_diff":12.0,"doc_id":"Hello"},
             {"date_time": datetime(2021, 4, 4), 'side': "CREDIT", 'account': "TEST", "amount": 200.0,
              "uuid": uuid.uuid4(), "round_off_diff": 12.0, "doc_id": "Hello"}
             ,{"date_time":datetime(2021,4,4),'side':"CREDIT",'account':"TEST","amount":155.0,
        "uuid":uuid.uuid4(),"round_off_diff":12.0,"doc_id":"Hello"}]


list_data_wrong_amounts = [{"date_time":datetime(2021,4,4),'side':"DEBIT",'account':"TEST","amount":10.0,
        "uuid":uuid.uuid4(),"round_off_diff":12.0,"doc_id":"Hello"},
             {"date_time": datetime(2021, 4, 4), 'side': "DEBIT", 'account': "TEST", "amount": 200.0,
              "uuid": uuid.uuid4(), "round_off_diff": 12.0, "doc_id": "Hello"}
             ,{"date_time":datetime(2021,4,4),'side':"CREDIT",'account':"TEST","amount":155.0,
        "uuid":uuid.uuid4(),"round_off_diff":12.0,"doc_id":"Hello"}]


account_data = [{"acc_group":"CurrentAsset","acc_type":"CurrentAsset","name":"Cash","ifrs_code":"IFRS17"}]

ifrs_data = [{"ifrs_code":"IFRS16","description":"None"}]


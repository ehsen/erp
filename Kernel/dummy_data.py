from datetime import datetime
import uuid

# Transaction date to test various functions
list_data = [{"date_time":datetime(2021,4,4),'side':"DEBIT",'account':"TEST","amount":355.0,
        "uuid":uuid.uuid4(),"round_off_diff":12.0,"doc_id":"Hello"},
             {"date_time": datetime(2021, 4, 4), 'side': "DEBIT", 'account': "TEST", "amount": 200.0,
              "uuid": uuid.uuid4(), "round_off_diff": 12.0, "doc_id": "Hello"}
             ,{"date_time":datetime(2021,4,4),'side':"DEBIT",'account':"TEST","amount":155.0,
        "uuid":uuid.uuid4(),"round_off_diff":12.0,"doc_id":"Hello"}]

list_data_wrong_amounts = [{"date_time":datetime(2021,4,4),'side':"DEBIT",'account':"TEST","amount":10.0,
        "uuid":uuid.uuid4(),"round_off_diff":12.0,"doc_id":"Hello"},
             {"date_time": datetime(2021, 4, 4), 'side': "DEBIT", 'account': "TEST", "amount": 200.0,
              "uuid": uuid.uuid4(), "round_off_diff": 12.0, "doc_id": "Hello"}
             ,{"date_time":datetime(2021,4,4),'side':"DEBIT",'account':"TEST","amount":155.0,
        "uuid":uuid.uuid4(),"round_off_diff":12.0,"doc_id":"Hello"}]


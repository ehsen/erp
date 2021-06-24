import mongoengine

#from erp_errors import DocIDFailed
from mongoengine import register_connection,connect
import os

"""
Helper functions are some general ultilities which doesn't fit anywhere.
"""

def handle_round_off(amount:float) -> (float,float):
    """
    This function rounds off the number as per policy and returns the rounded number
    alongwith the difference between actual amount and rounded amount
    :param amount:
    :return:
    """
    rounded_figure:float = round(amount,2)
    round_off_diff:float = 0.0
    if rounded_figure > amount:
        round_off_diff = rounded_figure - amount
    elif rounded_figure < amount:
        round_off_diff = amount - rounded_figure
    elif rounded_figure == amount:
        pass

    return rounded_figure, round(round_off_diff,4)

def validate_accs(acc_list:list,data:dict) -> bool:
    """
    This function checks whether the accounts in Transaction are correct. It will compare entered accounts
    against some cache

    :param schema:
    :param data:
    :return: bool
    """
    pass


def is_debit_credit_eq(trans_data:list) -> (bool,float,float):
    """
    This function checks whether debits and credits are equal in transaction data.
    Note: This function should only be used after transaction data is validated against mongo model

    :param trans_data:
    :return:
    """
    sum_of_debits:float = 0.0
    sum_of_credits:float = 0.0
    for item in trans_data:
        if item.get("side") == "DEBIT":
            sum_of_debits += item.get("amount")
        elif item.get("side") == "CREDIT":
            sum_of_credits += item.get("amount")
    #print(sum_of_debits)
    #print(sum_of_credits)
    if sum_of_debits != sum_of_credits:
        return False,sum_of_debits,sum_of_credits
    elif sum_of_debits == sum_of_credits:
        return True,sum_of_debits,sum_of_credits



def filter_dict_list(key,value,dict_list:list) -> list:
    """
    This function filters a list of dictionaries based on the value of a key and returns the filtered dict
    :param filter:
    :param dict_list:
    :return:
    """
    result = [d for d in dict_list if d.get(key)==value]
    return result

def generate_doc_id(model_name:object):
    """
    This function takes input from MongoModels class to generate a doc_id. For example
    if you want to generate doc_id for a transaction you will use give TransSeq class from
    MongoModels as input to this function.
    :return: Int
    """

    init_model = model_name()
    doc_id = init_model.save()
    #print(doc_id.doc_id)
    #print(type(doc_id.doc_id))

    if isinstance(doc_id.doc_id,int):
        return doc_id.doc_id
    else:
        raise #DocIDFailed("Failed to generate document id (doc_id)")

def connect_db():
    MONGO_DB_ALIAS = os.getenv('MONGO_DB_ALIAS')
    MONGO_TEST_URL = os.getenv('MONGO_TEST_URL')

    retries = 0
    while retries <= 10:
        try:
            connect(db=MONGO_DB_ALIAS,alias="default",host=MONGO_TEST_URL)
            print("DB Connected")
            return True
        except Exception:
            retries += 1
            if retries == 10:
                raise

def parse_error(validation_error:str,data_dict:dict):
    """
    This function parse the mongoengine validation error and returns the list of fields
    with validation error. This function requires the mongoengine validation error and original data_dict
    against which the validation is applied.

    :param validation_error:
    :param data_dict:
    :return:
    """

    keys_list = [item for item in data_dict.keys()]
    invalid_data = []
    for item in keys_list:
        if item in validation_error:
            invalid_data.append(item)


    return invalid_data
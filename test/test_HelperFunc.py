import pytest

from Kernel import HelperFunc, dummy_data
import unittest

"""
def test_handle_round_off():
    round_off_fig,diff = HelperFunc.handle_round_off(2.546)

    assert (round_off_fig,diff) == (2.55,0.004)
"""
class TestHelperFunc(unittest.TestCase):

   def test_is_debit_credit_eq_success(self):
       print("Test for equal debit credits")
       data = dummy_data.list_data
       func_result = HelperFunc.is_debit_credit_eq(data)
       print(f"func result = {func_result}")
       actual_result = (True,355.0,355.0)
       self.assertEqual(func_result,actual_result)

   def test_is_debit_credit_eq_fail(self):
       print("Test for unequal debit credits")
       data = dummy_data.list_data_wrong_amounts
       func_result = HelperFunc.is_debit_credit_eq(data)
       actual_result = (False, 210.0,155.0)
       self.assertEqual(func_result, actual_result)

















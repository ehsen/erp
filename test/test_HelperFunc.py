import pytest

from Kernel import HelperFunc, dummy_data


def test_handle_round_off():
    round_off_fig,diff = HelperFunc.handle_round_off(2.546)

    assert (round_off_fig,diff) == (2.55,0.004)








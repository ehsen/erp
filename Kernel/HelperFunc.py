
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




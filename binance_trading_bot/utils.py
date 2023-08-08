"""
utils.py
This file contains utility functions that can be used by other modules.
"""

import math

def calculate_profit(initial_balance: float, final_balance: float) -> float:
    """
    Calculates the profit based on the initial and final balance.
    Args:
        initial_balance (float): The initial balance.
        final_balance (float): The final balance.
    Returns:
        float: The profit.
    """
    return final_balance - initial_balance

def calculate_percentage_change(initial_value: float, final_value: float) -> float:
    """
    Calculates the percentage change between the initial and final values.
    Args:
        initial_value (float): The initial value.
        final_value (float): The final value.
    Returns:
        float: The percentage change.
    """
    return ((final_value - initial_value) / initial_value) * 100

def round_down(value: float, decimal_places: int) -> float:
    """
    Rounds down a value to the specified number of decimal places.
    Args:
        value (float): The value to round down.
        decimal_places (int): The number of decimal places to round down to.
    Returns:
        float: The rounded down value.
    """
    multiplier = 10 ** decimal_places
    return math.floor(value * multiplier) / multiplier

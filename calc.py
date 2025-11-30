"""
calc.py - Module with a logic error: Division by Zero

This module contains a function that calculates the average of a list of numbers.
The bug: The function doesn't handle empty lists and will crash with ZeroDivisionError.
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: A list of numeric values
        
    Returns:
        The average of the numbers as a float
        
    Raises:
        ZeroDivisionError: When the list is empty (this is the bug!)
    """
    total = sum(numbers)
    count = len(numbers)
    return total / count  # Bug: No check for empty list, crashes when count == 0

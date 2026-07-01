###########################################################################################
# Name        : digit_utils.py
# Description : Utility functions for performing various digit-based operations.
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

"""
digit_utils.py

A collection of utility functions for digit-based operations.

Functions:
"""

###########################################################################################
# Basic Digit Operations
###########################################################################################

def count_digits(number):
    """
    Counts the total number of digits in a number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Total number of digits
    """

    digit = 0
    digitCount = 0

    if number == 0:
        return 1
    
    while number != 0:
        digit = number % 10
        digitCount = digitCount + 1
        number = number // 10

    return digitCount

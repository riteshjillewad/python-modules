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

    digitCount = 0

    if number == 0:
        return 1
    
    if number < 0:
        number = abs(number)
    
    while number != 0:
        digitCount = digitCount + 1
        number = number // 10

    return digitCount

def sum_digits(number):
    """
    Returns the sum of all digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Sum of digits
    """

    if number < 0:
        number = abs(number)

    digitsSum = 0

    while number != 0:
        digit = number % 10
        digitsSum = digitsSum + digit
        number = number // 10

    return digitsSum

def product_digits(number):
    """
    Returns the product of all digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Product of all digits 
    """

    if number == 0:
        return 0

    number = abs(number)
    product = 1

    while number > 0:
        digit = number % 10
        product = product * digit
        number = number // 10

    return product

def reverse_number(number):
    """
    Returns the reversed number

    Parameters:
    ----------------------------
    number: int 

    Returns:
    ----------------------------
    int
        Reversed number
    """

    if number == 0:
        return 0
    
    # We store the sign, so that we can handle negative numbers case
    if number < 0:
        sign = -1
    else:
        sign = 1
    
    number = abs(number)
    reverse = 0

    while number != 0:
        reverse = reverse * 10 + number % 10
        number = number // 10

    return sign * reverse

def first_digit(number):
    """
    Returns first digit from number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        First digit
    """

    if number == 0:
        return 0
    
    number = abs(number)

    # Extract the digits, until single digit is left
    while number >= 10:
        number = number // 10

    return number

def last_digit(number):
    """
    Returns the last digit from number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Last digit
    """

    return abs(number) % 10

def middle_digit(number):
    """
    Returns the middle digit(s) of a number.
    If the number has an even amount of digits, returns the two middle digits.

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        The middle digit(s)
    """

    num_str = str(abs(number))
    length = len(num_str)
    
    mid_index = length // 2
    
    if length % 2 != 0:
        # ODD: Return the single exact middle digit
        return int(num_str[mid_index])
    else:
        # EVEN: Return the two middle digits combined
        return int(num_str[mid_index - 1 : mid_index + 1])
    
def replace_digit(number, target_digit, new_digit):
    """
    Replaces the target digit with new digit

    Parameters:
    ----------------------------
    number: int
    number: targetDigit
    number: newDigit

    Returns:
    ----------------------------
    int
        Number with replaced digit
    """

    if number < 0:
        sign = -1
    else:
        sign = 1

    # converting number to string
    number_str = str(abs(number))

    # making use of .replace(target, replacement)
    new_num_str = number_str.replace(str(target_digit), str(new_digit))

    return sign * int(new_num_str)

###########################################################################################
# Digit Counting Operations
###########################################################################################

def count_even_digits(number):
    """
    Return the count of even digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Even digits count
    """

    if number == 0:
            return 1

    even_digit_count = 0
    number = abs(number)

    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            even_digit_count += 1 
        number = number // 10

    return even_digit_count

def count_odd_digits(number):
    """
    Return the count of odd digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Odd digits count
    """

    odd_digit_count = 0
    number = abs(number)

    while number > 0:
        digit = number % 10
        if digit % 2 != 0:
            odd_digit_count += 1 
        number = number // 10

    return odd_digit_count

def count_zero_digits(number):
    """
    Return the count of zero digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Zero digits count
    """

    zero_digit_count = 0
    number = abs(number)

    while number > 0:
        digit = number % 10
        if digit == 0:
            zero_digit_count += 1
        number = number // 10

    return zero_digit_count

def count_zero_digits(number):
    """
    Return the count of non-zero digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Non-zero digits count
    """

    non_zero_digit_count = 0
    number = abs(number)

    while number > 0:
        digit = number % 10
        if digit != 0:
            non_zero_digit_count += 1
        number = number // 10

    return non_zero_digit_count

def count_occurrences(number, target_digit):
    """
    Returns the count of target digit

    Parameters:
    ----------------------------
    number: int
    target_digit: int

    Returns:
    ----------------------------
    int
        Occurences of target digit
    """
    
    if number == 0:
        return 1 if target_digit == 0 else 0

    target_digit_count = 0
    number = abs(number)

    while number != 0:
        digit = number % 10
        if digit == target_digit:
            target_digit_count += 1
        number = number // 10

    return target_digit_count
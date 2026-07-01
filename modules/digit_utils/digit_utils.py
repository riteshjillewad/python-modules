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
def count_digits(number)
def sum_digits(number)
def product_digits(number)
def reverse_number(number)
def first_digit(number)
def last_digit(number)
def middle_digit(number)
def replace_digit(number, target_digit, new_digit)

def count_even_digits(number)
def count_odd_digits(number)
def count_zero_digits(number)
def count_non_zero_digits(number)
def count_occurences(number, target_digit)

def contains_digit(number, target_digit)
def find_first_occurence(number, target_digit)
def find_last_occurence(number, target_digit)
def find_all_occurences(number, target_digit)

def digit_frequency(number, target_digit)

"""

###########################################################################################
# Basic Digit Operations
###########################################################################################

def count_digits(number: int) -> int:
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

def sum_digits(number: int) -> int:
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

def product_digits(number: int) -> int:
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

def reverse_number(number: int) -> int:
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

def first_digit(number: int) -> int:
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

def last_digit(number: int) -> int:
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

def middle_digit(number: int) -> int:
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
    
def replace_digit(number: int, target_digit: int, new_digit: int) -> int:
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

def count_even_digits(number: int) -> int:
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

def count_odd_digits(number: int) -> int:
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

def count_zero_digits(number: int) -> int:
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

def non_zero_digit_count(number: int) -> int:
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

def count_occurrences(number: int, target_digit: int) -> int:
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

###########################################################################################
# Digit Searching Operations
###########################################################################################

def contains_digit(number: int, target_digit: int) -> bool:
    """
    Checks if number contains target digit

    Parameters:
    ----------------------------
    number: int
    target_digit: int

    Returns:
    ----------------------------
    Boolean
        True or False
    """

    if number == 0 and target_digit == 0:
        return True
    
    number = abs(number)

    while number != 0:
        if number % 10 == target_digit:
            return True
        number = number // 10

    return False

def find_first_occurrence(number: int, target_digit: int) -> int:
    """
    Finds the 0-based index of the first (leftmost) occurrence of a target digit.
    Returns -1 if the digit is not found.

    Parameters:
    ----------------------------
    number: int
    target_digit: int

    Returns:
    ----------------------------
    int
        Index of the first occurrence, or -1
    """

    digits_list = list()
    number = abs(number)

    if number == 0:
        if target_digit == 0:
            return 0
        else:
            return -1
        
    # There are two approaches for this:
    # 1. Convert to string, and use .find()
    # 2. Store digits in list, and then traverse

    # Storing the digits in list (it is from right-to-left)
    while number != 0:
        digit = number % 10
        digits_list.append(digit)
        number = number // 10

    # Reverse the list, so we can move from left-to-right
    digits_list.reverse()

    for i in range(len(digits_list)):
        if digits_list[i] == target_digit:
            return i

    return -1

def find_last_occurrence(number: int, target_digit: int) -> int:
    """
    Finds the 0-based index of the last (rightmost) occurrence of a target digit.
    Returns -1 if the digit is not found.

    Parameters:
    ----------------------------
    number: int
    target_digit: int

    Returns:
    ----------------------------
    int
        Index of the last occurrence, or -1
    """

    digits_list = list()
    number = abs(number)

    if number == 0:
        if target_digit == 0:
            return 0
        else:
            return -1
        
    while number != 0:
        digit = number % 10
        digits_list.append(digit)
        number = number // 10

    digits_list.reverse()

    for i in range(len(digits_list) - 1, -1, -1):       # start = from end list, end = -1(till 0), step = -1
        if digits_list[i] == target_digit:
            return i
        
    return -1

def find_all_occurrences(number: int, target_digit: int) -> list[int]:
    """
    Finds all 0-based indices of a target digit using mathematical list extraction.
    
    Parameters:
    ----------------------------
    number: int
    target_digit: int

    Returns:
    ----------------------------
    list
        List of all occurences of index
    """

    if number == 0:
        return [0] if target_digit == 0 else []

    number = abs(number)
    digits_list = []

    while number != 0:
        digits_list.append(number % 10)
        number = number // 10

    digits_list.reverse()

    # We traverse the list and add the matching indices
    matching_indices = []
    for i in range(len(digits_list)):
        if digits_list[i] == target_digit:
            matching_indices.append(i)

    return matching_indices

def digit_frequency(number: int, target_digit: int) -> int:
    """
    Returns the frequency of target digit

    Parameters:
    ----------------------------
    number: int
    target_digit: int

    Returns:
    ----------------------------
    int
        Frequency of digit
    """

    count = 0
    number = abs(number)

    if number == 0:
        return 1 if target_digit == 0 else 0

    while number != 0:
        digit = number % 10
        if digit == target_digit:
            count += 1
        number = number // 10

    return count

def most_frequent_digit(number: int) -> int:
    """
    Returns most frequent digit 

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Most frequent digit
    """

    if number == 0:
        return 0
    
    number = abs(number)
    frequencies = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Counting the occurences of each digit
    while number != 0:
        digit = number % 10
        frequencies[digit] += 1
        number = number // 10

    max_count = 0
    most_frequent = 0

    # We now check for most frequent
    for i in range(10):
        if frequencies[i] > max_count:
            max_count = frequencies[i]
            most_frequent = i

    return most_frequent
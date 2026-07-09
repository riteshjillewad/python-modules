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
def most_frequent_digit(number)
def least_frequent_digit(number)
def unique_digits(number)
def duplicate_digits(number)

def is_palindrome(number)
def is_armstrong(number)
def is_strong(number)
def is_neon(number)
def is_duck(number)
def is_spy(number)
def is_disarium(number)
def is_happy(number)
def is_harshad(number)
def is_automorphic(number)
def is_trimorphic(number)

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

def least_frequent_digit(number: int) -> int:
    """
    Finds the least frequent digit. 
    Only considers digits that appear at least once.

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int
        Least frequent digit
    """

    if number == 0:
        return 0
        
    number = abs(number)
    frequencies = [0] * 10
    
    present_digits = [False] * 10
    
    while number != 0:
        digit = number % 10
        frequencies[digit] += 1
        present_digits[digit] = True
        number = number // 10
        
    min_count = float('inf')
    least_frequent = -1
    
    for i in range(10):
        if present_digits[i] and frequencies[i] <= min_count:
            min_count = frequencies[i]
            least_frequent = i
            
    return least_frequent

def unique_digits(number: int) -> list[int]:
    """
    Returns the list of unique digits from a number, sorted.

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    list[int]
        List of unique digits
    """

    if number == 0:
        return [0]
    
    number = abs(number)
    unique_set = set()

    while number != 0:
        unique_set.add(number % 10)
        number = number // 10

    return sorted(list(unique_set))

def duplicate_digits(number: int) -> list[int]:
    """
    Returns list of duplicate digits in number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    list[int]:
        List of duplicate digits in number
    """

    if number == 0:
        return [0]
    
    number = abs(number)
    seen = set()                            # Track digits that we encounter
    duplicates = set()                      # To store digits that have appeared second time

    while number != 0:
        digit = number % 10
        if digit in seen:
            duplicates.add(digit)
        else:
            seen.add(digit)
        number = number // 10

    return list(duplicates)

###########################################################################################
# Digit Properties Operations
###########################################################################################

def is_palindrome(number: int) -> bool:
    """
    To check if number is palindrome or not

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    boolean:
        True or False
    """

    if number < 0:
        return False

    original = number
    rev = 0

    while number != 0:
        digit = number % 10
        rev = rev * 10 + digit
        number = number // 10

    return original == rev

def is_armstrong(number: int) -> bool:
    """
    Function to check if number is armstrong.
    Numbers that equals the sum of its own digits, each raised to the power of the total number of digits
    Ex:
        153 -> 1^3 + 5^3 + 3^3

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool: 
        True or False
    """

    if number == 0:
        return True
    
    number = abs(number)
    original = number
    sum_digits = 0
    digit_count = count_digits(number)

    while number != 0:
        digit = number % 10
        sum_digits = sum_digits + digit ** digit_count
        number = number // 10

    return sum_digits == original 

def is_strong(number: int) -> bool:
    """
    Function to check if number is strong or not.
    Number whose sum of the factorials of its digits is equal to the original number itself
    Ex:
    145 = 1! + 4! + 5!

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool:
        True or False
    """

    if number == 0:
        return False
  
    number = abs(number)
    original = number
    sum_digits = 0 

    while number != 0:
        digit = number % 10
        # <--- Factorial calcuation logic --->
        fact = 1 
        for i in range(digit, 0, -1):
            fact = fact * i
        # <--- Adding the factorial to sum --->
        sum_digits += fact
        number = number // 10

    return original == sum_digits

def is_neon(number: int) -> bool:
    """
    Checks of given number is neon number or not.
    Number where sum of the digits of it's square is equal to the original number
    Ex:
        Square of number: 9^2 = 81
        Sum the digits of the square: 8 + 1 = 9
        sum(9) equals to the original number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool:
        True or False
    """

    number = abs(number)
    sum_digits = 0
    square_number = number * number

    while square_number != 0:
        digit = square_number % 10
        sum_digits = sum_digits + digit
        square_number = square_number // 10

    return number == sum_digits

def is_duck(number: int) -> bool:
    """
    Checks if a number is a Duck Number.
    Positive number that contains atleast one 0, but 0 must not be at start

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool:
        True or False
    """
    num_str = str(number)
    
    # Check if the first digit is '0'
    if num_str[0] == '0':
        return False
        
    # Check if there is at least one '0' in the rest of the string
    return '0' in num_str

def is_spy(number: int) -> bool:
    """
    Checks if number is spy number or not.
    Number where the sum of it's digit equals to product of digits
    Ex:
        1124 -> (1+1+2+4) = 8, (1*1*2*4) = 8

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool:
        True or False
    """

    if number == 0:
        return True
    
    return sum_digits(abs(number)) == product_digits(abs(number))

def is_disarium(number: int) -> bool:
    """
    Check if number is disarium or not.
    Number where the sum of its digits, each raised to the power of their respective position 
    (starting from 1 on the far left), equals the number itself.
    Ex:
        135 = 1^1 + 3^2 + 5^3

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool:
        True or False
    """

    number = abs(number)
    original = number
    
    # Reverse to process from the far-left digit first
    reversed_num = reverse_number(number)
    
    sum_digits = 0
    index = 1

    while reversed_num != 0:
        digit = reversed_num % 10
        sum_digits += digit ** index
        reversed_num //= 10
        index += 1

    return original == sum_digits

def is_happy(number: int) -> bool:
    """
    Checks if a number is a happy number.
    (Sum of squares of digits eventually reaches 1)

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool:
        True or False
    """
    number = abs(number)
    seen = set()

    # Continue until we hit 1 (happy) or a number we've seen before (cycle)
    while number != 1 and number not in seen:
        seen.add(number)
        
        sum_of_squares = 0
        temp = number
        while temp != 0:
            digit = temp % 10
            sum_of_squares += digit * digit
            temp //= 10
        
        number = sum_of_squares

    return number == 1

def is_harshad(number: int) -> bool:
    """
    Checks if number is harshad number or not.
    Number that is exactly divisible by sum of it's digit
    Ex:
        18 -> (1+8)=9 -> 18/9 = 2

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool:
        True or False
    """

    return abs(number) % sum_digits(number) == 0

def is_automorphic(number: int) -> bool:
    """
    Checks if a number is an Automorphic number.
    (The square of the number ends in the number itself)

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool:
        True or False
    """
    if number < 0:
        return False
    
    square = number * number
    
    # If number is 25 (2 digits), we need to check square % 100
    # If number is 5 (1 digit), we need to check square % 10
    num_digits = count_digits(number)
    divisor = 10 ** num_digits
    
    return square % divisor == number

def is_trimorphic(number: int) -> bool:
    """
    Checks if a number is a Trimorphic number.
    (The cube of the number ends in the number itself)

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    bool:
        True or False
    """
    if number < 0:
        return False
        
    cube = number ** 3
    
    # Determine the divisor based on the number of digits
    num_digits = count_digits(number)
    divisor = 10 ** num_digits
    
    return cube % divisor == number

###########################################################################################
# Mathematical Digit Operations
###########################################################################################

def digital_root(number: int) -> int:
    """
    Return the digital root of the number.
    Digital root is single-digit value obtained by summing it's digit until only one digit remains

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int:
        Digital root of the number
    """

    number = abs(number)

    while number >= 10:

        digit_sum = 0

        while number != 0:
            digit = number % 10
            digit_sum += digit
            number = number // 10
        
        number = digit_sum

    return digit_sum

def sum_of_squares(number: int) -> int:
    """
    Returns the sum of squares of digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    number:
        Sum of square of digit
    """

    digit_square_sum = 0
    number = abs(number)

    while number != 0:
        digit = number % 10
        digit_square = digit * digit
        digit_square_sum += digit_square
        number = number // 10

    return digit_square_sum

def sum_of_cubes(number: int) -> int:
    """
    Returns the sum of cubes of digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    number:
        Sum of cube of digit
    """

    digit_cube_sum = 0
    number = abs(number)

    while number != 0:
        digit = number % 10
        digit_cube = digit * digit
        digit_cube_sum += digit_cube
        number = number // 10

    return digit_cube_sum

def factorial_digit_sum(number: int) -> int:
    """
    Returns the sum of factorial of digits

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    number:
        Sum of factorial of digits
    """

    number = abs(number)
    sum_of_factorial = 0

    while number != 0:
        digit = number % 10

        # Reset fact for the current digit
        fact = 1 
        # Calculate factorial for current digit
        for i in range(1, digit + 1):
            fact *= i
            
        sum_of_factorial += fact
        number //= 10

    return sum_of_factorial

###########################################################################################
# Digit Rearrangements
###########################################################################################

def sort_digit_ascending(number: int) -> int:
    """
    Returns the sorted number in ascending format

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int:
        Sorted number (ascending)
    """

    number = abs(number)
    digit_list = list()

    while number != 0:
        digit = number % 10
        digit_list.append(digit)
        number = number // 10

    # We have the sorted digit in this list
    digit_list.sort()

    # Now we will reconstruct the number
    result = 0
    for digit in digit_list:
        result = (result * 10) + digit

    return result

def sort_digit_ascending(number: int) -> int:
    """
    Returns the sorted number in ascending format

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int:
        Sorted number (ascending)
    """

    number = abs(number)
    digit_list = list()

    while number != 0:
        digit = number % 10
        digit_list.append(digit)
        number = number // 10

    # We have the sorted digit in this list
    digit_list.sort()

    # Now we will reconstruct the number
    result = 0
    for digit in digit_list:
        result = (result * 10) + digit

    return result

def sort_digit_descending(number: int) -> int:
    """
    Returns the sorted number in descending format.

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int:
        Sorted number (descending)
    """

    number = abs(number)
    if number == 0:
        return 0
        
    digit_list = list()

    while number != 0:
        digit = number % 10
        digit_list.append(digit)
        number = number // 10

    # Sort in descending order
    digit_list.sort(reverse=True)

    # Now we reconstruct the number
    result = 0
    for digit in digit_list:
        result = (result * 10) + digit

    return result

def get_largest_possible(number: int) -> int:
    """
    Returns the largest number possible by rearranging the digits.

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int:
        Largets possible number

    """
    return sort_digit_descending(number)

def get_smallest_possible(number: int) -> int:
    """
    Returns the smallest number possible by rearranging the digits.

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    int:
        Smallest possible number
    """
    return sort_digit_ascending(number)

###########################################################################################
# Digit Extraction
###########################################################################################

def extract_even_digits(number: int) -> list[int]:
    """
    Returns list of even digits from number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    list[int]:
        List of even digits
    """

    number = abs(number)
    even_list = list()

    while number != 0:
        digit = number % 10
        if digit % 2 == 0:
            even_list.append(digit)
        number = number // 10

    return even_list

def extract_odd_digits(number: int) -> list[int]:
    """
    Returns list of odd digits from number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    list[int]:
        List of odd digits
    """

    number = abs(number)
    odd_list = list()

    while number != 0:
        digit = number % 10
        if digit % 2 != 0:
            odd_list.append(digit)
        number = number // 10

    return odd_list

def extract_prime_digits(number: int) -> list[int]:
    """
    Returns the list of prime digits from number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    list[int]:
        List of prime digits
    """

    number = abs(number)
    prime_digits = {2, 3, 5, 7}
    prime_number_list = []

    while number != 0:
        digit = number % 10
        if digit in prime_digits:
            prime_number_list.append(digit)
        number //= 10

    return prime_number_list

def extract_non_prime_digits(number: int) -> list[int]:
    """
    Returns the list of non-prime digits from number.
    (Non-prime digits are 0, 1, 4, 6, 8, 9)

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    list[int]:
        List of non-prime digits
    """

    number = abs(number)
    non_prime_digits = {0, 1, 4, 6, 8, 9}
    non_prime_list = list()

    while number != 0:
        digit = number % 10
        if digit in non_prime_digits:
            non_prime_list.append(digit)
        number //= 10

    return non_prime_list

def extract_unique_digits(number: int) -> list[int]:
    """
    Returns the list of unique digits from number

    Parameters:
    ----------------------------
    number: int

    Returns:
    ----------------------------
    list[int]:
        List of unique digits
    """

    number = abs(number)
    unique_digits = set()

    while number != 0:
        digit = number % 10
        unique_digits.add(digit)
        number = number // 10

    return list(unique_digits)

###########################################################################################
# Digit Transformation
###########################################################################################

def increment_digit(num: int, counter=1) -> int:
    """
    Increments the digits of the number by 1(default)

    Parameters:
    ----------------------------
    number: int
    number: counter (tells by how much to increment)

    Return value:
    ----------------------------
    int:
        Number with incremented digits
    """

    number = abs(num)
    new_number = 0
    
    while number != 0:
        digit = number % 10
        # Wrap-around logic: (9 + 1) % 10 = 0
        digit = (digit + counter) % 10                                              # IMP
        new_number = new_number * 10 + digit
        number = number // 10

    return reverse_number(new_number)

def decrement_digit(number: int, counter=1) -> int:
    """
    Decrements the digits of the number by 1(default)

    Parameters:
    ----------------------------
    number: int
    number: counter (tells by how much to decrement)

    Return value:
    ----------------------------
    int:
        Number with decremented digits
    """

    number = abs(number)
    new_number = 0
    
    while number != 0:
        digit = number % 10
        # The modulo operator handles the wrap-around for negative results automatically
        digit = (digit - counter) % 10
        new_number = new_number * 10 + digit
        number = number // 10

    return reverse_number(new_number)

def square_digits(number: int) -> int:
    """
    Squares the digits of number

    Parameters:
    ----------------------------
    number: int

    Return value:
    ----------------------------
    int:
        number
    """

    number = abs(number)
    new_number = 0
    
    while number != 0:
        digit = number % 10
        digit = (digit * digit) % 10
        new_number = new_number * 10 + digit
        number //= 10

    return reverse_number(new_number)

def replace_even_digits(number: int, target: int) -> int:
    """
    Replaces the even digits with target

    Parameters:
    ----------------------------
    number: int
    target: int

    Return value:
    ----------------------------
    number: int
    """

    number = abs(number)
    new_number = 0

    while number != 0:
        digit = number % 10
        if digit % 2 == 0:
            digit = target
        new_number = new_number * 10 + digit
        number = number // 10
    
    return reverse_number(new_number)

def replace_odd_digits(number: int, target: int) -> int:
    """
    Replaces the odd digits with target

    Parameters:
    ----------------------------
    number: int
    target: int

    Return value:
    ----------------------------
    number: int
    """

    number = abs(number)
    new_number = 0

    while number != 0:
        digit = number % 10
        if digit % 2 != 0:
            digit = target
        new_number = new_number * 10 + digit
        number = number // 10
    
    return reverse_number(new_number)

###########################################################################################
# Number Construction
###########################################################################################

def digits_to_list(number: int) -> list[int]:
    """
    Returns the list of digits

    Parameters:
    ----------------------------
    number: int

    Return value:
    ----------------------------
    list[int]:
        List of digits
    """

    digit_list = list()
    number = abs(number)

    while number != 0:
        digit_list.append(number % 10)
        number = number // 10

    digit_list.reverse()

    return digit_list
###########################################################################################
# Name        : digit_utils.py
# Description : Utility functions for performing various digit-based operations.
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

"""
number_utils.py
A collection of utility functions for number-based (whole numbers) operations

Functions:

"""

###########################################################################################
# Basic Number Operations
###########################################################################################

def is_even(number: int) -> bool:
    """
    Returns true if number is even

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True or false
    """

    """
    Alternate approach: Bitwise operations
        Ex: 6(0110), 7(0111)
        - number & 1 == 0 (LSB 0 means no odd value is present)
        - number & 1 == 1 (LSB 1 means there is remainder of 1)
    """
    # return number % 2 == 0
    return number & 1 == 0

def is_odd(number: int) -> bool:
    """
    Returns true if number is odd

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True or false
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    
    return number & 1 != 0

def square_num(number: int) -> int:
    """
    Returns the square of the number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Square of number
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")

    return number ** 2

def cube_num(number: int) -> int:
    """
    Returns the cube of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Cube of number
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")

    return number ** 3

def power_num(base: int, exponent: int) -> int:
    """
    Returns the power value of number

    Parameters:
    ------------------------------
    base: int
    exponent: int

    Return value:
    ------------------------------
    int:
        Power value of number
    """

    if not isinstance(base, int):
        raise TypeError("Base must be an integer.")
    
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer.")

    return base ** exponent

def get_square_root(number: int | float) -> float:
    """
    Returns the square root of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Square root of number
    """

    if number < 0:
        raise ValueError("Cannot find square root of negative number")

    return number ** 0.5

def get_cube_root(number: int | float) -> float:
    """
    Returns the cube root of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Cube root of number
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")

    if number < 0:
        raise ValueError("Cannot find cube root of negative number")

    return number ** (1/3)

def get_factors(number: int) -> list[int]:
    """
    Returns the factors of the number
    
    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    list[int]:
        Factors of number
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    
    if number <= 0:
        raise ValueError("Factors are calculated for positive integers greater than 0.")

    factors = set()

    for i in range(1, int(get_square_root(number)) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)

    return sorted(list(factors))

def get_factors_count(number: int) -> int:
    """
    Returns the count of factors of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        count of factors
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    
    fact_count = 0

    if number <= 0:
        raise ValueError("Factors are calculated for positive integers greater than 0.")
    
    for i in range(1, int(get_square_root(number)) + 1):
        if number % i == 0:
            # If the factors are distinct pairs (e.g., 2 and 6 for 12), add 2
            if i * i != number:
                fact_count += 2
            # If it's a perfect square root (e.g., 5 and 5 for 25), only add 1
            else:
                fact_count += 1

    return fact_count

def get_factors_sum(number: int) -> int:
    """
    Returns the sum of factors 

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        sum of factors
    """ 

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")

    return sum(get_factors(number))

###########################################################################################
# Prime number functions
###########################################################################################

def is_prime(number: int) -> bool:
    """
    Checks if number is prime

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True or false
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")

    if number <= 1:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    limit = get_square_root(number)

    for i in range(3, int(limit) + 1, 2):
        if number % i == 0:
            return False
        
    return True

def get_next_prime(number: int) -> int:
    """
    Returns the smallest prime number greater than number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Smallest prime number greater than num
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")

    next_num = number + 1

    while True:
        # Ex: num = 2
        # next_num = 3
        if is_prime(next_num):
            # Check if next_num is prime
            return next_num
        else:
            # We increment the num and check it
            next_num += 1

def get_prev_prime(number: int) -> int:
    """
    Returns the largest prime number smaller than number.

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Largest prime number smaller than number
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    
    # case 1: no prime numbers less than 2
    if number <= 2:
        raise ValueError("No prime numbers exist that are strictly smaller than 2.")
    
    # case 2: if number is 3, then largest prev prime number is 2
    if number == 3:
        return 2

    prev_num = number - 1

    # if prev number is even, we reduce it to make it odd
    if prev_num % 2 == 0:
        prev_num -= 1 

    # We only check odd numbers
    while prev_num >= 3:
        if is_prime(prev_num):    
            return prev_num
        prev_num -= 2            
        
    return 2

def get_prime_factors(number: int) -> list[int]:
    """
    Returns the list of prime factors

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    list[int]:
        Prime factors of number
    """

    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")

    if number <= 0:
        raise ValueError("Negative numbers not allowed!")

    primefactors = set()

    for i in range(1, number + 1):
        if number % i == 0:
            if is_prime(i):
                primefactors.add(i)

    return sorted(list(primefactors))

def get_nth_prime(n: int) -> int:
    """
    Returns the nth prime number

    Parameters:
    ------------------------------
    n: int

    Return value:
    ------------------------------
    int:
        nth prime number
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n <= 0:
        raise ValueError("The position 'n' must be a positive integer greater than 0.")
        
    if n == 1:
        return 2
    
    count = 1           # we start counting from 1st prime number i.e 2
    num = 3
    
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 2

def generate_primes(limit: int) -> list[int]:
    """
    Generates a list of all prime numbers up to and including the limit

    Parameters:
    ------------------------------
    limit: int
        The upper bound up to which primes should be generated.

    Return value:
    ------------------------------
    list[int]:
        A list of prime numbers.
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    
    if limit < 2:
        return []

    # 2 is the only even prime
    primes = [2]
    
    # Check only odd numbers up to the limit
    for num in range(3, limit + 1, 2):
        if is_prime(num):
            primes.append(num)
            
    return primes

def count_primes(limit: int) -> int:
    """
    Counts the total number of prime numbers up to and including the limit

    Parameters:
    ------------------------------
    limit: int
        The upper bound up to which primes should be counted.

    Return value:
    ------------------------------
    int:
        The count of prime numbers.
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    
    if limit < 2:
        return 0

    # Start count at 1 to include the number 2
    count = 1
    
    # Check only odd numbers up to the limit
    for num in range(3, limit + 1, 2):
        if is_prime(num):
            count += 1
            
    return count

def get_gcd(a: int, b: int) -> int:
    """
    Returns the gcd of two numbers

    Parameters:
    ------------------------------  
    a: int
    b: int

    Return value:
    ------------------------------
    int:
        gcd of two numbers
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")
    
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b
    
    return a

def get_lcm(a: int, b: int) -> int:
    """
    Returns the least common multiple (LCM) of two integers.

    Parameters:
    ------------------------------
    a: int
    b: int

    Return value:
    ------------------------------
    int:
        LCM of the two numbers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")
        
    # LCM of 0 and any number is 0 by mathematical convention
    if a == 0 or b == 0:
        return 0

    a = abs(a)
    b = abs(b)

    return (a // get_gcd(a, b)) * b

###########################################################################################
# Mathematical Operations
###########################################################################################

def get_factorial(number: int) -> int:
    """
    Returns the factorial of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Factorial of number
    """

    if not isinstance(number, int):
        raise ValueError("Input must be integer.")
    
    if number == 0:
        return 1
    
    fact = 1
    for i in range(number, 0, -1):
        fact = fact * i

    return fact

def get_double_factorial(number: int) -> int:
    """
    Returns the double factorial of number

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    int:
        Factorial of number
    """

    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    
    if number < 0:
        raise ValueError("Double factorial is not defined for negative integers.")
    
    if number == 0 or number == 1:
        return 1
    
    fact = 1
    
    # case 1: if number is odd, the series multiplies down to 1
    if number % 2 != 0:
        for i in range(number, 0, -2):
            fact = fact * i

    # case 2: if number is even, the series multiplies down to 2
    if number % 2 == 0:
        for i in range(number, 1, -2):
            fact = fact * i

    return fact

###########################################################################################
# Number Properties
###########################################################################################

def is_composite(number: int) -> bool:
    """
    Checks if a number is a composite number.

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True if the number is composite, False otherwise.
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    # Numbers less than or equal to 3, and all negative numbers, are not composite
    if number <= 3:
        return False

    # A composite number is any positive integer greater than 1 that is not prime
    return not is_prime(number)

def is_power_of_three(number: int) -> bool:
    """
    Checks if a number is a perfect power of three.

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True if the number is a power of three, False otherwise.
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    if number <= 0:
        return False

    while number % 3 == 0:
        number //= 3

    return number == 1

def is_power_of_two(number: int) -> bool:
    """
    Checks if a number is a perfect power of two.

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True if the number is a power of two, False otherwise.
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
        
    # Powers of 2 must be strictly greater than 0
    if number <= 0:
        return False
        
    # Bitwise trick: checks if only one bit is set to 1
    return (number & (number - 1)) == 0

def is_square(number: int) -> bool:
    """
    Checks if a number is a perfect square.

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True if the number is a perfect square, False otherwise.
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    if number < 0:
        return False

    root = round(get_square_root(number))
    return root * root == number

def is_deficient(number: int) -> bool:
    """
    Checks if a number is a deficient number.

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True if the number is deficient, False otherwise.
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    if number <= 0:
        raise ValueError("Input must be a positive integer.")

    factor_sum = 0

    for i in range(1, number):
        if number % i == 0:
            factor_sum += i

    return factor_sum < number

def is_abundant(number: int) -> bool:
    """
    Checks if a number is an abundant number.

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True if the number is abundant, False otherwise.
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    if number <= 0:
        raise ValueError("Input must be a positive integer.")

    factor_sum = 0

    for i in range(1, number):
        if number % i == 0:
            factor_sum += i

    return factor_sum > number

def is_perfect(number: int) -> bool:
    """
    Checks if a number is a perfect number.

    Parameters:
    ------------------------------
    number: int

    Return value:
    ------------------------------
    bool:
        True if the number is perfect, False otherwise.
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    if number <= 0:
        raise ValueError("Input must be a positive integer.")

    factor_sum = 0

    for i in range(1, number):
        if number % i == 0:
            factor_sum += i

    return factor_sum == number
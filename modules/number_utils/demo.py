###########################################################################################
# Name        : demo.py
# Description : Client-side to test the implemented functions
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

from number_utils import *

def main():
    num = 25
    n = 6

    ret = is_even(num)
    print(f"Is {num} even?: {ret}")

    ret = get_next_prime(num)
    print(f"Next prime number greater than {num}: {ret}")

    ret = get_gcd(60, 48)
    print(f"GCD of 60 and 48: {ret}")

    ret = get_factorial(n)
    print(f"Factorial of {n}: {ret}")

    ret = get_double_factorial(n)
    print(f"Double factorial of {n}: {ret}")

if __name__ == "__main__":
    main()
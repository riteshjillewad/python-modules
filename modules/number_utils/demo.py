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
    n = 5

    ret = is_even(num)
    print(f"Is {num} even?: {ret}")

    ret = get_next_prime(num)
    print(f"Next prime number greater than {num}: {ret}")

    ret = get_nth_prime(n)
    print(f"{n}th prime number: {ret}")

if __name__ == "__main__":
    main()
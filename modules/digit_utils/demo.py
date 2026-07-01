###########################################################################################
# Name        : demo.py
# Description : Client-side to test the implemented functions
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

from digit_utils import *

def main():

    print("Enter number: ")
    num = int(input())

    ret = count_digits(num)
    print(f"Number of digits in {num}: {ret}")

# <-----    ADD MORE FUNCTIONS FOR TESTING     ------>

    ret = count_zero_digits(num)
    print(f"Total zero digits: {ret}")

if __name__ == "__main__":
    main()
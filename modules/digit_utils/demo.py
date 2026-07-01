###########################################################################################
# Name        : demo.py
# Description : Client-side to test the implemented functions
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

from digit_utils import *

def main():

    num = 12332214331

    ret = count_digits(num)
    print(f"Number of digits in {num}: {ret}")

# <-----    ADD MORE FUNCTIONS FOR TESTING     ------>

    ret = find_all_occurrences(num, 2)
    print(f"All occurences are: {ret}")

if __name__ == "__main__":
    main()
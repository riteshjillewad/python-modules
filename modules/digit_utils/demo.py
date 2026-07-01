###########################################################################################
# Name        : demo.py
# Description : Client-side to test the implemented functions
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

from digit_utils import count_digits

def main():

    print("Enter number: ")
    num = int(input())

    ret = count_digits(num)
    print(f"Number of digits in {num}: {ret}")

if __name__ == "__main__":
    main()
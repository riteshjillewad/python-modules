###########################################################################################
# Name        : demo.py
# Description : Client-side to test the implemented functions
# Author      : Ritesh Jillewad
# Date        : 17-07-2026
# Version     : 1.0.0
###########################################################################################

from array_utils import *

def main():

    nums = [10.25, 20, 30, 40, 50]

    ret = get_arr_len(nums)
    print(f"Length: {ret}")

if __name__ == "__main__":
    main()
###########################################################################################
# Name        : array_utils.py
# Description : Utility functions for performing various array-based operations.
# Author      : Ritesh Jillewad
# Date        : 01-07-2026
# Version     : 1.0.0
###########################################################################################

"""
array_utils.py
-------------------------------------------------------------------------------------------
A collection of utility functions for array-based operations.
-------------------------------------------------------------------------------------------

Functions:

"""

###########################################################################################
# Basic Array Operations
###########################################################################################

def get_arr_len(elements: list) -> int:
    """
    Returns the length of a list containing any type of elements.

    Parameters:
    ------------------------------
    elements: list

    Return value:
    ------------------------------
    int:
        Length of the list.
    """
    if not isinstance(elements, list):
        raise TypeError("Input must be a list.")

    count = 0

    for _ in elements:
        count += 1

    return count

def copy_arr(elements: list) -> list:
    """
    Creates and returns a new shallow copy of the list.

    Parameters:
    ------------------------------
    elements: list

    Return value:
    ------------------------------
    list:
        A new list containing the same elements.
    """

    if not isinstance(elements, list):
        raise TypeError("Input must be a list.")

    new_list = []
    for item in elements:
        new_list.append(item)
        
    return new_list

def clone_arr(elements: list) -> list:
    """
    Creates and returns a cloned duplicate of the list.

    Parameters:
    ------------------------------
    elements: list

    Return value:
    ------------------------------
    list:
        A new list containing the exact same elements.
    """

    if not isinstance(elements, list):
        raise TypeError("Input must be a list.")

    cloned_list = []
    for item in elements:
        cloned_list.append(item)
        
    return cloned_list

def reverse_arr(elements: list) -> None:
    """
    Reverses the elements of the list in-place.

    Parameters:
    ------------------------------
    elements: list

    Return value:
    ------------------------------
    None
    """
    
    if not isinstance(elements, list):
        raise TypeError("Input must be a list.")
    
    length = get_arr_len(elements)
    start = 0
    end = length - 1

    while start < end:
        temp = elements[start]
        elements[start] = elements[end]
        elements[end] = temp
        
        start += 1
        end -= 1
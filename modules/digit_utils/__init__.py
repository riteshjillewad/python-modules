from .digit_utils import (
    reverse_number, sort_digit_ascending, sort_digit_descending,
    extract_unique_digits, extract_odd_digits, extract_prime_digits,
    extract_non_prime_digits, increment_digit, decrement_digit,
    replace_even_digits, count_digits
)

# This defines the public API of your library
__all__ = [
    'reverse_number', 'sort_digit_ascending', 'sort_digit_descending',
    'extract_unique_digits', 'extract_odd_digits', 'extract_prime_digits',
    'extract_non_prime_digits', 'increment_digit', 'decrement_digit',
    'replace_even_digits', 'count_digits',
    'is_palindrome', 'is_armstrong', 'is_strong', 'is_neon',
    'is_duck', 'is_spy', 'is_disarium', 'is_happy', 'is_harshad',
    'is_automorphic', 'is_trimorphic', 'sum_digits', 'sum_of_squares',
    'factorial_digit_sum', 'digital_root'
]
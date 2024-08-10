#!/usr/bin/python3
"""
This module contains the minOperations function
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly
    `n` 'H' characters in a text file, starting with a single 'H'. The only
    operations allowed are 'Copy All' and 'Paste'.

    Args:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required to reach `n` 'H' characters.
         Returns 0 if `n` is impossible to achieve.
    """
    total = 0
    factor = 2
    num = n

    while factor * factor <= num:
        while num % factor == 0:
            total += factor
            num //= factor
        factor += 1

    if num > 1:
        total += num  # Add the remaining prime factor, if any

    return total

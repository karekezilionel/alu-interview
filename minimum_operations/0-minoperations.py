#!/usr/bin/python3
"""
Calculate the minimum number of Copy All and Paste operations
to get exactly n 'H' characters.
"""


def minOperations(n):
    """
    Return the minimum operations to reach n 'H's.

    Parameters: n (integer)

    Returns: int (minimum operations)
    """
    # if n is not a number or less than 2 Hs
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

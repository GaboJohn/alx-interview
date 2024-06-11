#!/usr/bin/python3

"""
   Method that calculates the fewest number of operations
"""


def minOperations(n):
    """
    Method that calculates the fewest number of
    operations needed to result in exactly n H
    characters in the file.
    """

    if n < 2:
        return 0

    operations = 0
    start = 2

    while start <= n:
        if n % start == 0:
            operations += start
            n //= start

        else:
            start += 1

    return operations

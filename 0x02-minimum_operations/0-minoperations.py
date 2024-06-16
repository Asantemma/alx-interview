#!/usr/bin/python3
"""A method that calculates the fewest number of operations
   needed to result in exactly n H characters in the file.
   given a number n
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

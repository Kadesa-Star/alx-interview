#!/usr/bin/python3
"""
Module for calculating n number of operations to achieve
n characters
"""


def minOperations(n):
    """
    calculate fewest number of operations
    to result into n H characters
    :param n: number of characters required
    :return: min number of operations or 0 if n cant be adchieved
    """
    if n < 2:
        return (0)

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return (operations)

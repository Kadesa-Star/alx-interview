#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): The target total.

    Returns:
        int: Minimum number of coins needed, or -1 if total cannot be achieved.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    change = 0

    for coin in coins:
        if total == 0:
            break
        """ Use as many coins of this denomination as possible """
        change += total // coin
        total %= coin  # Update the remaining total

    return change if total == 0 else -1

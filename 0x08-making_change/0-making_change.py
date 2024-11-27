#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to achieve.

    Returns:
        int: Fewest number of coins needed, or -1 if total cannot be achieved.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    total_coins = 0

    for denom in coins:
        if total <= 0:
            break
        total_coins += total // denom
        total %= denom

    return total_coins if total == 0 else -1

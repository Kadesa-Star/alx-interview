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

    # Initialize a DP array to represent minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total 0

    # Fill the DP table
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the amount can't be achieved
    return dp[total] if dp[total] != float('inf') else -1

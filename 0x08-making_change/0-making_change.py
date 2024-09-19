#!/usr/bin/python3
"""
This module contains the makeChange function
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of integers representing the values of
        available coins.
        total (int): The total amount of money for which change is needed.

    Returns:
        int: The fewest number of coins required to make the total amount.
             - Returns 0 if total is 0 or less.
             - Returns -1 if the total cannot be met with the given coins.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

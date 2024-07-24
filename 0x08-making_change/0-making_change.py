#!/usr/bin/python3
"""
A function to determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    This function will take a list of coins and use
    that to calculate how much change the total will require.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to meet with the coins.

    Returns:
        int: The fewest number of coins needed to meet the total,
             or -1 if the total cannot be met with the given coins.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    counter = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many of the current coin as possible
        num_coins = total // coin
        counter += num_coins
        total -= num_coins * coin

    # If the total is not zero, return -1 indicating it can't be met exactly
    if total != 0:
        return -1

    return counter

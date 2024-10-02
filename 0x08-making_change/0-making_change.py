#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """Generate the fewest number of coins needed to reach a total

    Args:
        coins (list): List of coin denominations
        total (int): The total amount to reach

    Returns:
        int: Fewest number of coins needed to reach the total,
             or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to try the largest denominations first
    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        if total == 0:
            break
        # Take as many coins of this denomination as possible
        if coin <= total:
            num_coins = total // coin
            total -= num_coins * coin
            coin_count += num_coins

    # If we cannot meet the total exactly, return -1
    if total != 0:
        return -1
    return coin_count

#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.
    
    :param coins: List of coin denominations available.
    :param total: The total amount to make change for.
    :return: Fewest number of coins needed to meet the total, or -1 if not possible.
    """
    if total <= 0:
        return 0
    
    # Initialize dp array with infinity values, except dp[0] which is 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate over each coin and update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, it means we couldn't make the change
    return dp[total] if dp[total] != float('inf') else -1

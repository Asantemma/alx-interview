#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a large value
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Fill the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still the large value, then we can't form that total
    return dp[total] if dp[total] != total + 1 else -1

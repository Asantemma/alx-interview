#!/usr/bin/python3
""" function that determines fewest number of coins needed
to meet a certaib amount"""
def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet
    a given amount.
    
    Args:
        coins (list[int]): List of coin denominations.
        total (int): The target amount to be met.

    Returns:
        int: The fewest number of coins needed to meet the total amount,
        or -1 if it cannot be met.
    """

    # Return 0 if the total amount is less than 1
    if total < 1:
        return 0

    # Initialize the minimum coins needed to -1
    minCoins = -1

    # Proceed only if there are coins available
    if len(coins):
        # Sort the coin denominations in descending order
        coins = sorted(coins, reverse=True)
        numCoins = len(coins)
        minCoins = 0

        # Iterate over each coin denomination
        for i in range(numCoins):
            while total:
                # Check if the current coin can be used
                if total - coins[i] >= 0:
                    # Increment the coin count and decrease the total
                    minCoins += 1
                    total -= coins[i]
                else:
                    break

        # If the total is not zero after using the coins, then the total amount cannot be met
        if total != 0:
            minCoins = -1

    return minCoins

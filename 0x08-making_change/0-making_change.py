#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the memoization table with infinity values
    memo = [float('inf')] * (total + 1)

    # Base case: zero coins needed to make zero total
    memo[0] = 0

    # Fill in the memoization table bottom-up
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                memo[i] = min(memo[i], memo[i - coin] + 1)

    # Return the fewest number of coins needed to make the total
    return memo[total] if memo[total] != float('inf') else -1

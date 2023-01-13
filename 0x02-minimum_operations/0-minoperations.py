#!/usr/bin/python3
"""
A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    op = 0
    min_op = 2
    while n > 1:
        while n % min_op == 0:
            op += min_op
            n = n / min_op
        min_op += 1
    return op

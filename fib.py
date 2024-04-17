# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 04/17/2024
# Description: Program that takes a positive integer parameter and returns the number at that position of the Fibonacci sequence.

def fib(num):
    '''Takes a positive integer and returns the Fibonacci number at that postion'''
    if num == 1 or num == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(2, num):
            a, b = b, a + b
        return b

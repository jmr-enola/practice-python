'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

from math import factorial
from typing import Set

def solution01(Nsteps: int) -> int:
    
    if Nsteps == 1:
        return 1
    
    if Nsteps <= 0:
        return 0

    ones = 0
    twos = 0
    ways = 0

    while (Nsteps >= 2 * twos):
        ones = Nsteps - 2 * twos
        ways += factorial(ones + twos) / (factorial(ones) * factorial(twos))
        twos += 1
        
    return int(ways)


def solution02(Nsteps: int) -> int:
    
    if Nsteps == 0:
        return 1
    
    if Nsteps < 0:
        return 0
    
    return solution02(Nsteps-1) + solution02(Nsteps-2)

def solution03(Nsteps: int, ways: Set[int]) -> int:
    if Nsteps == 0:
        return 0
    elif Nsteps == 1:
        return 1

    dp = [0] * (Nsteps + 1)
    dp[0] = 1

    for i in range(1, Nsteps + 1):
        total = 0
        for x in ways:
            if i - x >= 0:
                total += dp[i - x]
        dp[i] = total

    return dp[Nsteps]





'''
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''

import random

def solution01(stream):
    n = None

    for i, elem in enumerate(stream):
        
        if i == 0:
            n = elem
            continue

        if random.randint(0, i) == 0:
            n = elem

    return n

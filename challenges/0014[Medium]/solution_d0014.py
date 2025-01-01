'''
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''
import random

def estmatePi(n: int) -> float:
    onCircle = 0

    for i in range(n + 1):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            onCircle += 1

    return (4 * onCircle) / n

print(estmatePi(1000000))
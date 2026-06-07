import random
import math

def f(x):
    return -(x - 5)**2 + 25

x = 0
T = 100

while T > 1:

    neighbor = x + random.choice([-1, 1])

    delta = f(neighbor) - f(x)

    if delta > 0:
        x = neighbor

    else:
        probability = math.exp(delta / T)

        if random.random() < probability:
            x = neighbor

    T *= 0.95

print(x)
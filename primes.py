import math

import numpy as np


def primes(n: int):
    sieve = np.ones(n)
    for k in range(2, math.isqrt(n)):
        sieve[2 * k :: k] = 0
    return sieve.nonzero()[0][2:]


if __name__ == "__main__":
    n = 500
    result = primes(n)
    print(result)

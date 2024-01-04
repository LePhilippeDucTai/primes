import math

import numpy as np


def primes(n: int):
    sieve = np.ones(n, dtype=bool)
    for k in range(2, math.isqrt(n) + 1):
        if sieve[k]:
            sieve[2 * k :: k] = False
    return sieve.nonzero()[0][2:]


if __name__ == "__main__":
    n = 500
    result = primes(n)
    print(result)

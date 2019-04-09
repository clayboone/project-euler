import math


def lpf(n: int) -> int:
    """Return the largest prime factor of a number `n`"""
    # Algorithm found online. Comments are for my understanding.
    assert n > 1
    max_prime = None

    # where n is 110, primes are [2, 5, 11]
    # Strip the number of 2s that divide n
    while n % 2 == 0:
        max_prime = 2
        n >>= 1  # n /= 2

    # n is odd now (55), primes are [5, 11]
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # range(3, 8, 2) = [3, 5, 7]
        while n % i == 0:
            max_prime = i
            n //= i

    # n (11) is still > 2 and must be prime
    if n > 2:
        max_prime = n

    return int(max_prime)

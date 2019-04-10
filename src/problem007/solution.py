import math


class Solution(object):

    @staticmethod
    def isPrime(n: 'number to test') -> bool:
        """Return whether or not a number is prime."""
        if n < 2:
            return False

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True

    @staticmethod
    def nth_prime(n) -> int:
        """Return the n-th prime number."""
        current = 2
        primes = []

        while len(primes) < n:
            if Solution.isPrime(current):
                primes.append(current)

            current += 1

        return primes[-1]

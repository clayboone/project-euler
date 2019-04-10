import math


class Solution(object):

    @staticmethod
    def lcm(factor_list: 'int[] or generator') -> int:
        resulting_primes_list = {}

        for i in factor_list:
            current_primes_list = {}

            for factor in Solution.get_prime_factors(i):
                if factor in current_primes_list:
                    current_primes_list[factor] += 1
                else:
                    current_primes_list[factor] = 1

            for prime, count in current_primes_list.items():
                if prime in resulting_primes_list:
                    resulting_primes_list[prime] = max([
                        resulting_primes_list[prime],
                        count
                    ])
                else:
                    resulting_primes_list[prime] = count

        ret = 1
        for prime, count in resulting_primes_list.items():
            ret *= math.pow(prime, count)

        return int(ret)

    @staticmethod
    def get_prime_factors(n: int) -> 'int[]':
        """Return a list of the prime factors of `n`."""
        primes = []

        # where n is 110, primes are [2, 5, 11]
        # Strip the number of 2s that divide n
        while n % 2 == 0:
            primes.append(2)
            n >>= 1  # n /= 2

        # n is odd now (55), primes are [5, 11]
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            # range(3, 8, 2) = [3, 5, 7]
            while n % i == 0:
                primes.append(i)
                n //= i

        # n (11) is still > 2 and must be prime
        if n > 2:
            primes.append(n)

        return primes

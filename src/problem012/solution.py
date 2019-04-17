from functools import reduce
from src.problem005.solution import Solution as p


class Solution(object):

    def __init__(self, min_divisors: 'int: minimum number of divisors'):
        self.min_divisors = min_divisors

    @staticmethod
    def generate_triangles():

        def triangle(n):
            """Find the n-th triangle number"""
            return int(n * (n+1) / 2)

        i = 0
        while True:
            i += 1
            yield triangle(i)

    def calculate(self):
        """Return the first triangle number with at least the number of
        divisors specified by `self.min_divisors + 1`.

        Technically, every triangle number greater than 1 will have an even
        number of divisors, so it's possible that some number has exactly 500
        divisors, the wording in the spec is "over 500 divisors", which is the
        reason for the `n+1`.

        The problem spec doesn't ask for the list of divisors, only the amount
        of divisors, so we can take a methematical shortcut by finding the
        product of the count of the prime factors plus 1.

        This solution also assumes that we're not counting negative divisors
        which would double the number factors and give different answers. The
        spec isn't clear about whether or not negative divisors should be taken
        into account, but generally speaking, they're not.
        """

        # TODO: Maybe make some 'mathlib' for common little functions like this
        # product = lambda l: reduce(lambda x, y: x * y, l, 1)
        def product(l: 'int[]'):
            '''Return the product of all numbers in an array.'''
            return reduce(lambda x, y: x * y, l, 1)

        for triangle in Solution.generate_triangles():
            primes_dict = {}

            # TODO: Two more functions for the 'mathlib':
            #     get_prime_factors(n: int) -> int[]
            #     prime_factors_dict(n: int) -> {factor: count, ...}

            # for f in [2, 2, 7] where T_n = 28
            for factor in p.get_prime_factors(triangle):
                if factor in primes_dict:
                    primes_dict[factor] += 1
                else:
                    primes_dict[factor] = 1

                # factors = {   where T_n == 28
                #   2: 2  -> 2 + 1 = 3
                #   7: 1  -> 1 + 1 = 2
                #                    3 * 2 == 6
                # }
                # Therefore: 28 has 6 factors.

                divisors = product([i+1 for i in primes_dict.values()])
                if divisors > self.min_divisors:
                    return triangle


if __name__ == "__main__":
    print(Solution(500).calculate())

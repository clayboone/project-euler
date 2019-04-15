from src.problem007.solution import Solution as p


class Solution(object):

    def __init__(self, n: int):
        self.n = n

    def calculate(self):
        s = 0

        for i in range(self.n):
            if p.isPrime(i):
                s += i

        return s


if __name__ == "__main__":
    print('The sum of all primes below two million is {}'.format(
        Solution(2_000_000).calculate()
    ))

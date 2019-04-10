from functools import reduce


class Solution(object):

    def __new__(self, n: 'int[] or iterator') -> int:
        return self.square_sums(n) - self.sum_squares(n)

    @staticmethod
    def sum_squares(n):
        return reduce(lambda x, y: x + y**2, n)

    @staticmethod
    def square_sums(n):
        return reduce(lambda x, y: x + y, n) ** 2

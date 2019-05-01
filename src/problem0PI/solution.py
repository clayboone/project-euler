class Solution(object):

    @staticmethod
    def gregory_leibniz(iterations: 'int') -> 'float: Pi':
        pi = 0
        subtract = False  # first operation is to add 4/1 to 0.

        for i in range(1, iterations * 2, 2):
            pi = pi - 4/i if subtract else pi + 4/i
            subtract = not subtract

        return pi

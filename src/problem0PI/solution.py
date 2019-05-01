class Solution(object):

    @staticmethod
    def gregory_leibniz(iterations: 'int') -> 'float':
        pi = 0.0
        adding = True

        for i in range(1, iterations * 2, 2):
            pi = pi + 4/i if adding else pi - 4/i
            adding = not adding

        return pi

from functools import reduce


def mult(l: 'array or tuple') -> 'float':
    """Return the product of all numbers in an array or tuple as a float."""
    return float(reduce(lambda x, y: x * y, l))


class Solution(object):

    @staticmethod
    def gregory_leibniz(iterations: 'int') -> 'float':
        """Calculate Pi using the Gregory-Leibniz series (slow convergence)"""
        pi = 0.0
        adding = True

        for i in range(1, iterations * 2, 2):
            pi = pi + 4/i if adding else pi - 4/i
            adding = not adding

        return pi

    @staticmethod
    def nilakantha(iterations: 'int') -> 'float':
        """Calculate Pi using the Nilakantha series (fast convergence)"""
        pi = 3.0
        adding = True

        for i in range(2, iterations * 2, 2):
            t = (i, i+1, i+2)
            pi = pi + 4 / mult(t) if adding else pi - 4 / mult(t)
            adding = not adding

        return pi

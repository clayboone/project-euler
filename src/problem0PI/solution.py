from enum import Enum
OP = Enum('Operator', 'ADD SUB')


class Solution(object):

    @staticmethod
    def gregory_leibniz(iterations: 'int') -> 'float: Pi':
        pi = 0
        op = OP.ADD

        for i in range(1, iterations * 2, 2):
            pi = pi - 4/i if op == OP.SUB else pi + 4/i
            op = OP.ADD if op == OP.SUB else OP.SUB

        return pi

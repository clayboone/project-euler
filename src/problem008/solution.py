from functools import reduce


class Solution(object):

    def __init__(self, tape: str):
        self.tape = tape

    def max_product(self, n) -> int:
        maxProd = -1
        tape = [int(x) for x in self.tape]

        for i in range(len(tape) - n):
            maxProd = max([maxProd, reduce(lambda x, y: x * y, tape[i:i+n])])

        return maxProd

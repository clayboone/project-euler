from functools import reduce


class Solution(object):

    def __init__(self, tape: 'str[]'):
        '''Instantiate a grid-searching object with an array of strings that,
        when split, would make a square grid.
        '''
        self.tape = []

        for line in tape:
            line = line.split()

            if len(line) != len(tape):
                raise ValueError('Grid is not a square.')
            else:
                self.tape.append([int(i) for i in line])

    def __call__(self, n: 'size of the search'):
        '''Search self.tape for the largest product of any `n` numbers in a row
        horizontally, vertically, and diagonally.
        '''

        # n <= 0 doesn't make sense and n == 1 is "find the biggest number"
        assert n > 1

        # self.tape is a square, so compare to either axis.
        assert n < len(self.tape)

        # Initial maximum product
        maxProd = -1

        #   product = lambda l: reduce(lambda x, y: x * y, l, 1)
        def product(l: 'int[]'):
            '''Return the product of all numbers in an array.'''
            return reduce(lambda x, y: x * y, l, 1)

        for y in range(len(self.tape) - n):
            for x in range(len(self.tape[y])):
                # Make an int[][] with dimensions 4*n: one with horizontal
                # numbers, one vertical, and two diagonal.

                if x <= len(self.tape[y]) - n:
                    # Find n-numbers horizontally
                    lines = [self.tape[y][x:x + n]]

                    # Find n-numbers vertically
                    lines.append([self.tape[y + d][x] for d in range(n)])

                    # Find n-numbers diagonally (negative slope)
                    lines.append([self.tape[y + d][x + d] for d in range(n)])

                if x >= n-1:
                    # Find n-numbers diagonally (positive slope)
                    lines.append([self.tape[y + d][x - d] for d in range(n)])

                # Find largest product
                for line in lines:
                    maxProd = max([maxProd, product(line)])

        return maxProd

    def __repr__(self):
        return 'Solution({})'.format(
            [' '.join(str(i).zfill(2) for i in line) for line in self.tape]
        )

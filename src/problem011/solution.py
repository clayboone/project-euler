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
        # What should I do here: Make 4 passes over the data, one for each
        # direction of line? Make 2, n-by-n sub-grids and remove all numbers
        # that aren't in a line? Maybe iterate all the way to the end on the
        # x-axis and put in some if's to see if we can make diagonal lines?

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
            for x in range(len(self.tape[y]) - n):
                # Make an int[][] with dimensions 3*n: one with horizontal
                # numbers, one vertical, and one diagonal.

                # Find n-numbers horizontally
                lines = [self.tape[y][x:n]]

                # Find n-numbers vertically
                l = []
                for sub_y in range(n):
                    l += [self.tape[y + sub_y][x]]

                lines.append(l)

                # Find n-numbers diagonally (negative slope).
                l = []
                for sub_xy in range(n):
                    l += [self.tape[y + sub_xy][x + sub_xy]]

                lines.append(l)

                # Find largest product
                for line in lines:
                    maxProd = max([maxProd, product(line)])

        # For this implementation we'll need to make a 2nd pass over the data
        # starting at n-1 and moving to the end on the x-axis to find all
        # products of numbers in a diagonal line with positive slope... God,
        # this is ugly.
        for y in range(len(self.tape) - n):
            for x in range(n-1, len(self.tape[y])):
                line = []

                for sub_xy in range(n):
                    line += [self.tape[y + sub_xy][x - sub_xy]]

                maxProd = max([maxProd, product(line)])

        return maxProd

    def __repr__(self):
        return 'Solution({})'.format(
            [' '.join(str(i).zfill(2) for i in line) for line in self.tape]
        )

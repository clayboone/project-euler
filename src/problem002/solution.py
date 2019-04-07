#!/usr/bin/env python3


class FiboSummer(object):

    def __init__(self,
                 maximum_value: 'int: upper-bound in the sequence',
                 multiples_to_include: 'int[]: list of nu' = None) -> None:

        self.max = maximum_value
        self.mults = multiples_to_include

    def calculate(self):
        """Calculate sum of values in the Fibonacci sequence, starting with
        [1, 2] (instead of [1, 1]). If `mults` is a list of integers, then only
        consider values which are multiples of numbers in the list.
        """
        seq = FiboSummer.build_sequence(self.max)

        if self.mults is None:
            return sum(seq, 0)
        else:
            l = []
            for el in seq:
                for x in self.mults:
                    if el % x == 0:
                        l.append(el)

            return sum(l, 0)

    @staticmethod
    def build_sequence(n: 'maximum possible value in sequence') -> 'int[]':
        fibo = [1, 2]

        while fibo[-1] + fibo[-2] <= n:
            fibo.append(fibo[-1] + fibo[-2])

        return fibo


if __name__ == '__main__':  # pragma: no cover
    print('Sum of even numbers not exceding 4 million is {}'.format(
        FiboSummer(4_000_000, [2]).calculate()
    ))

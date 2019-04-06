import unittest
from src.problem001.solution import sum_multiples_under


class TestSumMultiplesUnder(unittest.TestCase):

    def test_sum_multiples_under(self):
        self.assertEqual(sum_multiples_under(10), 23)
        self.assertEqual(sum_multiples_under(1000), 233168)

    def test_sum_multiples_under_different_inputs(self):
        self.assertEqual(sum_multiples_under(10, [4, 6]), 18)

    def test_sum_multiples_under_big_numbers(self):
        # TODO: use with a timeout?
        self.assertEqual(sum_multiples_under(100000), 2333316668)

    # TODO: Passing 0 throws a ZeroDivisionError

    # FIXME: Passing n=10 and m=[1, 1, ...] returns 45?


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

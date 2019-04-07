import unittest
from src.problem001.solution import sum_multiples_under


class TestSumMultiplesUnder(unittest.TestCase):

    def test_sum_multiples_under(self):
        self.assertEqual(sum_multiples_under(10), 45)
        self.assertEqual(sum_multiples_under(10, [1, 2, 3]), 45)
        self.assertEqual(sum_multiples_under(10, [3, 5]), 23)
        self.assertEqual(sum_multiples_under(1000, [3, 5]), 233168)
        self.assertEqual(sum_multiples_under(100000, [3, 5]), 2333316668)
        self.assertRaises(ValueError, sum_multiples_under, 10, [0])


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

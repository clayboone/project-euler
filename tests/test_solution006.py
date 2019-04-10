import unittest
from src.problem006.solution import Solution as ssd


class TestSolution(unittest.TestCase):

    def test_sum_squares(self):
        self.assertEqual(ssd.sum_squares(range(10 + 1)), 385)

    def test_square_sums(self):
        self.assertEqual(ssd.square_sums(range(10 + 1)), 3025)

    def test_solution(self):
        self.assertEqual(ssd(range(10 + 1)), 2640)
        self.assertEqual(ssd(range(100 + 1)), 25164150)


if __name__ == "__main__":
    unittest.main()

import unittest
from math import pi
from src.problem0PI.solution import Solution

FIRST_FIVE_OF_PI = str(pi)[:7]


class TestSolution(unittest.TestCase):

    def test_gegory_leibniz(self):
        result = str(Solution.gregory_leibniz(400_000))[:7]
        self.assertEqual(result, FIRST_FIVE_OF_PI)

    def test_nilakantha(self):
        result = str(Solution.nilakantha(40))[:7]
        self.assertEqual(result, FIRST_FIVE_OF_PI)


if __name__ == "__main__":
    unittest.main()

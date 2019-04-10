import unittest
from src.problem005.solution import Solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(Solution(1, 10).lcm_brute(), 2520)

        # Works, but takes ~319.0 seconds on my laptop
        # self.assertEqual(Solution(1, 20).lcm_brute(), 232792560)


if __name__ == "__main__":
    unittest.main()

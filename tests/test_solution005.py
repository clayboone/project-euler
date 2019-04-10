import unittest
from src.problem005.solution import Solution


class TestSolution(unittest.TestCase):

    def test_get_prime_factors(self):
        self.assertListEqual(Solution.get_prime_factors(8), [2, 2, 2])
        self.assertListEqual(Solution.get_prime_factors(110), [2, 5, 11])

    def test_lcm(self):
        self.assertEqual(Solution(1, 10).lcm(), 2520)
        self.assertEqual(Solution(1, 20).lcm(), 232792560)

    def test_lcm_brute(self):
        self.assertEqual(Solution(1, 10).lcm_brute(), 2520)
        # self.assertEqual(Solution(1, 20).lcm_brute(), 232792560)


if __name__ == "__main__":
    unittest.main()

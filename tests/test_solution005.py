import unittest
from src.problem005.solution import Solution as lcm


class TestSolution(unittest.TestCase):

    def test_get_prime_factors(self):
        self.assertListEqual(lcm.get_prime_factors(8), [2, 2, 2])
        self.assertListEqual(lcm.get_prime_factors(110), [2, 5, 11])

    def test_lcm(self):
        self.assertEqual(lcm.lcm(range(1, 11)), 2520)
        self.assertEqual(lcm.lcm(range(1, 21)), 232792560)


if __name__ == "__main__":
    unittest.main()

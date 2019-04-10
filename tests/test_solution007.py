import unittest
from src.problem007.solution import Solution


class TestSolution(unittest.TestCase):

    def test_isPrime(self):
        self.assertEqual(Solution.isPrime(1), False)
        self.assertEqual(Solution.isPrime(8), False)
        self.assertEqual(Solution.isPrime(29), True)

    def test_list_prime_numbers(self):
        self.assertEqual(Solution.nth_prime(6), 13)
        self.assertEqual(Solution.nth_prime(10_001), 104743)


if __name__ == "__main__":
    unittest.main()

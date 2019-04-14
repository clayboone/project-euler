import unittest
from src.problem009.solution import Solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = Solution(12)
        self.assertEqual(s.a, 3)
        self.assertEqual(s.b, 4)
        self.assertEqual(s.c, 5)
        self.assertEqual(s.sum, 12)
        self.assertEqual(s.product(), 60)
        self.assertEqual(Solution(1000).product(), 31875000)


if __name__ == "__main__":
    unittest.main()

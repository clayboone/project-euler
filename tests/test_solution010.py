import unittest
from src.problem010.solution import Solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(Solution(10).calculate(), 17)
        self.assertEqual(Solution(2_000_000).calculate(), 142913828922)


if __name__ == "__main__":
    unittest.main()

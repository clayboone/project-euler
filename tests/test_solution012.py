import unittest
from src.problem012.solution import Solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(Solution(5).calculate(), 28)
        self.assertEqual(Solution(500).calculate(), 76576500)


if __name__ == "__main__":
    unittest.main()

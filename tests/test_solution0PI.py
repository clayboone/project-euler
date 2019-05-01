import unittest
from src.problem0PI.solution import Solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        result = str(Solution.gregory_leibniz(500_000))
        self.assertEqual(result[:7], '3.14159')


if __name__ == "__main__":
    unittest.main()

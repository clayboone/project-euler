import unittest
from src.problem002.solution import FiboSummer


class TestFiboSummer(unittest.TestCase):

    def test_build_sequence(self):
        self.assertListEqual(FiboSummer.build_sequence(10)[:2], [1, 2],
                             'Sequence should start with [1, 2]')
        self.assertListEqual(FiboSummer.build_sequence(89)[-1:], [89],
                             'If possible, sequence should include `n`')

    def test_calculate(self):
        self.assertEqual(FiboSummer(100).calculate(), 231)
        self.assertEqual(FiboSummer(100, [2]).calculate(), 44)
        self.assertEqual(FiboSummer(4_000_000, [2]).calculate(), 4613732)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

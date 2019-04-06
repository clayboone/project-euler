import unittest
from solution import FiboSummer


class TestFiboSummer(unittest.TestCase):

    def test_build_sequence(self):
        self.assertListEqual(FiboSummer.build_sequence(100)[:2], [1, 2])
        self.assertListEqual(FiboSummer.build_sequence(100)[-2:], [55, 89])

    def test_calculate_example(self):
        self.assertEqual(FiboSummer(100, [2]).calculate(), 44)

    def test_calculate(self):
        self.assertEqual(FiboSummer(4_000_000, [2]).calculate(), 4613732)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

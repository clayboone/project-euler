import unittest
from src.problem003.solution import lpf


class TestLargestPrimeFactor(unittest.TestCase):

    def test_lpf(self):
        self.assertEqual(lpf(110), 11)
        self.assertEqual(lpf(13195), 29)
        self.assertEqual(lpf(600851475143), 6857)
        self.assertRaises(AssertionError, lpf, 1)

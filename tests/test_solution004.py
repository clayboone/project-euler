import unittest
from src.problem004.solution import isPalindrome
from src.problem004.solution import gen_products_from_digits
from src.problem004.solution import calculate


class TestFindPalindrome(unittest.TestCase):

    def test_isPalindrome(self):
        self.assertEqual(isPalindrome(9009), True)
        self.assertEqual(isPalindrome(1), True)
        self.assertEqual(isPalindrome(1234), False)
        self.assertEqual(isPalindrome(1234321), True)

    def test_gen_products_from_digits(self):
        count = 0

        for i in gen_products_from_digits(2):
            count += 1

            if count == 1:  # 99 * 99
                self.assertEqual(i, 9801)
            if count == 2:  # 99 * 98
                self.assertEqual(i, 9702)

    def test_calculate(self):
        self.assertEqual(calculate(2), 9009)
        self.assertEqual(calculate(3), 906609)

import math


def isPalindrome(n: int) -> bool:
    """Return whether or not a number reads the same backwards as it does
    forwards."""
    l = list(str(n))

    for i in range(math.floor(len(l) / 2)):
        temp = l[len(l)-1 - i]
        l[len(l)-1 - i] = l[i]
        l[i] = temp

    return str(n) == ''.join(l)


def gen_products_from_digits(num_digits: int) -> int:
    """Starting from the largest and working backwards, generate the product of
    two numbers with length `num_digits`"""
    m = ''

    for i in range(num_digits):
        m += '9'

    for i in range(int(m), 0, -1):
        for j in range(int(m), 0, -1):
            yield i * j


def calculate(digits: int) -> int:
    """Find that largest palindrome that can be made from multiplying two
    n-digit long numbers."""
    # This could be optimized.
    palindromes = []

    for i in gen_products_from_digits(digits):
        if isPalindrome(i):
            palindromes.append(i)

    return max(palindromes)

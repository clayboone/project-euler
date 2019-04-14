class Solution(object):

    def __init__(self, input_sum: 'int: sum of a+b+c'):
        self.input_sum = input_sum
        self.calculate()

    def calculate(self):
        # Thank you @blackpenredpen for teaching me math:
        # https://www.youtube.com/watch?v=n6vL2KiWrD4
        for n in range(self.input_sum):
            for m in range(self.input_sum):
                self.a = m**2 - n**2
                self.b = 2 * m * n
                self.c = m**2 + n**2

                if self.sum == self.input_sum:
                    return

    @property
    def sum(self):
        return self.a + self.b + self.c

    def product(self):
        return self.a * self.b * self.c


if __name__ == '__main__':
    s = Solution(1000)

    print('{}^2 * {}^2 == {}^2 with sum of {} and product {}'.format(
        s.a, s.b, s.c, s.sum, s.product()
    ))

class Solution(object):

    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def lcm_brute(self) -> int:
        """Return smallest multiple that can be evenenly divided by all numbers
        in the range from `start` to `stop`
        """
        max_mult = 1

        for i in range(self.start, self.stop + 1):
            max_mult *= i

        for mult in range(1, max_mult + 1):

            # for each number in the range specified
            for i in range(self.start, self.stop + 1):

                # if the number does not evenly divide this mult
                if mult % i != 0:

                    # continue looking for another mult
                    break

            else:
                # we didn't break from the loop, so this mult can be divided
                # evenly by all numbers in range specified
                return mult

        return max_mult

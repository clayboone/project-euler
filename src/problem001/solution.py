# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import sys


def sum_multiples_under(
        n: 'int: upper-bound to sum to' = 10,
        m: 'int: list of inputs' = [3, 5]) -> int:

    # O(n^2 * m) ~= 18 seconds when n=100000 #
    # l = []

    # for i in range(n):
    #     for j in m:
    #         if i % j == 0 and i not in l:
    #             l.append(i)

    # return(sum(l, 0))

    # O(n*m) ~= 0.03 seconds when n=100000 #
    l = []
    resulting_set = set()

    for i, val in enumerate(m):
        l.append([])

        for j in range(int(n)):
            if j % int(val) == 0:
                l[i].append(j)

        resulting_set |= set(l[i])

    return(sum(resulting_set, 0))


if __name__ == '__main__':  # pragma: no cover
    # Handle input the Linux way: pass input as args & fail on argc < 2.
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <upper-bound> [1st-multiple [2nd [...]]]')
    elif len(sys.argv) == 2:
        print(f'Sum is {sum_multiples_under(sys.argv[1])}')
    else:
        print(f'Sum is {sum_multiples_under(sys.argv[1], sys.argv[2:])}')

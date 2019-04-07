#!/usr/bin/env python3


def sum_multiples_under(
        n: 'int: upper-bound to sum to',
        m: 'int[]: list of inputs' = None) -> int:

    if m is not None and 0 in m:
        raise ValueError('Non-existant multiples cannot be summed.')
    elif m is None or 1 in m:
        return sum([x for x in range(n)])
    else:
        resulting_set = set()

        for e in m:
            l = []

            for j in range(int(n)):
                if j % int(e) == 0:
                    l.append(j)

            resulting_set |= set(l)

        return(sum(resulting_set, 0))


if __name__ == '__main__':  # pragma: no cover
    print('The sum of all multiples of 3 and 5 below 1000 is {}'.format(
        sum_multiples_under(1000, [3, 5])
    ))

#!/usr/bin/env python
"""Code generator to create the files and structure to quickly implement a new
solution."""

import os
import sys


texts = [
    # 0th: src/problemXXX/solution.py
    'class Solution(object):\n'
    '\n'
    '    def __init__(self, n: int):\n'
    '        self.answer = n\n'
    '\n'
    '    def calculate(self):\n'
    '        return self.answer\n',

    # 1st: src/problemXXX/readme.txt
    'Paste the problem description here.\n',

    # 2nd: tests/test_solutionXXX.py
    'import unittest\n'
    'from src.problem{}.solution import Solution\n'
    '\n'
    '\n'
    'class TestSolution(unittest.TestCase):\n'
    '\n'
    '    def test_solution(self):\n'
    '        self.assertEqual(Solution(4).calculate(), 4)\n'
    '\n'
    '\n'
    'if __name__ == "__main__":\n'
    '    unittest.main()\n'
]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <problem_number>')

    files = [
        'src/problem{}/solution.py',
        'src/problem{}/readme.txt',
        'tests/test_solution{}.py'
    ]

    dirs = [
        'src/problem{}'
    ]

    problem_number = sys.argv[1].zfill(3)

    # If any of the files already exist, exit with status 1.
    for file in files:
        if os.path.isfile(file.format(problem_number)):
            print('File {} already exists. Bailing out.'.format(
                file.format(problem_number)
            ))
            sys.exit(1)

    # Create the directory if necessary
    for d in dirs:
        if not os.path.isdir(d.format(problem_number)):
            os.mkdir(d.format(problem_number))

    # None of the files exist yet. Make them and exit.
    for i, file in enumerate(files):
        filename = file.format(problem_number)
        with open(filename, 'w') as f:
            f.write(texts[i].format(problem_number))

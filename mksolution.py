#!/usr/bin/env python
"""Code generator to create the files and structure to quickly implement a new
solution."""

import os
import sys

dirs = [
    'src',
    'src/problem{}',
    'tests'
]

files = {
    'src/problem{}/solution.py':
        'class Solution(object):\n'
        '\n'
        '    def __init__(self, n: int):\n'
        '        self.answer = n\n'
        '\n'
        '    def calculate(self):\n'
        '        return self.answer\n',

    'src/problem{}/readme.txt':
        'Paste the problem description here.\n',

    'tests/test_solution{}.py':
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
}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <problem_number>')

    problem_number = sys.argv[1].zfill(3)

    # If any of the files already exist, exit with status 1.
    for file in files:
        if os.path.exists(file.format(problem_number)):
            print(f'File {file.format(problem_number)} already exists.')
            sys.exit(1)

    # Make any folders if necessary
    for d in dirs:
        formatted_dir = d.format(problem_number)

        if not os.path.isdir(formatted_dir):
            os.mkdir(formatted_dir)

    # None of the files exist yet. Make them and exit.
    for file, content in files.items():
        formatted_file = file.format(problem_number)
        formatted_content = content.format(problem_number)

        with open(formatted_file, 'w') as f:
            f.write(formatted_content)

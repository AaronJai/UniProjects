#! /usr/bin/env python3

import unittest

from sorting import *

from random import Random

SEED = 2200
RUNS = 100
SIZE = 1000
RANGE = 1000


class TestSorting(unittest.TestCase):
    def __test_sorting(self, sort, name):
        random = Random(SEED)
        for i in range(RUNS):
            xs = [random.randint(0, RANGE) for _ in range(SIZE)]
            expected = sorted(xs.copy())
            received = sort(xs.copy())
            msg = f'{name} failed on run {i} with xs={xs}'
            self.assertEqual(received, expected, msg=msg)

    def test_insertion_sort(self):
        self.__test_sorting(insertion_sort, 'insertion_sort')

    def test_merge_sort(self):
        self.__test_sorting(merge_sort, 'merge_sort')


if __name__ == '__main__':
    unittest.main()

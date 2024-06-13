#! /usr/bin/env python3

import unittest

from searching import *

from random import Random

SEED = 2200
RUNS = 100
SIZE = 1000
RANGE = 1000


class TestSearching(unittest.TestCase):
    def test_cube_root(self):
        xs = [0, 1, 2, 3, 4, 4.4, -2, 0.1, -0.1]
        for x in xs:
            r = cube_root(x)
            msg = f'cube_root({x}) returned {r}'
            if r is None:
                self.assertTrue(x < 0, msg=msg)
            else:
                self.assertAlmostEqual(r*r*r, x, msg=msg)

    def test_lower_bound(self):
        random = Random(SEED)
        for i in range(RUNS):
            size = random.randint(0, SIZE)
            xs = [random.randint(0, RANGE) for _ in range(size)]
            xs.sort()
            x = random.randint(0, RANGE)
            expected = sum(y < x for y in xs)
            received = lower_bound(xs.copy(), x)
            msg = f'lower_bound(xs, x) failed with x = {x} and xs = {xs}'
            self.assertEqual(received, expected, msg=msg)

    def test_upper_bound(self):
        random = Random(SEED)
        for i in range(RUNS):
            size = random.randint(0, SIZE)
            xs = [random.randint(0, RANGE) for _ in range(size)]
            xs.sort()
            x = random.randint(0, RANGE)
            expected = sum(y <= x for y in xs)
            received = upper_bound(xs.copy(), x)
            msg = f'upper_bound(xs, x) failed with x = {x} and xs = {xs}'
            self.assertEqual(received, expected, msg=msg)


if __name__ == '__main__':
    unittest.main()

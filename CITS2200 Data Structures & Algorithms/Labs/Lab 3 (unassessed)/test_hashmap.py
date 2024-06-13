#! /usr/bin/env python3

import unittest

from hashmap import *


class TestHashMap(unittest.TestCase):
    def test_hashmap_example(self):
        n = 1000
        hashmap = HashMap()
        for i in range(n):
            hashmap[f'{i}^2'] = i * i
        self.assertEqual(len(hashmap), n)
        for i in range(len(hashmap)):
            self.assertEqual(hashmap[f'{i}^2'], i * i)

    def test_contains(self):
        n = 1000
        hashmap = HashMap()
        for i in range(n):
            self.assertFalse(f'key {i}' in hashmap)
            hashmap[f'key {i}'] = i
            self.assertTrue(f'key {i}' in hashmap)
        for i in range(n):
            self.assertTrue(f'key {i}' in hashmap)
        for i in range(n, n + n):
            self.assertFalse(f'key {i}' in hashmap)

    def test_remove(self):
        n = 1000
        hashmap = HashMap()
        for i in range(n):
            hashmap[f'key {i}'] = i
        for i in range(0, n, 2):
            self.assertEqual(hashmap.remove(f'key {i}'), i)
        for i in range(n):
            self.assertEqual(f'key {i}' in hashmap, i % 2 != 0)
        with self.assertRaises(KeyError):
            hashmap.remove('key 0')

    def test_delete(self):
        n = 1000
        hashmap = HashMap()
        for i in range(n):
            hashmap[f'key {i}'] = i
        for i in range(0, n, 2):
            self.assertTrue(hashmap.delete(f'key {i}'))
        for i in range(0, n, 2):
            self.assertFalse(hashmap.delete(f'key {i}'))

    def test_items(self):
        n = 1000
        hashmap = HashMap()
        for i in range(n):
            hashmap[f'key {i}'] = i
        items = hashmap.items()
        self.assertEqual(len(hashmap), n)
        self.assertEqual(len(items), n)
        for k, v in items:
            self.assertEqual(k, f'key {v}')


if __name__ == '__main__':
    unittest.main()

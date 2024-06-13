#! /usr/bin/env python3

import unittest

from arraylist import *


class TestArrayList(unittest.TestCase):
    def test_arraylist_example(self):
        n = 1000
        arraylist = ArrayList()
        for i in range(n):
            arraylist.append(i * i)
        self.assertEqual(len(arraylist), n)
        for i in range(len(arraylist)):
            self.assertEqual(arraylist[i], i * i)

    def test_extend(self):
        n = 1000
        arraylist = ArrayList()
        extension = ArrayList()
        for i in range(n):
            arraylist.append(i)
            extension.append(n - i)
        arraylist.extend(extension)
        self.assertEqual(len(arraylist), 2 * n)
        for i in range(n):
            self.assertEqual(arraylist[n+i], extension[i])

    def test_pop(self):
        n = 1000
        arraylist = ArrayList()
        for i in range(n):
            arraylist.append(i)
        for i in range(n):
            self.assertEqual(len(arraylist), n - i)
            self.assertEqual(arraylist.pop(), n - i - 1)
        self.assertEqual(len(arraylist), 0)
        with self.assertRaises(IndexError):
            arraylist.pop()

    def test_pop_front(self):
        n = 1000
        arraylist = ArrayList()
        for i in range(n):
            arraylist.append(i)
        for i in range(n):
            self.assertEqual(len(arraylist), n - i)
            self.assertEqual(arraylist.pop_front(), i)
        self.assertEqual(len(arraylist), 0)
        with self.assertRaises(IndexError):
            arraylist.pop_front()


if __name__ == '__main__':
    unittest.main()

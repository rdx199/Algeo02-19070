# -*- coding: utf-8 -*-
"""
    __test__.py

    Unit testing.
"""


import unittest

import vektorkata


class VektorKataTest(unittest.TestCase):

    def setUp(self):
        self.__set1 = frozenset('abcd')
        self.__set2 = frozenset('bcdef')

    def test_init(self):
        s = self.__set1
        v = vektorkata.VektorKata(s)
        self.assertEqual(v._set, s)
        self.assertEqual(len(v), len(s))
        self.assertEqual(set(iter(v)), s)
        self.assertTrue('a' in v)
        self.assertFalse('x' in v)

    def test_eq(self):
        v1 = vektorkata.VektorKata(self.__set1)
        v2 = vektorkata.VektorKata(self.__set2)
        self.assertTrue(v1 == v1)
        self.assertFalse(v1 == v2)
        self.assertNotEqual(hash(v1), hash(v2))

    def test_dot(self):
        v1 = vektorkata.VektorKata(self.__set1)
        v2 = vektorkata.VektorKata(self.__set2)
        self.assertEqual(v1 * v2, len(self.__set1 & self.__set2))

    def test_similiarity(self):
        v1 = vektorkata.VektorKata(self.__set1)
        v2 = vektorkata.VektorKata(self.__set2)
        self.assertAlmostEqual(vektorkata.similiarity(v1, v2), 0.6708203932499369)


if __name__ == '__main__':
    unittest.main()

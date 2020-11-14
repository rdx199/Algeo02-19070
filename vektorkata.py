# -*- coding: utf-8 -*-
"""
    vektorkata.py

    Modul vektor kata.
"""


__all__ = (
    'VektorKata',
    'similiarity',
    'VektorBuilder',
    'load_vektor',
    'save_vektor',
)


import sys

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()


class VektorKata:
    __slots__ = ('_set')

    def __init__(self, list_kata):
        self._set = frozenset(list_kata)

    def __repr__(self):
        return f'VektorKata({{{", ".join(self._set)!s}}})'
    def __str__(self):
        return f'{{{" ".join(self._set)!s}}}'
    def __len__(self):
        return len(self._set)
    def __iter__(self):
        return iter(self._set)
    def __contains__(self, item):
        return item in self._set

    def __eq__(self, other):
        return self._set == other._set
    def __ne__(self, other):
        return self._set != other._set
    def __hash__(self):
        return hash(self._set)

    def __mul__(self, other):
        return sum(1 for i in self._set if i in other._set)

    def panjang_vektor(self):
        from math import sqrt
        return sqrt(len(self))


def similiarity(v1, v2):
    from math import sqrt
    return (v1 * v2) / sqrt(len(v1) * len(v2))


class VektorBuilder:
    @staticmethod
    def build_vektor(string):
        return VektorKata(map(sys.intern, stemmer.stem(string).split()))

def load_vektor(f):
    return VektorKata(map(sys.intern, f.read(-1).split()))

def save_vektor(f, v):
    f.write(' '.join(v))

# -*- coding: utf-8 -*-
"""
    __main__.py

    Main file.
"""

import vektorkata
import html_getter

queries = dict()

def sort_similiarity(v):
    l = [(i, vektorkata.similiarity(v, v2)) for (i, v2) in queries.items()]
    l.sort(key=lambda x: x[1])
    return l

def main():
    for i in range(15):
        try:
            with open(f'query_{i:d}.txt', 'rt') as f:
                queries[i] = vektorkata.load_vektor(f)
        except OSError:
            pass
    print(queries)

def populate():
    s = html_getter.get_url('https://id.wikipedia.org')
    v = vektorkata.VektorBuilder.build_vektor(s)
    with open('query_0.txt', 'wt') as f:
        vektorkata.save_vektor(f, v)

if __name__ == '__main__':
    main()

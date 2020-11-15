# -*- coding: utf-8 -*-
"""
    __main__.py

    Main file.
"""

import vektorkata
import html_getter
import app

queries = dict()

def main():
    with open('test/urls.txt', 'rt') as f:
        urls = f.read(-1).split()
    for i in range(len(urls)):
        try:
            with open(f'test/query_{i:d}.txt', 'rt') as f:
                v = vektorkata.load_vektor(f)
            queries[i] = (urls[i], v)
        except OSError:
            s = html_getter.get_file(f'test/query_{i:d}.html')
            v = vektorkata.VektorBuilder.build_vektor(s)
            with open(f'test/query_{i:d}.txt', 'wt') as f:
                vektorkata.save_vektor(f, v)
            queries[i] = (urls[i], v)
    app.init(_queries=queries)
    app.app.run()

if __name__ == '__main__':
    main()

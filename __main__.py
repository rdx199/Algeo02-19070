# -*- coding: utf-8 -*-
"""
    __main__.py

    Main file.
"""

from urllib.error import URLError

import vektorkata
import html_getter
import app

urlfile = 'urls.txt'

queries = dict()

def main():
    with open(urlfile, 'rt') as f:
        urls = f.read(-1).split()
    for i in range(len(urls)):
        try:
            with open(f'query_{i:d}.txt', 'rt') as f:
                queries[i] = (urls[i], vektorkata.load_vektor(f))
        except OSError:
            print(f'Membaca {urls[i]}')
            try:
                s = html_getter.get_url(urls[i])
            except URLError:
                continue
            v = vektorkata.VektorBuilder.build_vektor(s)
            with open(f'query_{i:d}.txt', 'wt') as f:
                vektorkata.save_vektor(f, v)
            queries[i] = (urls[i], v)
    print(queries)
    app.init(_queries=queries)
    app.app.run()

if __name__ == '__main__':
    main()

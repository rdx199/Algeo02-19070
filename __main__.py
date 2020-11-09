# -*- coding: utf-8 -*-
"""
    __main__.py

    Main file.
"""

import vektorkata
import html_getter

url = 'http://id.wikipedia.org'

def main():
    s = html_getter.get_url(url)
    v = vektorkata.VektorBuilder.build_vektor(s)
    print(*v)

if __name__ == '__main__':
    main()

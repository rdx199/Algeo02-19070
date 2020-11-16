# -*- coding: utf-8 -*-
"""
    html_getter.py

    Mengambil dan membaca dokumen HTML.
"""


__all__ = (
    'get_url',
    'get_url_unclean',
    'get_file',
    'get_file_unclean',
)


import io
import urllib.request
import html.parser


_parse_tags = {
    'p',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'tr',
    'th',
    'td',
}
_no_parse_tags = {
    'script',
}


class Parser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.__list = [[]]
        self.__incdata = []

    def get_string(self):
        return ' '.join(s for l in self.__list for s in l)

    def handle_starttag(self, tag, attrs):
        if tag in _parse_tags:
            self.__incdata.append(True)
            self.__list.append([])
        elif tag in _no_parse_tags:
            self.__incdata.append(False)
        else:
            return

    def handle_endtag(self, tag):
        if len(self.__incdata) == 0:
            return
        if tag in _parse_tags or tag in _no_parse_tags:
            if self.__incdata.pop():
                ret = ''.join(self.__list.pop())
                self.__list[-1].append(ret)

    def handle_data(self, data):
        if self.__incdata and self.__incdata[-1]:
            self.__list[-1].append(data)


class AllowedChars:
    def __getitem__(self, item):
        if item >= 128:
            return None
        c = chr(item)
        if (c != '-') and c.isprintable() and (not c.isalpha()):
            return 32
        raise LookupError

_allowed_chars = AllowedChars()

def get_url(url):
    with io.TextIOWrapper(urllib.request.urlopen(url), 'utf-8') as f:
        parser = Parser()
        s = f.read(1024)
        while s:
            parser.feed(s)
            s = f.read(1024)
        return parser.get_string().casefold().translate(_allowed_chars)

def get_url_unclean(url):
    with io.TextIOWrapper(urllib.request.urlopen(url), 'utf-8') as f:
        parser = Parser()
        s = f.read(1024)
        while s:
            parser.feed(s)
            s = f.read(1024)
        return ' '.join(parser.get_string().split())

def get_file(file):
    with open(file, 'rt', encoding='utf-8') as f:
        parser = Parser()
        s = f.read(1024)
        while s:
            parser.feed(s)
            s = f.read(1024)
        return parser.get_string().casefold().translate(_allowed_chars)

def get_file_unclean(file):
    with open(file, 'rt', encoding='utf-8') as f:
        parser = Parser()
        s = f.read(1024)
        while s:
            parser.feed(s)
            s = f.read(1024)
        return ' '.join(parser.get_string().split())
#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2015-03-19 16:40:12
# Filename        : cattle/utils.py
# Description     : 

from __future__ import unicode_literals
import base64
import sys
from functools import wraps
import re
import zipfile
from HTMLParser import HTMLParser

is_py3 = sys.version[0] == '3'

def urlsafe_b64encode(s):
    """
    为了兼容python2的，返回str，并不返回 bytes
    """
    if not isinstance(s, bytes):
        s = s.encode('utf-8')
    value = base64.urlsafe_b64encode(s)

    return value.decode()

def native_str(*args):
    """
    把py2 的参数中str转成unicode
    """
    if is_py3:
        result = args
    else:
        result = map(lambda s: isinstance(s, str) and  s.decode('utf-8') or s, args)
    
    return result if len(args) != 1 else result[0]

def utf8(s):
    if is_py3:
        return isinstance(s, str) and s.encode('utf-8') or s
    else:
        return isinstance(s, unicode) and s.encode('utf-8') or str(s)


def adapter(manager_name):
    def outer_wrap(func):
        @wraps(func)
        def inner_wrap(self, *args, **kwargs):
            _manager = getattr(self, manager_name)
            func_name = func.__name__.split('_')[0]
            _manager_func = getattr(_manager, func_name)
            return _manager_func(*args, **kwargs)
        
        return inner_wrap

    return outer_wrap

class ObjectDict(object):
    def __init__(self, _data):
        self.__data = {}
        for _key, _value in _data.items():
            if _key.startswith('_'):
                setattr(self, _key, _value)
            else:
                self.__data[_key] = _value

    def __str__(self):
        return self.__data.__str__()

    def __repr__(self):
        return self.__data.__repr__()

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as e:
            raise AttributeError

    def __getitem__(self, name):
        return self.__data[name]



# https://github.com/lujinda/wiz-python/issues/5
class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        if self.lasttag in ("script", "style"):
            return

        text = data.strip()
        if len(text) > 0:
            text = re.sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()



def get_text_from_html(html):
    html = native_str(html)
    parser = _DeHTMLParser()
    parser.feed(html)
    parser.close()
    return parser.text()


def get_image_from_html(html):
    return re.findall(r'<img src="(.+?)"', html, re.U)


def generate_cache_key(cls, func, args, kwargs):
    key = cls.__class__.__name__ + func.__name__

    key += str(args) + str(kwargs)
    return key

def cache_self(func):
    @wraps(func)
    def wrap(self, *args, **kwargs):
        key = '_' + generate_cache_key(self, func, args, kwargs)
        if hasattr(self, key):
            return getattr(self, key)
        else:
            value = func(self, *args, **kwargs)
            setattr(self, key, value)
            return value

    return wrap



class _ZipFile(zipfile.ZipFile):
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwrags):
        self.close()

if hasattr(zipfile.ZipFile, '__exit__'):
    ZipFile = zipfile.ZipFile
else:
    ZipFile = _ZipFile


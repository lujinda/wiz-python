#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-11-02 10:58:01
# Filename      : test.py
# Description   : 
from __future__ import print_function, unicode_literals

from wiz.client import Wiz
from wiz.note import Note

def down_images(note):
    assert isinstance(note, Note)
    for image in note.data.images:
        with open('/tmp/' + image.name, 'wb') as fd:
            fd.write(image.data)

def down_attrs(note):
    assert isinstance(note, Note)
    for attr in note.data.attachments:
        with open('/tmp/' + attr.name, 'wb') as fd:
            fd.write(attr.data)

wiz = Wiz('q8886888@qq.com', 'zxc123')
notebook = wiz.ls_notebooks()[0] # ls_notebooks 列出所有笔记本
note = notebook.ls()[0] # notebook.ls 列出该笔记本下的所有笔记
# print(note.data.text) # 笔记数据,以文本形式列出

# down_images(note)
# down_attrs(note)

print(wiz.find_notes('a*')[0].data.body)


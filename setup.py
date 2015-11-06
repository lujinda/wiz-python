#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-11-06 14:25:42
# Filename      : setup.py
# Description   : 
from distutils.core import setup
import os
import wiz

setup(
        name = 'wiz',
        version = wiz.version,
        author = 'moment-x',
        author_email = 'q8886888@qq.com',
        license = 'GPL3',
        description = 'wiz note sdk',
        url = 'https://github.com/lujinda/wiz-python',
        packages = [
            'wiz',
            ]
        )


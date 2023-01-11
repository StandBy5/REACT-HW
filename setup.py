#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys
import platform
from setuptools import find_packages, setup


def get_about():
    about = {}
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(basedir, 'konlpy', 'about.py')) as f:
        exec(f.read(), about)
    return about


def requirements():
    # both JPype1 and JPype1-py3 don't support Windows. see http://konlpy.org/en/v0.4.4/install/.
    if platform.system() == 'Windows':
        return []

    def _openreq(reqfile):
        with open(os.path.join(os.path.dirname(__file__), reqfile)) as f:
            return f.read().splitlines()

    if sys.version_info[0] < 3:
        return _openreq('requirements2.
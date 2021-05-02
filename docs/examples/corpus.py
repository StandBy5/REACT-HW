#! /usr/bin/python
# -*- coding: utf-8 -*-

from konlpy.corpus import kobill
from konlpy.tag import Twitter; t = Twitter()
from matplotlib import pyplot as plt

pos = lambda x: ['/'.join(p) for p in t.pos(x)]
docs = [kobill.op
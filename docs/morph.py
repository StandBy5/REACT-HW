#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from time import time

from konlpy import tag
from konlpy.corpus import kolaw
from konlpy.utils import csvwrite, pprint


def tagging(tagger, text):
    r = []
    try:
        r = getattr(tag, tagger)().pos(text)
    except Exception as e:
        print "Uhoh,", e
    return r


def measure_time(taggers, mult=6):
    doc = kolaw.open('constitution.txt').read()*6
    data = [['n'] + taggers]
    for i in range(mult):
        doclen = 10**i
        times = [time()]
        diffs = [doclen]
        for tagger in taggers:
            r = tagging(tagger, doc[:doclen])
            times.append(time())
            diffs.append(times[-1] - times[-2])
            print '%s\t%s\t%s' % (tagger[:5], doclen, diffs[-1])
            pprint(r[:5])
        data.append(diffs)
        print
    return data


def measure_accuracy(taggers, text):
    print '\n%s' % text
    result = []
    for tagger in taggers:
        print tagger,
        r = tagging(tagger, text)
        pprint(r)
        result.append([tagger] + map(lambda s: ' / '.join(s), r))
    return result


def plot(result):

    from matplotlib import pylab as pl
    import scipy as sp

    if not result:
        result = sp.loa
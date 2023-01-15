#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def test_corpus_kolaw():
    from konlpy.corpus import kolaw

    fids = kolaw.fileids()

    kolaw.abspath()
    ko
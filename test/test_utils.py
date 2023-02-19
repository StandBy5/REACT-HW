#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys

def test_utils_pprint(capsys): # Fixture `capsys` allows stdout/stderr captures
    from konlpy.utils import pprint
    pprint([u"저는 소프트웨어 관련학과 입니다."])
    out, err = capsys.readouterr()
    if sys.version_info[0] < 3:
        assert out == u"[저는 소프트웨어 관련학과 입니다.]\n"
    else:
        assert out == u"['저는 소프트웨어 관련학과 입니다.']\n"

def test_utils_concordance():
    from konlpy.corpus import kolaw
    from konlpy.utils  import concordance
    doc = kolaw.open('constitution.txt').read()
    ccd = concordance(u'대한민국', doc, show=True)
    assert ccd == [0, 9, 98, 100, 110, 126, 133, 147, 787, 1836, 3620]

def test_utils_concordance_show(capsys):
    from konlpy.corpus import kolaw
    from konlpy.utils  import concordance
    doc = kolaw.open('constitution.txt').read()
    ccd = concordance(u'대한민국', doc, show=True)
    out, err =
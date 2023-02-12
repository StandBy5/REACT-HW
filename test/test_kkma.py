#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def kkma_instance():
    from konlpy.tag import Kkma
    k = Kkma()
    return k

@pytest.fixture
def string():
    return u"꽃가마 타고 강남 가자!"

def test_kkma_nouns(kkma_instance, string):
    assert kkma_instance.nouns(string) ==\
        [u'\uaf43\uac00\ub9c8', u'\ud0c0\uace0', u'\uac15\ub0
#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def hannanum_instance():
    from konlpy import init_jvm
    from konlpy.tag import Hannanum
    init_jvm()
    h = Hannanum()
    return h

@pytest.fixture
def string():
    return u"꽃가마 타고 강남 가자!"


def test_hannanum_analyze(hannanum_instance, string):
    assert hannanum_instance.analyze(string) ==\
        [[[(u'\uaf43\uac00', u'ncn'), (u'\uc774', u'jp'), (u'\ub9c8', u'ef')],
          [(u'\uaf43\uac00\ub9c8', u'ncn')],
          [(u'\uaf43\uac00', u'nqq'), (u'\uc774', u'jp'), (u'\ub9c8', u'ef')],
          [(u'\uaf43\uac00\ub9c8', u'nqq')]],
         [[(u'\ud0c0', u'pvg'), (u'\uace0', u'ecc')],
          [(u'\ud0c0', u'pvg'), (u'\uace0', u'ecs')],
          [(u'\ud0c0', u'pvg'), (u'\uace0', u'ecx')]],
         [[(u'\uac15\ub0a8', u'ncn')]],
         [[(u'\uac00', u'pvg'), (u'\uc790', u'ecc')],
          [(u'\uac00', u'pvg'), (u'\uc790', u'ecs')],
          [(u'\uac00', u'pvg'), (u'\uc790', u'ef')
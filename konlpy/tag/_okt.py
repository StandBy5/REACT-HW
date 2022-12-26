# -*- coding: utf-8 -*-
from __future__ import absolute_import

import jpype

from konlpy import jvm, utils
from konlpy.tag._common import validate_phrase_inputs


def Twitter(jvmpath=None):
    """
    The ``Twitter()`` backend has changed to ``Okt()`` since KoNLPy v0.5.0.
    See :issue:`141` for details.
    """

    from warnings import warn
    warn('"Twitter" has changed to "Okt" since KoNLPy v0.4.5.')
    return Okt(jvmpath)


class Okt():
    """
    Wrapper for `Open Korean Text <https://github.com/open-korean-text/open-korean-text>`_.

    Open Korean Text is an open source Korean tokenizer written in Scala,
    developed by Will Hohyon Ryu.

    .. code-block:: python

        >>> from konlpy.tag import Okt
        >>> okt = Okt()
        >>> print(okt.morphs(u'단독입찰보다 복수입찰의 경우'))
        ['단독', '입찰', '보다', '복수', '입찰', '의', '경우']
        >>> print(okt.nouns(u'유일하게 항공기 체계 종합개발 경험을 갖고 있는 KAI는')
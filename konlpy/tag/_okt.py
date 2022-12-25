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
    Wrapper for `Open Korean Text <https://github.com/o
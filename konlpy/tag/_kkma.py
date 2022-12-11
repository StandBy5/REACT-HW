
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import jpype

from konlpy import jvm, utils
from konlpy.tag._common import validate_phrase_inputs


__all__ = ['Kkma']


class Kkma():
    """Wrapper for `Kkma <http://kkma.snu.ac.kr>`_.

    Kkma is a morphological analyzer and natural language processing
    system written in Java, developed by the Intelligent Data Systems (IDS)
    Laboratory at `SNU <http://snu.ac.kr>`_.
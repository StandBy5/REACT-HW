# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys

try:
    from MeCab import Tagger
except ImportError:
    pass

from konlpy import utils
from konlpy.tag._common import validate_phrase_inputs


__all__ = ['Mec
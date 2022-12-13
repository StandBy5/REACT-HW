# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys

try:
    from MeCab import Tagger
except ImportError:
    pass

from konlpy import utils
from konlpy.tag._common import validate_phrase_inputs


__all__ = ['Mecab']


attrs = ['tags',        # 품사 태그
         'semantic',    # 의미 부류
         'has_jongsung',  # 종성 유무
         'read',        # 읽기
         'type',        # 타입
         'first_pos',   # 첫번째 품사
         'last_pos',    # 마지막 품사
         'original',    # 원형
         'indexed']     # 인덱스 표현


def parse(result, allattrs=False, join=False, split_inflect=False):
    def split(elem, join=False, split_inf
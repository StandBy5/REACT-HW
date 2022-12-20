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
    def split(elem, join=False, split_inflect=False) -> []:
        if not elem: return [('', 'SY')]
        segments = elem.split('\t', 1)
        if len(segments) != 2:
            return [('', 'SY')]
        s, t = segments
        features = t.split(',')

        if split_inflect and features[4] == 'Inflect':
            original = features[7]
            tokens = original.split('+')
            tokens = [token.split('/') for token in tokens]

            res = []
            for token in tokens:
                if join:
                    res.append(token[0] + '/' + token[1])
                else:
                    res.append((token[0], token[1]))
            return res
        tag = features[0]
        if join:
            return [s + '/' + tag]
        return [(s, tag)]

    if split_inflect:
        res = []
        for elem in result.splitlines()[:-1]:
            morphs = split(elem, join=join, split_inflect=split_inflect)
            res.extend(morphs)
        return res
    return [split(elem, join=join)[0] for elem in result.splitlines()[:-1]]


class Mecab():
    """Wrapper for MeCab-ko morphological analyzer.

    `MeCab`_, originally a Japanese morphological analyzer and POS tagger
    developed by the Graduate School of Informatics in Kyoto University,
    was modified to MeCab-ko by the `Eunjeon Project`_
    to adapt to the Korean language.

    In order to use MeCab-ko within KoNLPy, follow the directions in
    :ref:`optional-installations`.

    .. code-block:: python
        :emphasize-lines: 1

        >>> # MeCab installation needed
        >>> from konlpy.tag import Mecab
        >>> mecab = Mecab()
        >>> print(mecab.morphs(u'영등포구청역에 있는 맛집 좀 알려주세요.'))
        ['영등포구', '청역', '에', '
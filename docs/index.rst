
KoNLPy: Korean NLP in Python
============================

.. image:: https://travis-ci.org/konlpy/konlpy.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/konlpy/konlpy
    :height: 18px

.. image:: https://readthedocs.org/projects/konlpy/badge/?version=latest
    :alt: Documentation Status
    :target: https://readthedocs.org/projects/konlpy/?badge=latest
    :height: 18px

KoNLPy (pronounced *"ko en el PIE"*) is a Python package for natural language processing (NLP) of the Korean language.
For installation directions, see :doc:`here <install>`.

For users new to NLP, go to :ref:`start`.
For step-by-step instructions, follow the :ref:`guide`.
For specific descriptions of each module, go see the :ref:`api` documents.

.. sourcecode:: python

    >>> from konlpy.tag import Kkma
    >>> from konlpy.utils import pprint
    >>> kkma = Kkma()
    >>> pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
    [네, 안녕하세요..,
     반갑습니다.]
    >>> pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
    [질문,
     건의,
     건의사항,
     사항,
     깃헙,
     이슈,
     트래커]
    >>> pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))
    [(오류, NNG),
     (보고, NNG),
     (는, JX),
     (실행, NNG),
     (환경, NNG),
     (,, SP),
     (에러, NNG),
     (메세지, NNG),
     (와, JKM),
     (함께, MAG),
     (설명, NNG),
     (을, JKO),
     (최대한, NNG),
     (상세히, MAG),
     (!, SF),
     (^^, EMO)]
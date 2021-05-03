Exploring a document
====================

Exploring a document can consist of various components:

- Counts (characters, words, etc.)
- Checking Zipf's laws: :math:`fr=k`
- Concordances

.. literalinclude:: explore.py
    :language: python

- Console::

    nchars  : 19240
    ntokens : 4178
    nmorphs : 1501

    Top 20 frequent morphemes:
    [((의, J), 398),
     ((., S), 340),
     ((하, X), 297),
     ((에, J), 283),
     ((ㄴ다, E), 242),
     ((ㄴ,
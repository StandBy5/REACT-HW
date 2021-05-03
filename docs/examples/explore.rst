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
     ((ㄴ, E), 226),
     ((이, J), 218),
     ((을, J), 211),
     ((은, J), 184),
     ((어, E), 177),
     ((를, J), 148),
     ((ㄹ, E), 135),
     ((/, S), 131),
     ((하, P), 124),
     ((는, J), 117),
     ((법률, N), 115),
     ((,, S), 100),
     ((는, E), 97),
     ((있, P), 96),
     ((되, X), 95)]

    Locations of "대한민국" in the document:
    0 대한민국헌법 유구한 역사와
    9 대한국민은 3·1운동으로 건립된 대한민국임시정부의 법통과 불의에
    98 총강 제1조 ① 대한민국은 민주공화국이다. 
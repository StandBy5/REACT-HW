Finding collocations
====================

We can find collocations with the help of `NLTK <http://nltk.org>`_.

In order to find trigram collocations, replace `BigramAssocMeasures` with `TrigramAssocMeasures`, and `BigramCollocationFinder` with `TrigramCollocationFinder`.

.. literalinclude:: collocations.py
    :language: python

- Console::

    Collocations among tagged words:
    [((가부, NNG), (동수
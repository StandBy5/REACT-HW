Chunking
========

After :doc:`tagging a sentence with part of speech </morph>`, we can segment it into several higher level multitoken sequences, or "chunks".

Here we demonstrate a way to easily chunk a sentence, and find noun, verb and adjective phrases in Korean text, using :py:class:`nltk:nltk.chunk.regexp.RegexpParser`.

.. literalinclude:: chunking.py
    :language: python

According to the chunk grammer defined above, we have three rules to extracted phrases from our sentence.
First, we have a rule to extract noun phrases (NP), where our chunker finds a serial of nouns, followed with an optional Suffix. (Note that these rules can be modified f
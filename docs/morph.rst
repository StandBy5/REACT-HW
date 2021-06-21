Morphological analysis and POS tagging
======================================

*Morphological analysis* is the identification of the structure of morphemes and other linguistic units, such as root words, affixes, or parts of speech.

*POS (part-of-speech) tagging* is the process of marking up morphemes in a phrase, based on their definitions and contexts.
For example.::

    가방에 들어가신다 -> 가방/NNG + 에/JKM + 들어가/VV + 시/EPH + ㄴ다/EFN

POS tagging with KoNLPy
-----------------------

In KoNLPy, there are several different options you can choose for POS tagging.
All have the same input-output structure; the input is a phrase, and the output is a list of tagged morphemes.

For detailed usage instructions see the :doc:`api/konlpy.tag`.

.. seealso::
    `Korean POS tags comparison chart <https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0>`_

        Compare POS tags between several Korean analytic projects. (In Korean)

Comparison between POS tagging classes
--------------------------------------

Now, we do time and per
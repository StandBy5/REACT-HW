Multithreading with KoNLPy
==========================

Sometimes it gets boring to wait for tagging jobs to end.
How about using some concurrency tricks?
Python supports multithreading and multiprocessing out-of-the-box, and you can use them with KoNLPy as well.
Here's an example using multithreading.

.. literalinclude:: multithreading.py
    :language: python

- Console::

    Number of lines in document:
    356
    Batch tagging:
    37.758173
    Concurrent tagging:
    8.037602


Check out how much faster it gets!

.. no
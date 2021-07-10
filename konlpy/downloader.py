# -*- coding: utf-8 -*-
from __future__ import absolute_import

import hashlib
import json
import os
import subprocess
import sys
import tarfile
import zipfile

if sys.version_info[0] < 3:
    import urllib
else:
    import urllib.request as urllib

from konlpy import internals


def default_download_dir():
    """
    Returns the directory to which packages will be downloaded by default.
    This value can be overriden using the constructor,
    or on a case-by-case basis using the ``download_dir`` argument
    when calling ``download()``.

    On Windows, the default download directory is ``PYTHONHOME/lib/konlpy``,
    where *PYTHONHOME* is the directory containing Python e.g., ``C:\\Python27``.

    On all other platforms, the default directory is the first of the following
    which exists or which can be created with write permission:
    ``/usr/share/konlpy_data``, ``/usr/local/share/konlpy_data``,
    ``/usr/lib/konlpy_data``, ``/usr/local/lib/konlpy_data``, ``~/konlpy_data``.
    """

    konlpydir = internals.get_datadir()

    # On Windows, use %APPDATA%
    if sys.platform == 'win32' and 'APPDATA' in os.environ:
        homedir = os.environ['APPDATA']

    # Otherwise, install in the user's home directory
    else:
        homedir = os.path.expanduser('~/')
        if homedir == '~/':
            raise ValueError("Could not find a default download directory")

    return os.path.join(homedir, 'konlpy_data')


class Downloader(object):
    """
    A class used to access the KoNLPy data
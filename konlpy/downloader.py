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
    A class used to access the KoNLPy data server, which can be used to download packages.
    """

    PACKAGE_URL = 'http://konlpy.github.io/konlpy-data/packages/%s.%s'
    SCRIPT_URL = 'http://konlpy.github.io/konlpy-data/packages/%s.sh'
    INDEX_URL = 'http://konlpy.github.io/konlpy-data/index.json'

    INSTALLED = 'installed'
    NOT_INSTALLED = 'not installed'
    STALE = 'corrupt or out of date'

    def __init__(self, download_dir=None):
        self._download_dir = download_dir

    def download(self, id=None, download_dir=None):
        """The KoNLPy data downloader.
        With this module you can download corpora, models and other data packages
        that can be used with KoNLPy.

        Downloading packages
        ====================

        Individual packages can be downloaded by passing a single argument, the package identifier for the package that should be downloaded:

        >>> download('corpus/kobill')
        [konlpy_data] Downloading package 'kobill'...
        [konlpy_data]   Unzipping corpora/kobill.zip.

        To download all packages, simply call ``download`` with the argument 'all':

        >>> download('all')
        [konlpy_data] Downloading package 'kobill'...
        [konlpy_data]   Unzipping corpora/kobill.zip.
        ...

        """
        if download_dir is None:
            download_dir = self._download_dir

        if id is None:
            raise ValueError("Please specify a package to download. To download all available packages, pass 'all' to the argument: ``konlpy.download('all')``.")
        if id == 'all':
            raise NotImplementedError("This function is not implemented yet. Please download each package individually until further notice.")
        info = self._get_info(id)
        for msg in self._download_package(info, download_dir):
            print(msg)

    def status(self, info_or_id=None, download_dir=None):
        self.index = json.loads(urllib.urlopen(self.INDEX_URL).read().decode())
        """
        Return a constant describing the local status of the given package.
        Status can be one of ``INSTALLED``, ``NOT_INSTALLED``, or ``STALE``.
        """

        if info_or_id is None:
            raise ValueError("Please specify a package to download.")
        if isinstance(info_or_id, dict):
            info = info_or_id
        else:
            id = info_or_id
            try:
                info = self.index[id]
            except KeyError:
                raise ValueError("Package does not exist. Please check the package name.")

        if download_dir is None:
            download_dir = self._download_dir

        filepath = os.path.joi
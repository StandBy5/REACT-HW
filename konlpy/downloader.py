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
    Returns the directory t
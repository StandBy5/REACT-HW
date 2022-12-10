# -*- coding: utf-8 -*-
""" Common utility function for tagger classes """
from __future__ import absolute_import
from __future__ import unicode_literals
import sys


# For both Python 2 and Python 3 compatibility
if sys.version_info[0] >= 3:
    basestring = 
#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def hannanum_instance():
    from konlpy import init_jvm
    from konlpy.tag import Hannanum
    init_jvm()
    h = Hannanum
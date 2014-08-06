#!/usr/bin/python
# coding: utf8

import gpsimage
import pytest
import unittest

path = 'test_image.jpg'

def test_entry_points():
    gpsimage.open

def test_timezone():
    g = gpsimage.open(path)
    assert g.ok
#!/usr/bin/python
# coding: utf8

import gpsimage
import pytest
import unittest

path = 'gpsimage\\images\\test_image_garmin_montana_650.jpg'

def test_entry_points():
    gpsimage.open

def test_timezone():
    g = gpsimage.open(path)
    assert g.ok
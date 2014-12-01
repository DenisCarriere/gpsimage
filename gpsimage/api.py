#!/usr/bin/python
# coding: utf8

from .base import GPSImage

def open(path):
    """Open GPSImage

    :param ``image``: Image filepath
    """
    return GPSImage(path)
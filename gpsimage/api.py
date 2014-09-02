#!/usr/bin/python
# coding: utf8

from base import GPSImage

def open(path):
    """
    """
    return GPSImage(path)

def image_from_data(image_data):
    """
    Open an image from an in-memory BytesIO image data.
    :param image_data: BytesIO Image data.
    :return: GPSImage instance from image data.
    """
    return GPSImage(image_data, True)
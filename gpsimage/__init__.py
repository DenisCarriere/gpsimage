#!/usr/bin/python
# coding: utf8

"""
GPSImage library
~~~~~~~~~~~~~~~~

Retrieves GPS data from Geo-referenced images made easy.

Every task is made easy with tons of ``help`` & ``debug`` commands!

    >>> import gpsimage # pip install gpsimage
    >>> img = gpsimage.open('<image.jpg>')
    
    # Coordinates Latitude & Longitude in Degrees 
    >>> img.lat, img.lng
    45.413140 -75.656703

    # Altitude in Feet
    >>> img.altitude
    142.04025779
    
    # From 0 to 360 Degrees
    >>> img.direction
    165.974436341
    ...

"""

__title__ = 'gpsimage'
__version__ = '0.0.1'
__author__ = 'Denis Carriere'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Denis Carriere'

# CORE
from api import open

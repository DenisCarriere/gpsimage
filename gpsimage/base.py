from __future__ import print_function
import os
import logging
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import time
import datetime


class GPSImage(object):
    """
    GPS Image Class will contain all the geo-referenced information from the image.
    
    @Attributes
    lat - Latitude (Degrees)
    lng - Longitude (Degrees)
    altitude - Elevation Above Mean Sea Level
    datum - Coordinate system (Typically WGS84)
    ok - True or False if coordinates exists

    @Functions
    debug - Generates a report of all the attributes available
    """
    _exclude = ['lat', 'lng','debug','json','ok', 'help', 'x', 'y', 'path']
    _GPSInfo = {}
    _errors = []
    _exif = {}

    def __init__(self, path):
        self.path = os.path.abspath(path)
        self._basename = os.path.basename(self.path)

        # Exif Tags            
        self._TAGS = self._invert(TAGS)
        self._GPSTAGS = self._invert(GPSTAGS)

        # Initial Functions
        self._image = self._open_image(self.path)
        self._exif = self._open_exif(self._image)
        self._GPSInfo = self._exif.get(self._TAGS.get('GPSInfo'))

    def __repr__(self):
        if self.ok:
            return '<{0} [{1}, {2} ({3})]>'.format(self._basename, self.lat, self.lng, self.datum)
        else:
            return '<{0} [{1}>'.format(self._basename, self.status)

    def __getattr__(self, key):
        if 'GPS' in key:
            value = self._GPSInfo.get(self._GPSTAGS.get(key))
        else:
            value = self._exif.get(self._TAGS.get(key))
        # Remove extra spaces from strings
        
        if isinstance(value, (str,unicode)):
            value = value.strip()
        return value

    def _invert(self, tags):
        container = dict()
        for key, value in tags.items():
            container[value] = key
        return container

    def _open_image(self, path):
        if os.path.exists(path):
            try:
                return Image.open(path)
            except:
                raise OSError('File not an image')
        else:
            raise OSError('File Path does not exist')

    def _open_exif(self, image):
        exif = image._getexif()
        if exif:
            return exif
        else:
            self._errors.append('Exif not found')
            return {}
            
    def _divide(self, items):
        if items:
            if len(items) == 2:
                if bool(items[0] or items[1]):
                    return float(items[0]) / float(items[1])
                else:
                    return 0.0

    def _dms_to_dd(self, dms, ref):
        if len(dms) == 3:
            degrees = self._divide(dms[0])
            minutes = self._divide(dms[1]) / 60
            seconds = self._divide(dms[2]) / 60 / 60
            dd = degrees + minutes + seconds

            # South & West returns Negative values
            if ref in ['S', 'W']:
                dd *= -1
            return dd

    def _pretty(self, key, value, special=''):
        if special:
            key = special.get(key)
        if key:
            extra_spaces = ' ' * (20 - len(key))
            return '{0}{1}: {2}'.format(key, extra_spaces, value)

    def debug(self):
        # JSON Results
        print('## JSON Results')
        for key, value in self.json.items():
            print(self._pretty(key, value))
        print('')

        # Camera Raw
        if self._exif:
            print('## Camera Raw')
            for key, value in self._exif.items():
                print(self._pretty(key, value, TAGS))
            print('')

        # GPS Raw
        if self._GPSInfo:
            print('## GPS Raw')
            for key, value in self._GPSInfo.items():
                print(self._pretty(key, value, GPSTAGS))

    @property
    def status(self):
        if not self._exif:
            return 'ERROR - Exif not found'
        elif not self._GPSInfo:
            return 'ERROR - No GPS Info'
        elif not self.ok:
            return 'ERROR - No Geometry'
        else:
            return 'OK'

    @property
    def dpi(self):
        value = self._image.info.get('dpi')
        if value:
            if len(value) == 2:
                if bool(value[0] and value[1]):
                    return value
                # If both values are (0, 0) then change it to the standard 72DPI
                else:
                    return (72, 72)
        else:
            # Retrieves X & Y resolution from Exif instead of PIL Image
            x = self._divide(self.XResolution)
            y = self._divide(self.YResolution)
            if bool(x and y):
                return (int(x), int(y))

    @property
    def ok(self):
        if bool(self.lat and self.lng):
            return True
        else:
            return False

    @property
    def model(self):
        return self.Model

    @property
    def make(self):
        return self.Make

    @property
    def datum(self):
        if self.GPSMapDatum:
            return self.GPSMapDatum
        else:
            return 'WGS-84'

    @property
    def lng(self):
        lng_dms = self.GPSLongitude
        lng_ref = self.GPSLongitudeRef
        return self._dms_to_dd(lng_dms, lng_ref)

    @property
    def x(self):
        return self.lng

    @property
    def lat(self):
        lat_dms = self.GPSLatitude
        lat_ref = self.GPSLatitudeRef
        return self._dms_to_dd(lat_dms, lat_ref)

    @property
    def y(self):
        return self.lat

    @property
    def altitude(self):
        return self._divide(self.GPSAltitude)

    @property
    def direction(self):
        return self._divide(self.GPSImgDirection)

    @property
    def timestamp(self):
        return self.DateTimeOriginal

    @property
    def width(self):
        return self._image.size[0]

    @property
    def height(self):
        return self._image.size[1]

    @property
    def size(self):
        if bool(self.height and self.width):
            return (self.width, self.height)

    @property
    def geometry(self):
        if self.ok:
            return {'type':'POINT', 'coordinates':[self.lng, self.lat]}

    @property
    def satellites(self):
        if self.GPSSatellites:
            return int(self.GPSSatellites)

    @property
    def json(self):
        container = {}
        for key in dir(self):
            if bool(not key.startswith('_') and key not in self._exclude):
                value = getattr(self, key)
                if value:
                    container[key] = value
        return container

if __name__ == '__main__':
    img = GPSImage('images/garmin_montana_650.JPG')
    print(img)
    img.debug()

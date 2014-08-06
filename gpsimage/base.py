from __future__ import print_function
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


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

    def __init__(self, path):
        self._path = path
        self._basename = os.path.basename(path)

        # Exif Tags            
        self._TAGS = self._invert(TAGS)
        self._GPSTAGS = self._invert(GPSTAGS)

        # Initial Functions
        self._image = self._open_image(self._path)
        self._exif = self._open_exif(self._image)

        # Detailed Exif
        self._GPSInfo = self._exif.get(self._TAGS.get('GPSInfo'))

    def __repr__(self):
        return '<{0} ({1}) [{2}, {3}]>'.format(self._basename, self.datum, self.lat, self.lng)

    def __getattr__(self, key):
        if 'GPS' in key:
            return self._GPSInfo.get(self._GPSTAGS.get(key))
        else:
            raise 'No attributes exists'

    def _invert(self, tags):
        container = dict()
        for key, value in tags.items():
            container[value] = key
        return container

    def _open_image(self, path):
        if os.path.exists(path):
            image = Image.open(path)
            if image:
                return image
            else:
                raise 'Path is not an Image'
        else:
            raise 'Path does not exist'

    def _open_exif(self, image):
        exif = image._getexif()
        if exif:
            return exif
        else:
            raise 'Image does not contain Exif'

    def _divide(self, items):
        if len(items) == 2:
            return float(items[0]) / float(items[1])
        else:
            raise 'Unknown Equation'

    def _dms_to_dd(self, dms, ref):
        degrees = self._divide(dms[0])
        minutes = self._divide(dms[1]) / 60
        seconds = self._divide(dms[2]) / 60 / 60
        dd = degrees + minutes + seconds

        # South & West returns Negative values
        if ref in ['S', 'W']:
            dd *= -1
        return dd

    def debug(self):
        # GPS Results
        print('## GPS Results')
        print('[lat]:', img.lat)
        print('[lng]:', img.lng)
        print('[datum]:', img.datum)
        print('[altitude] (Feet):', img.altitude)
        print('[direction] (0-360):', img.direction)
        print('')

        # GPS Raw
        print('## GPS Raw')
        for key, value in self._GPSInfo.items():
            tag = GPSTAGS.get(key)
            extra_spaces = ' ' * (20 - len(tag))
            print('{0}{1}: {2}'.format(GPSTAGS.get(key), extra_spaces, value))

    @property
    def ok(self):
        if bool(self.lat and self.lng):
            return True
        else:
            return False

    @property
    def datum(self):
        return self.GPSMapDatum

    @property
    def lng(self):
        lng_dms = self.GPSLongitude
        lng_ref = self.GPSLongitudeRef
        return self._dms_to_dd(lng_dms, lng_ref)

    @property
    def lat(self):
        lat_dms = self.GPSLatitude
        lat_ref = self.GPSLatitudeRef
        return self._dms_to_dd(lat_dms, lat_ref)

    @property
    def altitude(self):
        return self._divide(self.GPSAltitude)

    @property
    def direction(self):
        return self._divide(self.GPSImgDirection)

if __name__ == '__main__':
    img = GPSImage('Garmin.jpg')
    img.debug()

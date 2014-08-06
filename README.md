# GPSImage Library

Retrieves GPS data from Geo-referenced.

GPS Image will contain all the geo-referenced information from an image.

Every task is made easy! 

![GPSImage](https://raw.githubusercontent.com/DenisCarriere/gpsimage/master/gpsimage/images/gpsimage.jpg)


## Install

**Requires** PIL module installed, for issues with Windows try to download Pillow. 

```bash
$ pip install gpsimage
```

## GPS-Camera Devices

The following GPS-Camera devices have been tested with this GPSImage python module.

If your device is not listed, feel free to send me a photo taken from your device and I will be glad to troubleshoot it.

- [Garmin Montana 650](http://sites.garmin.com/montana/)
- [Android Samsung Galaxy](http://www.samsung.com/us/topic/our-galaxy-smartphones)

## Python Example

```python
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
```

## JSON Results

This example was taken from a Android Samsung Galaxy

```python
>>> import gpsimage # pip install gpsimage
>>> img = gpsimage.open('<image.jpg>')
>>> img.json

# JSON Results
{'altitude': 79.0,
'datum': 'WGS-84',
'direction': 321.0,
'geometry': {'coordinates': [-76.4515263888889, 44.24509527777778],
'type': 'POINT'},
'height': 2592,
'make': u'Samsung',
'model': u'Galaxy Nexus',
'status': 'OK',
'timestamp': u'2014:08:06 15:29:41',
'width': 1944}
```

## Attributes

### GPS data
- **lat** or **y** - Latitude (Degrees)
- **lng** or **x** - Longitude (Degrees)
- **geometry** - GeoJSON Point
- **altitude** - Elevation Above Mean Sea Level
- **datum** - Coordinate system (Typically WGS84)
- **direction** - Camera orientation (0-360 degrees)
- **ok** - True or False if coordinates exists

### Device Specific
- **timestamp ** - Calendar dates (YYYY-MM-DD HH:MM:SS)
- **model** - Device model (Galaxy Nexus)
- **make** - Device manufacturer (Samsung)

### Standard
- **status** - Checks if everything is ok
- **width** - Dimension of image (Pixels)
- **height** - Dimension of image (Pixels)

## Functions
- **debug** - Generates a report of all the attributes available

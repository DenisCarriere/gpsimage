# GPSImage Library

Retrieves GPS data from Geo-referenced.

GPS Image will contain all the geo-referenced information from an image.

Every task is made easy! 

With tons of ``help`` & ``debug`` commands!

## Install

**Requires** PIL module installed, for issues with Windows try to download Pillow. 

```bash
    $pip install gpsimage
```

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

## Attributes

- **lat** - Latitude (Degrees)
- **lng** - Longitude (Degrees)
- **altitude** - Elevation Above Mean Sea Level
- **datum** - Coordinate system (Typically WGS84)
- **ok** - True or False if coordinates exists

## Functions

- **debug** - Generates a report of all the attributes available

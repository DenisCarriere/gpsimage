#!/usr/bin/python
# coding: utf8

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist --formats=gztar upload')
    sys.exit()

version = '0.0.1'
requires = []

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='gpsimage',
    version=version,
    description="Retrieves GPS data from Geo-referenced images made easy",
    long_description=readme,
    author='Denis Carriere',
    author_email='carriere.denis@gmail.com',
    url='https://github.com/DenisCarriere/gpsimage',
    download_url='https://github.com/DenisCarriere/gpsimage/tarball/master',
    license=license,
    packages=['gpsimage'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'gpsimage': 'gpsimage'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='gps image exif lat lng georeferenced geo',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)

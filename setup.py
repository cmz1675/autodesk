#!/usr/bin/env python

from setuptools import setup

setup(
    name='autodesk',
    version='1.0',
    packages=['autodesk', 'timer'],
    include_package_data=True,
    install_requires=['flask', 'RPi.GPIO', 'requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    scripts=['bin/cmd.py', 'bin/logger.py'],
    entry_points={'console_scripts': ['autodesk-timer=timer.timer:main']},
)
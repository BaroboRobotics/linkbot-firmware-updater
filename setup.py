#!/usr/bin/env python3

from setuptools import setup
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('linkbot_firmware_updater/linkbot_firmware_updater.py').read(),
    re.M
    ).group(1)

setup(
    name = "linkbot_firmware_updater",
    packages = ["linkbot_firmware_updater", ],
    version = version,
    entry_points = {
        "console_scripts": ['linkbot-firmware-updater=linkbot_firmware_updater.linkbot_firmware_updater:main']
    },
    install_requires = [
        "PyLinkbot >= 2.3.4", 
        "pystk500v2 >= 2.3.0",
        ],
    description = "Firmware Updating Tool for Barobo Linkbots.",
    zip_safe = False,
    include_package_data = True,
    author = "David Ko",
    author_email = "david@barobo.com",
    )


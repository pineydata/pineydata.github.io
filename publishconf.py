# This file is only used if you use `make publish` or explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Set SITEURL to your custom domain
SITEURL = 'https://www.pineydata.com'
RELATIVE_URLS = False

# Ensure static paths are included
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

# Theme settings
THEME = 'themes/piney'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']

TAILWIND_CSS = True
THEME_COLOR_PRIMARY = '#009477'
THEME_COLOR_SECONDARY = '#2fa1ba'

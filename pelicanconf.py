AUTHOR = 'Piney Data'
SITENAME = 'Piney Data'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output'

TIMEZONE = 'America/New_York'  # Adjust as needed

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/piney'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']

TAILWIND_CSS = True
THEME_COLOR_PRIMARY = '#2fa1ba'
THEME_COLOR_SECONDARY = '#009477'

# Page settings
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}'

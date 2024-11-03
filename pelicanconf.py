from zoneinfo import ZoneInfo
from datetime import datetime



AUTHOR = 'Kyle MacKenzie'
SITENAME = 'GenderFree SCD'
SITESUBTITLE = ''
SITEURL = ""

PATH = "src"

TIMEZONE = 'America/New_York'
TODAY = datetime.today().astimezone(ZoneInfo(TIMEZONE))


DEFAULT_LANG = 'en'

THEME = 'theme'
STYLESHEET_URL = '/theme/css/main.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
#    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DIRECT_TEMPLATES = (('index'),)

USE_FOLDER_AS_CATEGORY=True

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "{slug}/index.html"

ARTICLE_URL = 'events/{date:%Y}-{date:%b}-{date:%d}-{slug}/'
ARTICLE_SAVE_AS = "events/{date:%Y}-{date:%b}-{date:%d}-{slug}/index.html"

DEFAULT_DATE_FORMAT = "%A %m/%-d/%Y"

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

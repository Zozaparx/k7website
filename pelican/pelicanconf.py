AUTHOR = 'Zoe'
SITENAME = 'K7 Technosensible'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# DISPLAY_PAGES_ON_MENU = True   # Include pages in the menu
# DISPLAY_CATEGORIES_ON_MENU = True  # Include categories in the menu


# MENUITEMS = [
#     ('Présentation', '/content/pages/bio.md'),  # Example: Link to the homepage
#     ('Média ✨', '/content/pages/le-media.html'),  # Link to the About page
#     ('Lab 🧪', '/content/pages/le-lab.html'),  # Link to the About page
#     ('Studio 🪅', '/pages/about.html'),  # Link to the About page

# ]



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#images static generation
STATIC_PATHS = ['images', 'audio', 'extras/custom.css']

THEME = 'pelican-themes/notmyidea-cms'

EXTRA_PATH_METADATA = {
    'extras/custom.css': {'path': 'static/custom.css'}
}

CUSTOM_CSS = 'static/custom.css'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican_youtube']

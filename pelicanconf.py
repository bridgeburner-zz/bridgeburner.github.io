#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vishwath Mohan'
SITENAME = u'Vishwath Mohan'
SITESUBTITLE = u'Coffee, Security, AI, Armchair Philosophy'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'US/Central'
DEFAULT_LANG = u'en'

# Static Pages
STATIC_PATHS = ['images', 'assets', 'extras/CNAME']
EXTRA_PATH_METADATA = {'extras\\CNAME': {'path': 'CNAME'}, }

# Putting robots as a template page because we want to replace the SITEURL
TEMPLATE_PAGES = {'extras\\robots.txt': 'robots.txt'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Theme (Modified pelican-cait)
THEME = "theme"
CUSTOM_MENUITEMS = (('Blog', 'index.html'),
                    ('About Me', 'pages/about-me.html'))
USE_CUSTOM_MENU = True

# Plugins
PLUGIN_PATHS = ['..\\third_party\\pelican-plugins',]
PLUGINS = ['sitemap']

# The sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Fork on Github Ribbon
GITHUB_URL = 'https://github.com/bridgeburner/'

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/vishwath'),
          ('google-plus-sign', 'https://plus.google.com/+VishwathMohan'),
          ('github-alt', 'https://github.com/bridgeburner'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

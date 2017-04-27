#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Junshoong'
SITENAME = 'TIL'
SITEURL = 'http://til.junshoong.net'

OUTPUT_PATH = 'output'
PATH = 'content'

TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = "themes/simple-bootstrap"
DEFAULT_DATE_FORMAT = '%Y-%m-%d, %a'

# Url settings, remove '.html'
ARCHIVE_URL = '{archive}'
ARCHIVE_SAVE_AS = ARCHIVE_URL+'.html'

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL+'.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = PAGE_URL+'/index.html'

CATEGORY_URL = '{slug}/index'
CATEGORY_SAVE_AS = CATEGORY_URL+'.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = TAG_URL+'.html'

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = AUTHOR_URL+'.html'

LINKS = (('blog', 'http://blog.junshoong.net'),)

PLUGINS = [
    'pelican_gist',
]


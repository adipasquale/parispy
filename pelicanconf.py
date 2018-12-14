#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adrien Di Pasquale'
SITENAME = 'ParisPy Meetup'
# SITEURL = "http://localhost:8000"
SITETITLE = 'ParisPy Meetup'
SITELOGO = '/images/python-logo.png'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
  ('Groupe Meetup.com', 'https://www.meetup.com/Paris-py-Python-Django-friends'),
  ('Proposez un talk !', 'https://goo.gl/forms/RiuLdXUM0cckgUWo2'),
  ('Contact', 'https://www.meetup.com/fr-FR/messages/?new_convo=true'),
)

# Social widget

SOCIAL = (
  ('twitter', 'https://twitter.com/paris_py'),
)

DEFAULT_PAGINATION = False

THEME = "./theme"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SUMMARY_MAX_LENGTH = None

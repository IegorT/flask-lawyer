# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#secure
CSRF_ENABLED = True
SECRET_KEY = b""

# available languages
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'ru': 'Russian',
    'uk': 'Ukrainian'
}
BABEL_DEFAULT_LOCALE = 'en'

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''

# administrator list
ADMINS = ['', '']


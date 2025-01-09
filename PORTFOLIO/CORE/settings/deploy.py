# ruff: noqa: F403

from os import getenv

import dj_database_url

from CORE.settings.base import *


DATABASES = {'default': dj_database_url.parse(str(getenv('DATABASE_URL')))}

DEBUG = False
SECRET_KEY = getenv('SECRET_KEY')
ALLOWED_HOSTS = str(getenv('ALLOWED_HOSTS')).split(',')


# HTTP -> HTTPS redirect
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

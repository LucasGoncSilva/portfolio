import environ

from PORTFOLIO.settings.base import *


env = environ.Env()


DATABASES = {}


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

from os import environ

from PORTFOLIO.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': environ['DB_USER'],
        'NAME': environ['DB_NAME'],
        'PASSWORD': environ['DB_PASSWORD'],
        'HOST': environ['DB_HOST'],
        'PORT': '5432',
    }
}

DEBUG = environ['DEBUG']
ALLOWED_HOSTS = environ['ALLOWED_HOSTS'].split(',')
SECRET_KEY = environ['SECRET_KEY']


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

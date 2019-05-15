# -*- encoding:utf-8 -*-
"""
    Application local settings:
        - database
        - server connections
"""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5k@dbpq_3+t7g+ylt5h1*ox79lnwp-qijry3y60^1r_9q*m5b('

##
#   Database setup
##
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Add 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mainApp',                      # Or path to database file if using sqlite3.
        'USER': 'user',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

##
# Email setup
##
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

##
#   Update config array with these values
##
UPDATE_CONFIGS = [
]

UPDATE_CONFIGS = [
    #('CACHES', 'default', 'LOCATION', '/var/run/memcached/memcached.sock'),
    ('CACHES', 'default', 'KEY_PREFIX', 'mainApp:'),

    ('AUTH_CLIENT_ID','mainApp'),
    ('AUTH_CLIENT_SECRET',''),
    ('AUTH_SSO_LOCALE', 'cs'),
    ('AUTH_AVAIL_IDP',('pirati','facebook',)),   # tuple
]

LOG_INCOMING_REQUESTS = False

DEBUG=False
DEBUG_LOCAL=False



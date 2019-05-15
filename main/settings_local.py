# -*- encoding:utf-8 -*-
"""
    Application local settings:
        - database
        - server connections
"""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iQP-5=I(\<._9EMRHC;[4z?SHQ{5OZW;S*0FJKMuxsRuXSHQ{5OZW;S*0FJKMuxsRuXi2H~a'

##
#   Domain setup
#
HTTP_PROTOCOL = 'https'
BASE_SUBDOMAIN = "app" + "."
BASE_DOMAIN = "kouzelnakrabicka.cz"


##
#   Database setup
##
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'piratieuweb',
        'USER': 'piratieuweb',
        'PASSWORD': '',
        'HOST': '',          # Set to empty string for localhost.
        'PORT': '',          # Set to empty string for default.
    }
}

##
# Email setup
##
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
#DEFAULT_FROM_EMAIL = "martin.rejman@kouzelnakrabicka.cz"  # if you don't already have this in settings


##
#   Update config array with these values
##
UPDATE_CONFIGS = [
    #('CACHES', 'default', 'LOCATION', '/var/run/memcached/memcached.sock'),

    ('HTTP_PROTOCOL', 'http'),
    ('BASE_SUBDOMAIN', ''),
    ('BASE_DOMAIN', '127.0.0.1'),
    ('BASE_PORT', '8019'),

]

LOG_INCOMING_REQUESTS = False

DEBUG=True
DEBUG_LOCAL=True



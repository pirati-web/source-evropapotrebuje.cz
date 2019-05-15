# -*- encoding:utf-8 -*-
"""
    Main settings file for one domain.

    Domain: .CZ
"""

import os

from .settings_global import *
from .settings_local import *

##
#   Load ENV variables with prefix NALODENI_ to UPDATE_CONFIGS
#
#   Docker deployment needs setting to be supplied externally.
#
#   ENV_APPROVED_UPDATES contains known variables we can set,
#   the tuple contains "path" to the setting.
ENV_APPROVED_UPDATES = {
    'AUTH_SERVER' : ('AUTH_SERVER',),
    'AUTH_CLIENT_ID' : ('AUTH_CLIENT_ID',),
    'AUTH_CLIENT_SECRET' : ('AUTH_CLIENT_SECRET',),
    'AUTH_AVAIL_IDP' : ('AUTH_AVAIL_IDP',),

    'HTTP_PROTOCOL' : ('HTTP_PROTOCOL',),
    'BASE_DOMAIN' : ('BASE_DOMAIN',),
    'BASE_SUBDOMAIN' : ('BASE_SUBDOMAIN',),
    'BASE_PORT' : ('BASE_PORT',),

    'PSQL_USER' : ('DATABASES','default','USER'),
    'PSQL_PASSWORD' : ('DATABASES','default','PASSWORD'),
    'PSQL_DBNAME' : ('DATABASES','default','NAME'),
    'PSQL_HOST' : ('DATABASES','default','HOST'),
    'PSQL_PORT' : ('DATABASES','default','PORT'),

    'APP_REG_LIMIT_HARD' : ('APP_REG_LIMIT_HARD', ),
    'APP_REG_LIMIT_SOFT' : ('APP_REG_LIMIT_SOFT', ),
    'TOKEN_VALID_SEC' : ('TOKEN_VALID_SEC', ),

    'EMAIL_BACKEND' : ('EMAIL_BACKEND',),
    'EMAIL_HOST' : ('EMAIL_HOST',),
    'EMAIL_PORT' : ('EMAIL_PORT',),
    'EMAIL_HOST_USER' : ('EMAIL_HOST_USER',),
    'EMAIL_HOST_PASSWORD' : ('EMAIL_HOST_PASSWORD',),
    'EMAIL_USE_TLS' : ('EMAIL_USE_TLS',),
    'EMAIL_USE_SSL' : ('EMAIL_USE_SSL',),
    'EMAIL_SSL_CERTFILE' : ('EMAIL_SSL_CERTFILE',),
    'EMAIL_SSL_KEYFILE' : ('EMAIL_SSL_KEYFILE',),

    'DEBUG' : ('DEBUG',),
    'DEBUG_LOCAL' : ('DEBUG_LOCAL',),
}
for evk in os.environ:
    if evk[0:9] == "NALODENI_":
        var_key = evk[9:]
        if var_key in ENV_APPROVED_UPDATES:
            val_type = os.environ[evk][0:2]
            val = str(os.environ[evk][2:])

            if val_type == "s-":
                val = (val, )           # tuple
            elif val_type == "b-":
                val = (val == 'on', )   # tuple
            elif val_type == "a-":
                # nested tuple, one gets eaten by + operator
                val = ( tuple(val.split(',')) ,)
            else:
                print("Wrong ENV value for '%s', skipping" % evk)
                continue

            if val == "":
                val = (None, )
                
            UPDATE_CONFIGS.append( ENV_APPROVED_UPDATES[var_key] + val )

##
#   Update configs from settings_local.UPDATE_CONFIGS
#
#   Each item is a list-like path to the setting to be
#   updated, the last value of the list is the value of
#   the setting updated. E.g.:
#       ('CACHES', 'default', 'KEY_PREFIX', 'cz:'),
#   is the same as
#       CACHES['default']['KEY_PREFIX'] = 'cz:'
#   written directly in the settings file.
#
#   Use array references to update the existing array.
#   [:-2] used to preserve the last array-like link, so
#   we can update the value there, and not the local variable.
for item in UPDATE_CONFIGS:
    p = vars()
    for i in item[:-2]:
        if not i in p:
            p[i] = {}
        p = p[i]
    p[item[-2]]=item[-1]

#
##


##                              ##
#   DO NOT EDIT BELOW !!!        #
##                              ##

##
#   SECURITY - do not change.
##
#CSRF_USE_SESSIONS = False
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = (HTTP_PROTOCOL == 'https')    # fix to HTTPS when available
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = (HTTP_PROTOCOL == 'https') # fix to HTTPS when available
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', HTTP_PROTOCOL)

##
#   Domain setup
##
BASE_URL = HTTP_PROTOCOL + '://' + BASE_SUBDOMAIN + BASE_DOMAIN + ((':' + BASE_PORT) if BASE_PORT != "" else "")
SESSION_COOKIE_DOMAIN= BASE_SUBDOMAIN + BASE_DOMAIN
CSRF_COOKIE_DOMAIN=BASE_SUBDOMAIN + BASE_DOMAIN
CSRF_TRUSTED_ORIGINS = [ SESSION_COOKIE_DOMAIN , ]
ALLOWED_HOSTS =        [ BASE_SUBDOMAIN + BASE_DOMAIN, ]

##
# Internationalization, https://docs.djangoproject.com/en/1.11/topics/i18n/
##
LANGUAGE_CODE = 'cs'
TIME_ZONE = 'Europe/Prague'


##
#   Logger config
##
LOG_FILES = os.path.join(BASE_DIR, 'log_files')
LOG_INCOMING_REQUESTS_FILE = os.path.join(
        LOG_FILES, 'incoming_requests_%s.log' % BASE_DOMAIN 
        )

##
#   Media files path setup
##
MEDIA_ROOT = os.path.join(BASE_DIR,'media_files')

##
#   Debugging settings
##
if DEBUG_LOCAL:
    ALLOWED_HOSTS += [
            'localhost',
            ]

    CSRF_COOKIE_DOMAIN = "localhost"
    SESSION_COOKIE_DOMAIN= CSRF_COOKIE_DOMAIN


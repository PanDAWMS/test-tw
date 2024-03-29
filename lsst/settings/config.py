
from os.path import dirname, join

import core
import lsst

#from local import defaultDatabase, MY_SECRET_KEY
from local import dbaccess, MY_SECRET_KEY

### VIRTUALENV
#VIRTUALENV_PATH = '/data/virtualenv/django1.6.1__python2.6.6'
#VIRTUALENV_PATH = '/data/virtualenv/django1.6.1__python2.6.6__lsst'
#VIRTUALENV_PATH = '/data/wenaus/virtualenv/twdev__django1.6.1__python2.6.6__lsst'
VIRTUALENV_PATH = '/data/wenaus/virtualenv/twrpm'

### WSGI
WSGI_PATH = VIRTUALENV_PATH + '/pythonpath'


STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(dirname(core.common.__file__), 'static'),
#    join(dirname(lsst.__file__), 'static'),
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(dirname(core.common.__file__), 'templates'),
    join(dirname(lsst.__file__), 'templates'),
)

STATIC_ROOT = join(dirname(lsst.__file__), 'static')
#STATIC_ROOT = None
MEDIA_ROOT = join(dirname(lsst.__file__), 'media')
STATIC_URL_BASE = '/static/'
MEDIA_URL_BASE = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = MY_SECRET_KEY

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# DATABASES = {
# #    'default': {
# #        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
# #        'NAME': '',                      # Or path to database file if using sqlite3.
# #        'USER': '',                      # Not used with sqlite3.
# #        'PASSWORD': '',                  # Not used with sqlite3.
# #        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
# #        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
# #    }
#     'default': defaultDatabase
# }
DATABASES = dbaccess

### URL_PATH_PREFIX for multi-developer apache/wsgi instance
### on EC2: URL_PATH_PREFIX = '/bigpandamon' or URL_PATH_PREFIX = '/developersprefix'
#URL_PATH_PREFIX = '/lsst'
#URL_PATH_PREFIX = '/twrpmlsst'
URL_PATH_PREFIX = '/lsst'
#URL_PATH_PREFIX = ''
### on localhost:8000: URL_PATH_PREFIX = '/.'
#URL_PATH_PREFIX = ''
MEDIA_URL = URL_PATH_PREFIX + MEDIA_URL_BASE
STATIC_URL = URL_PATH_PREFIX + STATIC_URL_BASE


#LOG_ROOT = '/data/bigpandamon_virtualhosts/lsst/logs'
#LOG_ROOT = '/data/wenaus/logs'
LOG_ROOT = '/data/wenaus/bigpandamon_virtualhosts/twrpm/logs'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
#    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile-bigpandamon': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/logfile.bigpandamon",
            'maxBytes': 1000000000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'logfile-django': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/logfile.django",
            'maxBytes': 1000000000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'logfile-viewdatatables': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/logfile.viewdatatables",
            'maxBytes': 1000000000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'logfile-rest': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/logfile.rest",
            'maxBytes': 1000000000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler'
            'class':'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
#            'level': 'ERROR',
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers':['logfile-django'],
            'propagate': True,
            'level':'DEBUG',
        },
        'django_datatables_view': {
            'handlers':['logfile-viewdatatables'],
            'propagate': True,
            'level':'DEBUG',
        },
        'rest_framework': {
            'handlers':['logfile-rest'],
            'propagate': True,
            'level':'DEBUG',
        },
        'bigpandamon': {
            'handlers': ['logfile-bigpandamon'],
            'level': 'DEBUG',
        },
    },
    'formatters': {
        'verbose': {
#            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            'format': '%(asctime)s %(module)s %(name)-12s:%(lineno)d %(levelname)-5s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(name)-12s:%(lineno)d %(message)s'
        },
    },
    'logfile': {
        'level':'DEBUG',
        'class':'logging.handlers.RotatingFileHandler',
        'filename': LOG_ROOT + "/logfile",
        'maxBytes': 10000000,
        'backupCount': 5,
        'formatter': 'verbose',
    },
}

ENV = {
    ### Application name
    'APP_NAME': "PanDA Monitor", \
    ### Page title default
    'PAGE_TITLE': "PanDA Monitor", \
    ### Menu item separator
    'SEPARATOR_MENU_ITEM': "&nbsp;&nbsp;&nbsp;", \
    ### Navigation chain item separator
    'SEPARATOR_NAVIGATION_ITEM': "&nbsp;&#187;&nbsp;" , \
}


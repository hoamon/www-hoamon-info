# Django settings for trunk project.
import os, sys
TRUNK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TRUNK)
sys.path.insert(0, os.path.join(TRUNK, 'modules'))

TRUNK_PARENT = os.path.dirname(TRUNK)
sys.path.insert(0, TRUNK_PARENT)

# use the below to set up third party libraries
#sys.path.insert(0, os.path.join(os.path.dirname(TRUNK), 'asset', 'SOME-LIB-DIR'))

if (os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or
    os.getenv('SETTINGS_MODE') == 'prod'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'INSTANCE': 'ho600:test',
            'NAME': 'ho600',                      # Or path to database file if using sqlite3.
        }
    }
else:
    # Running in development, so use a local MySQL database.
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'ho600',
            'PASSWORD': 'ho600',
            'HOST': 'localhost',
            'NAME': 'ho600',
            'OPTIONS': {
               'init_command': 'SET storage_engine=INNODB',
            }
        }
    }

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Taipei'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-tw'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$6*g!0&amp;0n$972d&amp;$zq4y*vf^^v=y)($p88bmj4vf$67pqbjrc2'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


sys.path.insert(0, os.path.join(TRUNK_PARENT, 'asset', 'django-mediagenerator'))
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mediagenerator.middleware.MediaMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'ho600_lib',

    'mediagenerator', # must be last
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'filters': [],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# mediagenerator
MEDIA_DEV_MODE = DEBUG
DEV_MEDIA_URL = '/mediagenerator/'
PRODUCTION_MEDIA_URL = '/production_mediagenerator/'
# *********************************************************** <
# YOU should put TRUNK/media into TRUNK/for_mediagenerator/   <
GLOBAL_MEDIA_DIRS = (os.path.join(TRUNK, 'for_mediagenerator'), )
# YOU should put TRUNK/media into TRUNK/for_mediagenerator/   >
# *********************************************************** >

MEDIA_GENERATORS = (
    'mediagenerator.generators.copyfiles.CopyFiles',
    'mediagenerator.generators.bundles.Bundles',
    #'mediagenerator.generators.manifest.Manifest',
)
COPY_MEDIA_FILETYPES = ('gif', 'jpg', 'jpeg', 'png', 'svg', 'svgz',
                                     'ico', 'swf', 'ttf', 'otf', 'eot')
IGNORE_APP_MEDIA_DIRS = ('django.contrib.admin', )
MEDIA_BUNDLES = (
    # put {% include_media "bundle.css" %} in template.html
    ('bundle.css',
        'media/root.css',
    ),

    # put {% include_media "bundle.js" %} in template.html
    ('bundle.js',
        'media/root.js',
    ),
)

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.yuicompressor.YUICompressor',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

YUICOMPRESSOR_PATH = os.path.join(TRUNK_PARENT, 'asset', 'yuicompressor-2.4.7.jar')



class NonSetError(Exception): pass



import local_settings

for v in dir(local_settings):
    if len(v) >= 2 and v[:2] != '__':
        if not locals().has_key(v):
            raise NonSetError('Please set the variable "%s" in settings.py first!' % v)
        else:
            if DEBUG:
                print('Upload settings.%s to %s' % (v, getattr(local_settings, v)))
from local_settings import *

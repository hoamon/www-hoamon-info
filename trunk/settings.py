# Django settings for trunk project.

import os, sys


def _insert_sys_path(index, path):
    """ insert "path" to sys.path if "path" not in sys.path
    """
    if path not in sys.path:
        sys.path.insert(index, path)


TRUNK = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TRUNK)
_insert_sys_path(0, os.path.join(TRUNK, 'depends_modules'))
_insert_sys_path(0, os.path.join(TRUNK, 'modules'))
_insert_sys_path(0, TRUNK)
TRUNK_PARENT = os.path.dirname(TRUNK)
_insert_sys_path(0, TRUNK_PARENT)

# use the below to set up third party libraries
#_insert_sys_path(0, os.path.join(os.path.dirname(TRUNK), 'asset', 'SOME-LIB-DIR'))


if os.environ.get('APPLICATION_ID', ''):
    SDK_MODE = 'appengine'
else:
    SDK_MODE = 'puredjango'


if (os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or
    os.getenv('SETTINGS_MODE') == 'gae_production'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'INSTANCE': 'ho600.com:ho600-com:ho600-com',
            'NAME': 'ho600',                      # Or path to database file if using sqlite3.
        }
    }
elif (os.environ.get('UWSGI_ORIGINAL_PROC_NAME', None) or
    os.environ.get('APACHE_PID_FILE', None)):
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'ho600_production',
            'PASSWORD': 'ho600_production',
            'HOST': 'localhost',
            'NAME': 'ho600_production',
            'OPTIONS': {
               'init_command': 'SET storage_engine=INNODB',
            }
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


TEMPLATE_CONTEXT_PROCESSORS =  (
    'django.contrib.auth.context_processors.auth',
    'ho600_lib.context_processors.settings',
)


_insert_sys_path(0, os.path.join(TRUNK_PARENT, 'asset', 'django-debug-toolbar'))
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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

_insert_sys_path(0, os.path.join(TRUNK_PARENT, 'asset', 'mimeparse-0.1.3')) # needed by django-tastypie
_insert_sys_path(0, os.path.join(TRUNK_PARENT, 'asset', 'python-dateutil-1.5')) # needed by django-tastypie
_insert_sys_path(0, os.path.join(TRUNK_PARENT, 'asset', 'django-tastypie'))
# and Optional modules:
# python_digest (https://bitbucket.org/akoha/python-digest/)
# lxml (http://lxml.de/) if using the XML serializer
# pyyaml (http://pyyaml.org/) if using the YAML serializer
# biplist (http://explorapp.com/biplist/) if using the binary plist serializer


# the modules were needed by INSTALLED_APPS
ANOTHER_DEPENDS_MODULES = (
    'mimeparse',
    'dateutil',
)


_insert_sys_path(0, os.path.join(TRUNK_PARENT, 'asset', 'django-guardian'))
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)
ANONYMOUS_USER_ID = -1


_insert_sys_path(0, os.path.join(TRUNK_PARENT, 'asset', 'django-mediagenerator'))
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
    'tastypie',
    'guardian',
    'ho600_lib',

    'debug_toolbar',
    'mediagenerator', # must be last
)


INTERNAL_IPS = ('127.0.0.1', '192.168.1.1', '192.168.1.2', '192.168.1.254', )
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
def custom_show_toolbar(request):
    if request.META.get('REMOTE_ADDR') in INTERNAL_IPS:
        return DEBUG  # Always show toolbar, for example purposes only.
    else:
        return False
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    'EXTRA_SIGNALS': [],
    'HIDE_DJANGO_SQL': False,
    'TAG': 'div',
    'ENABLE_STACKTRACES' : True,
}

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


# django-tastypie >>>
API_LIMIT_PER_PAGE = 25
TASTYPIE_FULL_DEBUG = DEBUG
# <<< django-tastypie


# mediagenerator >>>
MEDIA_DEV_MODE = DEBUG
DEV_MEDIA_URL = '/mediagenerator/'
PRODUCTION_MEDIA_URL = '/production_mediagenerator/'
GLOBAL_MEDIA_DIRS = (os.path.join(TRUNK, 'media'),
                        os.path.join(TRUNK, 'modules'),
                        #ROOT,  # if you run in GAE mode, this ROOT directory will raise a IOError on ./trunk/_generate_media .
                                # for example: the media file laies on ./my_module/media/xxx.js , 
                                # you should use os.path.join(ROOT, 'my_module', 'media') here and
                                # ('bundle_xxx.js',
                                #   'xxx.js'),
                                # in MEDIA_BUNDLES.
                        )


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
    ('jquery.css',
        'jquery.css',
    ),

    # put {% include_media "bundle.js" %} in template.html
    ('jquery.js',
        'jquery.js',
        'jqueryui.js',
    ),
)

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.yuicompressor.YUICompressor',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

YUICOMPRESSOR_PATH = os.path.join(TRUNK_PARENT, 'asset', 'yuicompressor-2.4.7.jar')
# <<< mediagenerator



class NonSetError(Exception):
    """ Any variable in local_settings.py should be set in settings.py first.
        If not, the raise this Error.
    """
    pass



# load another settings and local_settings of other modules >>>
try:
    import local_settings
except ImportError:
    pass
else:
    for v in dir(local_settings):
        if len(v) >= 2 and v[:2] != '__':
            if not locals().has_key(v):
                raise NonSetError('Please set the variable "%s" in settings.py first!' % v)
            else:
                if DEBUG:
                    print('Upload settings.%s to %s' % (v, getattr(local_settings, v)))
    from local_settings import *


for app in INSTALLED_APPS:
    try:
        app_settings = __import__('.'.join([app, 'settings']))
    except ImportError:
        continue
    else:
        for v in dir(app_settings):
            if len(v) >= 2 and v[:2] != '__':
                globals()[v] = getattr(app_settings, v)

    try:
        local_app_settings = __import__('.'.join([app, 'local_settings']))
    except ImportError:
        continue
    else:
        for v in dir(local_app_settings):
            if len(v) >= 2 and v[:2] != '__' and hasattr(app_settings, v):
                globals()[v] = getattr(local_app_settings, v)
# <<< load another settings and local_settings of other modules

# Django settings for trunk project.

import os, sys, datetime
from os.path import join


class LoadAfterAppSettings(object):
    """ put any variables and values in this class.VARS then the variables will be loaded in the end of settings.py,
        but before import turnk_local_settings.*

        the settings.* loading order:

            original trunk/settings.*
            >> every settings.* in INSTALLED_APPS
            >> original trunk/settings.LoadAfterAppSettings.VARS
            >> trunk/turnk_local_settings.*
    """
    VARS = {}



def _insert_sys_path(index, path):
    """ insert "path" to sys.path if "path" not in sys.path
    """
    if path not in sys.path:
        sys.path.insert(index, path)


TRUNK = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TRUNK)
_insert_sys_path(0, join(TRUNK, 'depends_modules'))
_insert_sys_path(0, join(TRUNK, 'modules'))
_insert_sys_path(0, TRUNK)
TRUNK_PARENT = os.path.dirname(TRUNK)
_insert_sys_path(0, TRUNK_PARENT)

for d in os.listdir(join(TRUNK, 'depends_modules')):
    _insert_sys_path(0, join(TRUNK, 'depends_modules', d))

# use the below to set up third party libraries
#_insert_sys_path(0, join(os.path.dirname(TRUNK), 'asset', 'SOME-LIB-DIR'))

# the modules were needed by INSTALLED_APPS
# for bin/before_deployment.py
ANOTHER_DEPENDS_MODULES = []

if os.environ.get('APPLICATION_ID', ''):
    _insert_sys_path(0, join(os.path.dirname(TRUNK), 'asset', 'django-gae-backends'))
    SDK_MODE = 'appengine'
    EMAIL_BACKEND = "gae_backends.mail.EmailBackend"
    MEMCACHE = {
        'BACKEND': 'gae_backends.memcache.MemcacheCache',
    }
else:
    SDK_MODE = 'puredjango'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    MEMCACHE = {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }


try:
    import trunk_local_settings
except ImportError:
    DATABASES = False
else:
    if hasattr(trunk_local_settings, 'DATABASES') and trunk_local_settings.DATABASES:
        DATABASES = trunk_local_settings.DATABASES
    else:
        DATABASES = False


if ((os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or
    os.getenv('SETTINGS_MODE') == 'gae_production')):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DEBUG = False
    if not DATABASES:
        DATABASES = {
            'default': {
                'ENGINE': 'google.appengine.ext.django.backends.rdbms', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
                'INSTANCE': 'ho600.com:ho600-com:ho600-com',
                'NAME': 'ho600',                      # Or path to database file if using sqlite3.
                }
            }
elif ((os.environ.get('UWSGI_ORIGINAL_PROC_NAME', None)
        #INFO: if UWSGI_DEB_CONFNAME = 'tho600', the MODE still is DEBUG(but only with nginx+uwsgi)
        and os.environ.get('UWSGI_DEB_CONFNAME', 'tho600') != 'tho600')
    or os.environ.get('AP_PARENT_PID', None)
    or os.getenv('SETTINGS_MODE') == 'production'):
    #INFO: If You are running in the windows dos enviroment,
    # and want to syncdb to the ho600_prod.
    # Please do the below line in the dos before syncdb
    # d:\> set SETTINGS_MODE=production
    DEBUG = False
    if not DATABASES:
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
else:
    # Running in development, so use a local MySQL database.
    DEBUG = True
    if not DATABASES:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'USER': 'test_ho600',
                'PASSWORD': 'test_ho600',
                'HOST': 'localhost',
                'NAME': 'test_ho600',
                'OPTIONS': {
                    'init_command': 'SET storage_engine=INNODB',
                    }
                }
            }


try:
    import trunk_local_settings
except ImportError:
    pass
else:
    if hasattr(trunk_local_settings, 'DEBUG'):
        DEBUG = trunk_local_settings.DEBUG

def uwsgi_print(s):
    if DEBUG: print(' <<< Print >>> %s' % (s))


TEMPLATE_DEBUG = DEBUG

DEVELOPER_DOCS_PATH = os.path.join(TRUNK, '..', 'docs', '_build', 'html')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'default_trunk_cache',
    },
    'COMPRESSOR_CACHE': MEMCACHE,
}


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'ja-jp'

LANGUAGES = (
    ('ja-jp', u'\u65e5\u672c\u8a9e(Japanese)'),
    ('en-us', 'English(United States)'),
    ('zh-tw', u'\u6b63\u9ad4\u4e2d\u6587(Taiwan, R.O.C.)'),
    ('zh-cn', u'\u7b80\u4f53\u4e2d\u6587(Mainland China)'),
)

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
STATIC_ROOT = join(TRUNK, 'staticsite')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    join(TRUNK, 'static'),
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
    'compressor.finders.CompressorFinder',
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
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)


_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'django-debug-toolbar'))
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware', # for i18n multi-languages
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'mediagenerator.middleware.MediaMiddleware',
    # and please set a INTERNAL_IPS variable, like INTERNAL_IPS = ('127.0.0.1', '1.2.3.4',)
    'ho600_lib.middleware.Handle500Middleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    join(TRUNK, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'mimeparse-0.1.3')) # needed by django-tastypie
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'python-dateutil-1.5')) # needed by django-tastypie
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'rose')) # needed by django-tastypie
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'defusedxml')) # needed by django-tastypie with xml format
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'django-tastypie'))
# the modules were needed by INSTALLED_APPS
# for bin/before_deployment.py
ANOTHER_DEPENDS_MODULES += [
    'mimeparse',
    'dateutil',
    'rose',
    'defusedxml',
]

# and Optional modules:
# python_digest (https://bitbucket.org/akoha/python-digest/)
# lxml (http://lxml.de/) if using the XML serializer
# pyyaml (http://pyyaml.org/) if using the YAML serializer
# biplist (http://explorapp.com/biplist/) if using the binary plist serializer


_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'django-guardian'))
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)
ANONYMOUS_USER_ID = -1


_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'django_compressor'))
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'versiontools')) # needed by django_compressor
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'django-appconf')) # needed by django_compressor
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'six')) # needed by django-appconf
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'BeautifulSoup')) # optional needed by django_compressor+lxml
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'html5lib', 'python')) # optional needed by django_compressor
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'slimit', 'src')) # optional needed by django_compressor
# the modules were needed by INSTALLED_APPS
# for bin/before_deployment.py
ANOTHER_DEPENDS_MODULES += [
    'six',
    'BeautifulSoup',
    'html5lib',
    'slimit',
]


_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'httplib2', 'python2'))
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'python-openid'))
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'python-oauth2'))
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'django-social-auth'))
# the modules were needed by INSTALLED_APPS
# for bin/before_deployment.py
ANOTHER_DEPENDS_MODULES += [
    'httplib2',
    'openid',
    'oauth2',
]


_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'pyasn1', 'pyasn1-0.1.6'))
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'python-rsa'))
_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'ho600-django-gae-federated-auth'))
# the modules were needed by INSTALLED_APPS
# for bin/before_deployment.py
ANOTHER_DEPENDS_MODULES += [
    'pyasn1',
    'rsa',
]

_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'django-mediagenerator'))

_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'pytz-2013b', 'pytz-2013b'))
ANOTHER_DEPENDS_MODULES += [
    'pytz',
]

_insert_sys_path(0, join(TRUNK_PARENT, 'asset', 'suds-0.4', 'suds-0.4'))
ANOTHER_DEPENDS_MODULES += [
    'suds',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.humanize',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'django_extensions', # only for generate model graph
    'tastypie',
    'guardian',
    'ho600_lib',

    'social_auth',
    'federated_auth',

    'debug_toolbar',    # if you don't want this app, then change "DEBUG_TOOLBAR_CONFIG"(likes below)
                        # in your local_settings.py.
                        #DEBUG_TOOLBAR_CONFIG = {
                        #    'INTERCEPT_REDIRECTS': False,
                        #    'SHOW_TOOLBAR_CALLBACK': lambda R: False,
                        #    'EXTRA_SIGNALS': [],
                        #    'HIDE_DJANGO_SQL': False,
                        #    'TAG': 'div',
                        #    'ENABLE_STACKTRACES' : True,
                        #}

    'appconf',
    'versiontools',
    'compressor',

    'mediagenerator', # must be last
]

# ho600-django-gae-federated-auth <<<
LoadAfterAppSettings.VARS['LOGIN'] = '/federated_auth/'
LoadAfterAppSettings.VARS['SOCIAL_AUTH_LOGIN_REDIRECT_URL'] = '/federated_auth/log_ip/'
LoadAfterAppSettings.VARS['SOCIAL_AUTH_NEW_USER_REDIRECT_URL'] = '/federated_auth/'
LoadAfterAppSettings.VARS['SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL'] = '/federated_auth/'
LoadAfterAppSettings.VARS['SOCIAL_AUTH_DISCONNECT_REDIRECT_URL'] = '/federated_auth/'
# >>> ho600-django-gae-federated-auth


# django-debug_toolbar <<<
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
# >>> django-debug_toolbar

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

# django-compressor >>>
COMPRESS_ENABLED = not DEBUG
# This two variables(COMPRESS_OFFLINE, COMPRESS_OFFLINE_MANIFEST)
# **did not** use in runserver or Nginx/Apache, it will be failured.
#COMPRESS_OFFLINE = not DEBUG
#COMPRESS_OFFLINE_MANIFEST = join(TRUNK, 'compressor-static', 'manifest.json')
COMPRESS_CACHE_BACKEND = 'COMPRESSOR_CACHE'
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = join(TRUNK, 'compressor-static')
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.yui.YUICSSFilter',
                        'compressor.filters.cssmin.CSSMinFilter']
if sys.platform.startswith('linux'):
    COMPRESS_PRECOMPILERS = ( ('text/x-scss', '/usr/local/bin/scss {infile} {outfile}'),)
else:
    COMPRESS_PRECOMPILERS = ( ('text/x-scss', 'scss {infile} {outfile}'),)
COMPRESS_YUI_BINARY = 'java -jar %s' % join(ROOT, 'asset', 'yuicompressor-2.4.7.jar')
if DEBUG:
    SV_ = STATIC_VERSION = lambda: '?v=%s' % datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f')
else:
    SV_ = STATIC_VERSION = ''
# <<< django-compressor


# mediagenerator >>>
MEDIA_DEV_MODE = DEBUG
DEV_MEDIA_URL = '/mediagenerator/'
PRODUCTION_MEDIA_URL = '/production_mediagenerator/'
GENERATED_MEDIA_DIR = join(TRUNK, 'mediagenerator-static')
GLOBAL_MEDIA_DIRS = (join(TRUNK, 'static'),
                        join(TRUNK, 'modules'),
                        join(TRUNK, 'depends_modules'),
                        #ROOT,  # if you run in GAE mode,
                                # this ROOT directory will raise a IOError on ./trunk/_generate_media .
                                # for example: the media file laies on ./my_module/media/xxx.js ,
                                # you should use join(ROOT, 'my_module', 'media') here and
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
MEDIA_BUNDLES = [
    # put {% include_media "bundle.css" %} in template.html
    ('jquery.css',
        'jquery.css',
    ),

    # put {% include_media "bundle.js" %} in template.html
    ('jquery.js',
        'jquery.js',
        'jqueryui.js',
    ),
]

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.yuicompressor.YUICompressor',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

YUICOMPRESSOR_PATH = join(TRUNK_PARENT, 'asset', 'yuicompressor-2.4.7.jar')
# <<< mediagenerator


if DEBUG:
    SV_ = STATIC_VERSION = lambda: '?v=%s' % datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f')
else:
    SV_ = STATIC_VERSION = ''


# load another settings and local_settings of other modules >>>
# load INSTALLED_APPS.settings first and check any variables in INSTALLED_APPS.local_settings
# if the variables set in INSTALLED_APPS.settings then replace value of INSTALLED_APPS.settings
# in the last, load all variables were set before in ROOT/trunk_local_settings.py.
for app in INSTALLED_APPS:
    try:
        app_settings = __import__('.'.join([app, 'settings']))
    except ImportError:
        pass
    else:
        try:
            local_settings = __import__('.'.join([app, 'local_settings']))
        except ImportError:
            local_settings = False
        for a in app.split('.')[1:]:
            app_settings = getattr(app_settings, a)
        app_settings = app_settings.settings
        if local_settings:
            for a in app.split('.')[1:]:
                local_settings = getattr(local_settings, a)
            local_settings = local_settings.local_settings
        for v in dir(app_settings):

            if local_settings and hasattr(local_settings, v):
                setattr(app_settings, v,
                    getattr(local_settings, v))

            if len(v) >= 2 and v[:2] != '__':
                if v != 'MEDIA_BUNDLES':
                    locals()[v] = getattr(app_settings, v)
                elif hasattr(app_settings, 'MEDIA_BUNDLES'):
                    for mb in getattr(app_settings, 'MEDIA_BUNDLES'):
                        ori = [l[0] for l in MEDIA_BUNDLES]
                        if mb[0] not in ori:
                            MEDIA_BUNDLES.append(mb)


for k, v in LoadAfterAppSettings.VARS.items():
    locals()[k] = v


try:
    import trunk_local_settings
except ImportError:
    pass
else:
    for k in dir(trunk_local_settings):
        if (len(k) == 1 and k != '_') or (len(k) >= 2 and k[:2] != '__'):
            if k == 'DATABASES':
                continue
            elif not locals().has_key(k):
                #raise NonSetError('***Please set the variable "%s" in settings.py or INSTALLED_APPS/settings.py first!!!' % k)
                if DEBUG:
                    uwsgi_print('Please set the variable "%s" in settings.py or INSTALLED_APPS/settings.py first!!!' % k)
                continue

            if DEBUG:
                uwsgi_print('Update settings.%s to %s' % (k, getattr(trunk_local_settings, k)))
            locals()[k] = getattr(trunk_local_settings, k)

# <<< load another settings and trunk_local_settings of other modules

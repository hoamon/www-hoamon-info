"""
WSGI config for hoamon_info project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

try: from wsgi_settings import SHOW_PRINT
except ImportError: SHOW_PRINT = False

def uwsgi_print(s):
    """ In Linux OS, we can monitor uwsgi log with the below command:

        tail -f ttainan.log | grep '\(\( <<< Print >>> \)\|\(GET\|POST\|PUT\|DELETE\)\| spawned uWSGI master \)'

            <<< Print >>> => display message from this function(uwsgi_print)

            GET|POST|PUT|DELETE => display single connection between browser and uwsgi server

            spawned uWSGI master => display uwsgi server restart log
    """
    if SHOW_PRINT:
        print(' <<< Print >>> %s' % s)

try:
    import uwsgi
except ImportError:
    if SHOW_PRINT:
        uwsgi_print('import uwsgi error')
else:
    from uwsgidecorators import timer
    from django.utils import autoreload

    @timer(1)
    def change_code_gracefull_reload(sig):
        if autoreload.code_changed():
            uwsgi.reload()
    if SHOW_PRINT:
        uwsgi_print('set "autoreload"')
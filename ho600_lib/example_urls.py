import os, datetime

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import get_template
from django.template import RequestContext
from django.views import static
need_staff_login_serve = staff_member_required(static.serve)

from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


def compressor_example(R):
    t0 = datetime.datetime.now()
    t = get_template('ho600_lib/compressor_example.html')
    html = t.render(RequestContext(R, {'time': (datetime.datetime.now()-t0)}))
    return HttpResponse(html)


def mediagenerator_example(R):
    t0 = datetime.datetime.now()
    t = get_template('ho600_lib/mediagenerator_example.html')
    html = t.render(RequestContext(R, {'time': (datetime.datetime.now()-t0)}))
    return HttpResponse(html)


urlpatterns = patterns('',
    url(r'compressor/', compressor_example),
    url(r'mediagenerator/', mediagenerator_example),
    url(r'', mediagenerator_example),
)

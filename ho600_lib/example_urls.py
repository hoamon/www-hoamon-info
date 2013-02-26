from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import get_template
from django.template import Context
from django.views import static
need_staff_login_serve = staff_member_required(static.serve)

from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


def view(R):
    t = get_template('ho600_lib/index.html')
    html = t.render(Context({}))
    return HttpResponse(html)


urlpatterns = patterns('',
    url(r'', view)
)

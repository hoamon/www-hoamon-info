from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.views import static
need_staff_login_serve = staff_member_required(static.serve)

from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^(?P<path>(favicon.ico|robots.txt))$', 'django.views.static.serve',
        {'document_root' : '_generated_media', 'show_indexes' : settings.DEBUG}),
    url(r'^production_mediagenerator/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root' : '_generated_media', 'show_indexes' : settings.DEBUG}),
    url(r'^static/admin/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root' : 'django_admin_media', 'show_indexes' : settings.DEBUG}),
    url(r'^__docs__/?$', need_staff_login_serve,
        {'document_root': '__docs__', 'path': 'index.html', 'show_indexes': settings.DEBUG}),
    url(r'^__docs__/(?P<path>.*)$', need_staff_login_serve,
        {'document_root' : '__docs__', 'show_indexes' : settings.DEBUG}),
    # Examples:
    # url(r'^$', 'trunk.views.home', name='home'),
    # url(r'^trunk/', include('trunk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)

urlpatterns += patterns('',
    url(r'^__admin__/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    #<<< default view on any urls, you shoule remove me and put yours.
    url(r'', lambda R: HttpResponse('''<html><head></head><body>
<h1>Hello World!!</h1>
<p>This is the default view on any urls, you shoule remove me(in ./trunk/urls.py) and put yours.</p>
<p>from <a href="https://www.ho600.com/">ho600.com</a></p>
<hr align="left" width="600px"/>
<p><h3>To Web Users:</h3>
You see this page because the "Developer" of this Web Site use
<a href="https://bitbucket.org/hoamon/ho600-django-gae-default-trunk/">ho600-django-gae-default-trunk</a>
to be a part of this site.
If you have any question,
<b>please don't submit</b> issues to
"<a href="https://bitbucket.org/hoamon/ho600-django-gae-default-trunk/">ho600-django-gae-default-trunk</a>".
</p>
<p>Thanks for your listening.</p>
<p>best regards.</p>
<p><a href="https://www.ho600.com/">ho600.com</a></p>
</body></html>
''')),
    #>>> default view on any urls, you shoule remove me and put yours.
)
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.views import static
need_staff_login_serve = staff_member_required(static.serve)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^(?P<path>(favicon.ico|robots.txt))$', 'django.views.static.serve',
        {'document_root' : 'media', 'show_indexes' : settings.DEBUG}),
    url(r'^production_mediagenerator/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root' : '_generated_media', 'show_indexes' : settings.DEBUG}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root' : 'media', 'show_indexes' : settings.DEBUG}),
    url(r'^static/admin/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root' : 'media/admin', 'show_indexes' : settings.DEBUG}),
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
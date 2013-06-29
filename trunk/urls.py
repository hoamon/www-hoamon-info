#!/usr/bin/python

#Copyright (c) 2013, ho600.com
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without modification,
#are permitted provided that the following conditions are met:
#
#    Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
#    Redistributions in binary form must
#    reproduce the above copyright notice, this list of conditions and the
#    following disclaimer in the documentation and/or other materials provided
#    with the distribution.
#
#    Neither the name of the ho600.com nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
#INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
#OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
#EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import os

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
        {'document_root' : os.path.join(settings.TRUNK, 'static'), 'show_indexes' : settings.DEBUG}),
    # for django-compressor
    url(r'^static/CACHE/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root' : os.path.join(settings.TRUNK, 'compressor-static', 'CACHE'), 'show_indexes' : settings.DEBUG}),

    # for django-mediagenerator
    url(r'^production_mediagenerator/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root' : os.path.join(settings.TRUNK, 'mediagenerator-static'), 'show_indexes' : settings.DEBUG}),

    url(r'^__docs__/?$', need_staff_login_serve,
        {'document_root': settings.DEVELOPER_DOCS_PATH, 'path': 'index.html', 'show_indexes': settings.DEBUG}),
    url(r'^__docs__/(?P<path>.*)$', need_staff_login_serve,
        {'document_root' : settings.DEVELOPER_DOCS_PATH, 'show_indexes' : settings.DEBUG}),

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

def ho600_default_view(R):
    try: from __version__ import version
    except ImportError: version = 'LOCAL_DEBUG'
    import os
    _o = ''
    if settings.DEBUG:
        for k, v in os.environ.items():
            _o += '<div><b>%s</b> = %s</div>' % (k, v)
    _s = ''
    if settings.DEBUG:
        for k in dir(settings):
            _s += '<div><b>%s</b> = %s</div>' % (k, getattr(settings, k))

    html = '''<html><head><title>Enviroment Variables</title></head><body>
<h1>Hello Version( <a target="%(version)s" href="https://bitbucket.org/hoamon/ho600-django-gae-default-trunk/commits/%(version)s">%(version)s</a> )!!</h1>
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
<hr align="left" width="600px"/>
<h3>To Developer:</h3>
<h4>os.environ:</h4>
<p>
%(_o)s
</p>
<h4>settings:</h4>
<p>
%(_s)s
</p>
</body></html>
''' % {'version': version, '_o': _o, '_s': _s}
    return HttpResponse(html)


js_info_dict = {
    'packages': ('federated_auth', ),
}


urlpatterns += patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^social_auth/', include('social_auth.urls'), name='social_auth'), # needed by federated_auth
    url(r'^federated_auth/', include('federated_auth.urls'), name='federated_auth'),

    url(r'^ho600_lib/', include('ho600_lib.urls'), name='ho600_lib'),
    #<<< default view on any urls, you shoule remove me and put yours.
    url(r'', ho600_default_view)
    #>>> default view on any urls, you shoule remove me and put yours.
)

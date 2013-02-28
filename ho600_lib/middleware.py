#!/usr/bin/env python

# Copyright (c) 2013, ho600.com
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#     Redistributions in binary form must
#     reproduce the above copyright notice, this list of conditions and the
#     following disclaimer in the documentation and/or other materials provided
#     with the distribution.
#
#     Neither the name of the ho600.com nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import re, datetime, sys
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.sessions.models import Session
from django.core.exceptions import MultipleObjectsReturned
from django.template import TemplateDoesNotExist, RequestContext
from django.template.loader import get_template
from django.views.debug import ExceptionReporter
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.conf import settings
from django.utils import simplejson as json

from ho600_lib import get_template_by_site_and_lang
from ho600_lib.models import BugPage




class Handle500Middleware(object):
    def process_exception(self, request, exception):
        """ Create a technical server error response. The last three arguments are
            the values returned from sys.exc_info().
        """
        reporter = ExceptionReporter(request, *sys.exc_info())
        #phase I, record bug page html
        bp = BugPage(html=reporter.get_traceback_html())
        bp.save()
        #phase II, record request's detail
        bp.save_with_request(request=request)
        #phase III, search the same bug kind
        bp.kind = bp.find_bug_kind()
        bp.save()

        if request.is_ajax():
            return HttpResponseServerError(json.dumps({'code': bp.code}), mimetype='application/json')
        else:
            if settings.DEBUG:
                pass
            else:
                try:
                    t = get_template_by_site_and_lang('500.html', sub_dir='')
                except TemplateDoesNotExist:
                    try:
                        t = get_template('500.html')
                    except TemplateDoesNotExist:
                        t = get_template_by_site_and_lang('500.html', sub_dir='ho600_lib')
                html = t.render(RequestContext(request, {'bug_page': bp}))
                return HttpResponseServerError(html)




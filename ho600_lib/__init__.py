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


VERSION = (1, 0, 9, 'final', 0)


import os
from django.utils.translation import get_language, get_language_from_request
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


def get_utc_time(time_str, format='%Y-%m-%d %H:%M:%S'):
    time, plus_minus, hour_offset, minute_offset = \
        re.match('([^\+]+) ([\+-])([0-9][0-9])([0-9][0-9])', time_str).groups()
    time = datetime.datetime.strptime(time, format)
    if plus_minus == '+':
        time -= datetime.timedelta(hours=int(hour_offset), minutes=int(minute_offset))
    else:
        time += datetime.timedelta(hours=int(hour_offset), minutes=int(minute_offset))
    return time


def get_site_from_settings():
    from django.conf import settings

    if hasattr(settings, 'SITE'):
        return settings.SITE
    else:
        from django.contrib.sites.models import Site
        return Site.objects.get(id=settings.SITE_ID)


def get_template_by_site_and_lang(template_name, sub_dir='ho600_lib',
                                        show_template_filename=False):
    """ the order of finding template:

            lang_names = ['user_prefer_lang'] + [settings.LANGUAGE_CODE]

            for lang_name in lang_names:
                if domain_name/module_name/lang_name/template_name: return
                if module_name/lang_name/template_name: return
            module_name/template_name
    """
    from django.conf import settings
    from django.contrib.sites.models import Site


    lang = get_language()
    if not template_name.endswith('.html'): template_name += '.html'

    if hasattr(settings, 'SITE_DOMAIN'):
        site = settings.SITE_DOMAIN
    else:
        site = Site.objects.all().order_by('id')[0].domain

    langs = [lang] + [settings.LANGUAGE_CODE]

    for lang in langs:
        paths = []
        paths.append(os.path.join(site, sub_dir, lang, template_name))
        paths.append(os.path.join(sub_dir, lang, template_name))
        for path in paths:
            try:
                t = get_template(path)
            except TemplateDoesNotExist:
                continue
            else:
                if show_template_filename:
                    logging.info('Use template: "%s"' % t.name)
                return t

    path = os.path.join(sub_dir, template_name)
    try:
        return get_template(path)
    except TemplateDoesNotExist:
        raise TemplateDoesNotExist('site: %s, sub_dir: %s, lang: %s, template_name:%s'
                                    %(site, sub_dir, lang, template_name))


def static(R, *args, **kw):
    """ Why did we make another static function?

        this wraper function can help me to set a {% url "xxx.views.static" some.js %} in the template

        And static directory means its files were "nerver" be generated by generatemedia
    """
    from django.views import static as dj_static
    return dj_static.serve(R, *args, **kw)


def media(R, *args, **kw):
    """ Why did we make another media function?

        this wraper function can help me to set a {% url "xxx.views.media" some.js %} in the template

        And media directory means its files "could" be generated by generatemedia
    """
    from django.views import static as dj_static
    return dj_static.serve(R, *args, **kw)


try:
    from google.appengine.api.datastore_types import Email
    from google.appengine.api.datastore_types import Text
    from google.appengine.api.datastore_types import PhoneNumber
    from google.appengine.api.datastore_types import Link
except ImportError:
    Email = Text = PhoneNumber = Link = None

from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.utils import simplejson as json
from django.views.debug import ExceptionReporter
from django.utils.safestring import SafeUnicode

from ho600_lib.models import BugKind, BugPage

import re
import os
import sys
import logging
import types
import datetime



class WalkStructure:
    def __init__(self, s, list_f=lambda x,y: y if 1 else y,
        hash_f=lambda x,y: y if x >=0 else y, to_json=False):
        self._s = s
        self._list_f = list_f if not to_json else self.toJSON
        self._hash_f = hash_f if not to_json else self.toJSON
        self.walk(s)


    def rNewS(self):
        return self._s


    def toJSON(self, k, v):
        type_v = type(v)
        if type_v in [types.UnicodeType, Text, Email, PhoneNumber, Link, SafeUnicode]:
            return str(v.encode('utf8'))
        elif type_v == datetime.datetime:
            return v.strftime('%Y-%m-%d %H:%M:%S')
        elif type_v == datetime.date:
            return v.strftime('%Y-%m-%d')
        else:
            return v


    def walk(self, s):
        if type(s) == types.DictionaryType:
            for k, v in s.items():
                v = self._hash_f(k, v)
                s[k] = v
                self.walk(v)

        elif type(s) == types.ListType:
            for i, v in enumerate(s):
                v = self._list_f(i, v)
                s[i] = v
                self.walk(v)
        return s



class AJAXForbiddenError(Exception): pass



class AjaxController(object):
    AJAX_FUNCTION = {}
    def register(self, ajax_function):
        func_name = ajax_function.func_name
        if self.AJAX_FUNCTION.get(func_name, None): raise Exception('%s was existed' % func_name)
        self.AJAX_FUNCTION[func_name] = ajax_function
        logging.info(self.AJAX_FUNCTION)
        return self.callback


    def callback(self, R):
        submit = R.POST['submit'] if R.POST.get('submit', None) else R.GET.get('submit', None)
        if not submit: raise AJAXForbiddenError('has no submit name')

        function = self.AJAX_FUNCTION.get(submit, None)
        if not function: raise AJAXForbiddenError('has no %s function' % submit)

        R.DATA = R.POST if R.method == 'POST' else R.GET

        try:
            result = function(R)
        except AJAXForbiddenError, e:
            return HttpResponseForbidden("\n".join(e.args), mimetype='text/plain')
        except:
            reporter = ExceptionReporter(R, *sys.exc_info())
            #phase I, record bug page html
            bp = BugPage(html=reporter.get_traceback_html())
            bp.save()
            #phase II, record request's detail
            bp.saveWithRequest(request=R)
            #phase III, search the same bug kind
            bp.kind = bp.findBugKind()
            bp.save()

            code = bp.code
            logging.error('bug page code: %s' % bp.code)
            return HttpResponseServerError(code, mimetype='text/plain')

        if type(result) in [HttpResponse, HttpResponseNotFound,
            HttpResponseForbidden, HttpResponseServerError, HttpResponseRedirect]:
            return result
        elif type(result) == types.DictType:
            result["__status__"] = True
            ws = WalkStructure(result, to_json=True)
            return HttpResponse(json.dumps(ws.rNewS()))
        else:
            return HttpResponseForbidden(u'format of return data is not defined, it should be a dictionary!',
                mimetype='text/plain')



ajax_controller = AjaxController()

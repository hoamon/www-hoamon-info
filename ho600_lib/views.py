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
# Create your views here.

from django.template.loader import get_template
from django.template import TemplateDoesNotExist, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.utils import simplejson as json

from ho600_lib import ajax_controller
from ho600_lib import AJAXForbiddenError
from ho600_lib.models import Option, BugKind, BugPage
from django.conf import settings

import re
import os
import sys
import logging
import types
import datetime


@ajax_controller.register
def testBug(R):
    a = 1 / 0


@ajax_controller.register
def testAjax(R):
    raise AJAXForbiddenError('for test AJAXForbiddenError')
    raise KeyError('for test KeyError')
    raise ValueError('for test ValueError')
    d = {}
    for k, v in R.GET.items():
        d[k] = v
    return HttpResponse(str(d), mimetype='text/plain')


@ajax_controller.register
def solvedOrQuit(R):
    try:
        bug_kind = BugKind.objects.get(id=R.DATA.get('bug_kind_id', 0))
    except BugKind.DoesNotExist:
        raise AJAXForbiddenError('No bug kind record', mimetype='text/plain')
    bug_kind.is_solved = not bug_kind.is_solved
    bug_kind.save()
    return {'is_solved': bug_kind.is_solved}


@ajax_controller.register
def search(R):
    bug_kinds = []
    code = R.DATA.get('code', None)
    if code:
        try:
            bp = BugPage.objects.get(code=code)
        except BugPage.DoesNotExist:
            pass
        else:
            if bp.kind: bug_kinds.append(bp.kind)
    else:
        start_date = R.DATA.get('start_date', '')
        end_date = R.DATA.get('end_date', '')
        is_solved = R.DATA.get('is_solved', '')
        type = R.DATA.get('type', '')
        request_url = R.DATA.get('request_url', '')
        file_name = R.DATA.get('file_name', '')
        if (not start_date and not end_date and not is_solved and
            not type and not request_url and not file_name):
            raise AJAXForbiddenError('Please input one search at least')
        if type:
            try: type = Option.objects.get(id=type)
            except Option.DoesNotExist: type = ''
        if request_url:
            try: request_url = Option.objects.get(id=request_url)
            except Option.DoesNotExist: request_url = ''
        if file_name:
            try: file_name = Option.objects.get(id=file_name)
            except Option.DoesNotExist: file_name = ''

        bug_kinds = BugKind.search(start_date=start_date, end_date=end_date,
            is_solved=is_solved, type=type, request_url=request_url, file_name=file_name)

    if not bug_kinds:
        raise AJAXForbiddenError('It has no records with your search options!')

    bks = [{'_id': bk.id,
        'type': bk.type.value,
        'note': bk.note,
        'request_url': bk.request_url.value,
        'file_name': bk.file_name.value,
        'line_no': bk.line_no,
        'is_solved': bk.is_solved,
        'lastest_10_bug_codes': [bp.code for bp in bk.r10BugPages()],
        'create_time': bk.create_time,
    } for bk in bug_kinds]
    return {'total_count': len(bug_kinds), 'bug_kinds': bks}


def recordHttp404Error(R, template_name='404.html'):
    if not R.META.get('HTTP_REFERER', '') or not R.META.get('PATH_INFO', ''):
        #log_id = None
        pass
    else:
        #log = Log()
        #user = R.user
        #referer = R.META.get('HTTP_REFERER', '')
        #path = R.META.get('PATH_INFO', '')

        #log.makeHTTP404Log(user=user, referer=referer, url=path)
        #log_id = log.object_id
        pass
    path = R.META.get('PATH_INFO', '')
    log_id = 0

    if R.is_ajax():
        return HttpResponseNotFound('%s<>%s'%(path, log_id), mimetype='text/plain')
    else:
        f = os.path.join(R.META.get('HTTP_HOST', ''), '404.html')
        try:
            t = get_template(f)
        except TemplateDoesNotExist:
            try:
                t = get_template('404.html') # You need to create a 404.html template.
            except TemplateDoesNotExist:
                t = get_template(os.path.join('ho600_lib', '404.html'))
        html = t.render(RequestContext(R, {'log_id': log_id, 'request': R}))
        return HttpResponseNotFound(html)


def rBugKind(R, id):
    try:
        bug_kind = BugKind.objects.get(id=id)
    except BugKind.DoesNotExist:
        return HttpResponseForbidden('Cound not find bug kind: %s' % id, mimetype='text/plain')
    t = get_template(os.path.join('ho600_lib', 'bug_kind.html'))
    html = t.render(RequestContext(R, {'bug_kind': bug_kind}))
    return HttpResponse(html)


def rBugKindHtml(R, id):
    try:
        bug_kind = BugKind.objects.get(id=id)
    except BugKind.DoesNotExist:
        return HttpResponseForbidden('Cound not find bug kind: %s' % id, mimetype='text/plain')
    return HttpResponse(bug_kind.html)


def rBugPage(R, code):
    try:
        bug_page = BugPage.objects.filter(code=code).order_by('-id')[0]
    except IndexError:
        return HttpResponseForbidden('Cound not find bug page: %s' % code, mimetype='text/plain')
    t = get_template(os.path.join('ho600_lib', 'bug_page.html'))
    html = t.render(RequestContext(R, {'bug_page': bug_page}))
    return HttpResponse(html)


def rBugPageHtml(R, code):
    try:
        bug_page = BugPage.objects.filter(code=code).order_by('-id')[0]
    except IndexError:
        return HttpResponseForbidden('Cound not find bug page: %s' % code, mimetype='text/plain')
    if bug_page.html:
        return HttpResponse(bug_page.html)
    else:
        return HttpResponse(bug_page.kind.html)


def rBugList(R):
    bk_query = BugKind.objects.filter(is_solved=False).order_by('-create_time')
    total_count = bk_query.count()
    bug_kinds = bk_query[:10]
    t = get_template(os.path.join('ho600_lib', 'bug_list.html'))
    html = t.render(RequestContext(R, {'total_count': total_count, 'bug_kinds': bug_kinds}))
    return HttpResponse(html)


callback = ajax_controller.callback
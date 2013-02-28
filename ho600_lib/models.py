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

from django.db import models as M
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AnonymousUser
from django.utils import simplejson as json
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext

from random import choice, randint
from types import IntType, LongType

import re, datetime, logging, settings, os


def NOW(): return datetime.datetime.now()



class Tree(M.Model):
    parent = M.ForeignKey('self', related_name='child_set', null=True)



    class Meta:
        """ It will not generate a database table when 'abstract' set True
        """
        abstract = True



    def has_this_child(self, child):
        if self == child:
            return True
        else:
            for c in self.child_set.all():
                if c.has_this_child(child):
                    return True
        return False



    def get_all_child_set_as_list(self, level=0, max_level=0):
        if max_level > 0 and level > max_level:
            return []
        else:
            list = [(level, self)]
            for c in self.child_set.all().order_by('id'):
                sub_list = c.get_all_child_set_as_list(level=level+1, max_level=max_level)
                list.extend(sub_list)
            return list



class PostCode(Tree):
    """ About:

            A model collects post code data

        Usage:

            In your another models.py, put some code like below:

                from ho600_lib.models import PostCode
                class SomeYourPlace(PostCode):
                    pass

            And copy a json exmaple likes ROOT/ho600_lib/fixtures/taiwan_postcode.py
            to your modules/fixtures/ and rename "model" value to be "yourmodule.someyourplace"
    """
    id = M.CharField(verbose_name='post code', primary_key=True, max_length=32)
    code = M.CharField(verbose_name='post code', max_length=6, null=True)
    name = M.CharField(verbose_name='name', max_length=32)
    extra_name = M.CharField(verbose_name='extra name', max_length=128, null=True)
    note = M.TextField(default='')


    class Meta:
        """ It will not generate a database table when 'abstract' set True
        """
        abstract = True



    def __str__(self):
        return '%s: %s(code: %s)' % (self.id, self.name, self.code)


    def __unicode__(self):
        return u'%s: %s(code: %s)' % (self.id, self.name, self.code)



class Option(M.Model):
    swarm = M.CharField(verbose_name=_('Swarm'), max_length=64)
    value = M.CharField(verbose_name=_('Value'), max_length=512)



class BugKind(M.Model):
    request_url = M.ForeignKey(Option, verbose_name=_('Request URL'), related_name='be_request_url_set')
    file_name = M.ForeignKey(Option, verbose_name=_('Wrong File'), related_name='be_file_name_set')
    line_no = M.IntegerField(verbose_name=_('Wrong Line No.'))
    type = M.ForeignKey(Option, verbose_name=_('Wrong Type'), related_name='be_type_set')
    note = M.TextField(verbose_name=_('Wrong Note'))
    html = M.TextField(verbose_name=_('Bug page'))
    tracker = M.CharField(verbose_name=_('Tracker'), max_length=512, null=True)
    create_time = M.DateTimeField(verbose_name=_('Create Time'), auto_now_add=True)
    is_solved = M.BooleanField(verbose_name=_('Is Solved?'), default=False)
    solved_time = M.DateTimeField(verbose_name=_('Solved Time'))


    @classmethod
    def search(self, **kw):
        hash = {}
        for k, v in kw.items():
            if v and k not in ['start_date', 'end_date']:
                if k == 'is_solved':
                    if v == 'True':
                        hash[k] = True
                    else:
                        hash[k] = False
                else:
                    hash[k] = v

        if kw.get('start_date', None):
            try:
                date = datetime.datetime.strptime(kw['start_date'], '%Y-%m-%d')
            except ValueError:
                date = ''
            if date: hash['create_time__gte'] = date

        if kw.get('end_date', None):
            try:
                date = datetime.datetime.strptime(kw['end_date'], '%Y-%m-%d')
            except ValueError:
                date = ''
            if date: hash['create_time__lte'] = date

        return self.objects.filter(**hash)


    def rAllBugPages(self):
        return self.bugpage_set.all().order_by('-create_time')


    def r10BugPages(self):
        return self.bugpage_set.all().order_by('-create_time')[:10]


    def save(self):
        if self.id:
            old_object = self.__class__.objects.get(id=self.id)
            if old_object.is_solved != self.is_solved:
                #TODO connect tracker
                logging.info('#TODO: Do connectting tracker')
                if old_object.is_solved == False:
                    for bp in self.bugpage_set.all():
                        bp.is_solved = True
                        bp.save()

        super(BugKind, self).save()



REQUEST_URL_RE = re.compile('<th>Request URL:</th>[ \t]*<td>([^<]+)</td>', flags=re.I)
FILENAME_LINE_NO_RE = re.compile('<th>Exception Location:</th>[ \t]*<td>([^<]+) +in +[^<]+, +line +([0-9]+)[^<]*</td>', flags=re.I)
TYPE_NOTE_RE = re.compile('<div id="summary">[ \t]*<h1>([^<]+)</h1>[ \t]*<pre[^>]*>([^<]*)</pre>', flags=re.I)
ROOT_RE = re.compile('^%s/'%os.path.dirname(os.path.abspath(settings.__file__)))
class BugPage(M.Model):
    LETTER_SET = ('-', '+', '/', '*', '2', '3', '5', '6', '8', '9', 'A', 'J', 'K', 'L', 'N', 'Y', 'Z')

    kind = M.ForeignKey(BugKind, null=True)
    code = M.CharField(verbose_name=_('Wrong Code'), max_length=4, null=True)
    username = M.CharField(max_length=64, null=True)
    remote_addr = M.CharField(verbose_name=_('User IP'), max_length=15, null=True)
    get = M.CharField(verbose_name=_('GET'), max_length=512, null=True)
    post = M.CharField(verbose_name=_('POST or PUT'), max_length=512, null=True)
    cookies = M.CharField(verbose_name=_('COOKIES'), max_length=512, null=True)
    method = M.CharField(verbose_name=_('Request Method:GET/POST/PUT/DELETE'), max_length=6, null=True)
    html = M.TextField(verbose_name=_('Bug Page'))
    is_solved = M.BooleanField(verbose_name=_('Is Solved'), default=False)
    create_time = M.DateTimeField(verbose_name=_('Create Time'), auto_now_add=True)
    solved_time = M.DateTimeField(verbose_name=_('Solved Time'))


    def find_bug_kind(self):
        if self.kind: return self.kind
        html = self.html.replace('\n', '').replace('\r', '')
        request_url = REQUEST_URL_RE.search(html).groups()[0]
        try:
            request_url = Option.objects.get(swarm='request_url-option', value=request_url[:512])
        except Option.DoesNotExist:
            request_url = Option(swarm='request_url-option', value=request_url[:512])
            request_url.save()
        try:
            file_name, line_no = FILENAME_LINE_NO_RE.search(html).groups()
        except:
            file_name, line_no = 'No File', 0
        file_name = ROOT_RE.sub('', file_name)
        try:
            file_name = Option.objects.get(swarm='file_name-option', value=file_name[:512])
        except Option.DoesNotExist:
            file_name = Option(swarm='file_name-option', value=file_name[:512])
            file_name.save()
        type, note = TYPE_NOTE_RE.search(html).groups()
        try:
            type = Option.objects.get(swarm='type-option', value=type[:512])
        except Option.DoesNotExist:
            type = Option(swarm='type-option', value=type[:512])
            type.save()
        try:
            bk = BugKind.objects.get(request_url=request_url, file_name=file_name,
                line_no=int(line_no), type=type)
            if bk.note != note: raise BugKind.DoesNotExist
        except BugKind.DoesNotExist:
            bk = BugKind(request_url=request_url, file_name=file_name,
                line_no=int(line_no), type=type, note=note, html=self.html)
        except BugKind.MultipleObjectsReturned:
            bk = BugKind.objects.filter(request_url=request_url, file_name=file_name,
                line_no=int(line_no), type=type).order_by('-create_time')[0]
        bk.is_solved = self.is_solved
        bk.save()
        count = bk.bugpage_set.all().count()
        if count > 20:
            for bp in bk.bugpage_set.all()[5:(count-15)]:
                bp.delete()
        return bk


    def save(self):
        if not self.code:
            while 1:
                code = ''.join([choice(self.LETTER_SET) for i in xrange(4)]).upper()
                if not self.__class__.objects.filter(code=code):
                    self.code = code
                    break

        if self.is_solved and self.html:
            self.html = ''
            self.solved_time = NOW()

        if self.id: self.kind = self.findBugKind()

        super(BugPage, self).save()

        if self.kind and self.is_solved == False:
            self.kind.is_solved = False
            self.kind.save()


    def _get_plain_string(self, dictionary):
        keys = dictionary.keys()
        keys.sort()
        return '\n'.join(['%s=%s'%(k, dictionary[k]) for k in keys])


    def save_with_request(self, request):
        if getattr(request, 'user', None) and type(request.user) != AnonymousUser:
            self.username = request.user.username
        self.remote_addr = request.META.get('REMOTE_ADDR', '')
        self.method = request.method
        self.get = self._get_plain_string(request.GET)[:500]
        self.post = self._get_plain_string(request.POST)[:500]
        self.cookies = self._get_plain_string(request.COOKIES)[:500]
        self.save()
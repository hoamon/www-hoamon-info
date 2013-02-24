#!/usr/bin/python

#Copyright (c) 2012, ho600.com
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


VERSION = (1, 0, 3, 'final', 0)


import os
from django.utils.translation import get_language, get_language_from_request
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views import static as dj_static
from django.conf import settings
from django.contrib.sites.models import Site


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
    if hasattr(settings, 'SITE'):
        return settings.SITE
    else:
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
    return dj_static.serve(R, *args, **kw)


def media(R, *args, **kw):
    """ Why did we make another media function?

        this wraper function can help me to set a {% url "xxx.views.media" some.js %} in the template

        And media directory means its files "could" be generated by generatemedia
    """
    return dj_static.serve(R, *args, **kw)


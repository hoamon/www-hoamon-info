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

import re
from django.conf import settings
from django import template
from django import forms
from mediagenerator.generators.bundles.utils import _render_include_media
from mediagenerator import utils

from ho600_lib.models import Option

register = template.Library()

@register.simple_tag
def use_jqueryui(jquery_version, jqueryui_version, theme_name):
    return """<link rel="stylesheet" title="default" type="text/css" media="screen" href="//ajax.googleapis.com/ajax/libs/jqueryui/%(jqueryui_version)s/themes/%(theme_name)s/jquery-ui.css" />
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/%(jquery_version)s/jquery.min.js"></script>
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jqueryui/%(jqueryui_version)s/jquery-ui.min.js"></script>
    <script type="text/javascript">
            function self_joined_jquery () {
                if (JQUERY_CSS && JQUERY_JS && JQUERYUI_JS){
                    document.write(unescape('%%3Clink rel="stylesheet" title="default" type="text/css" media="screen" href="'+JQUERY_CSS+'" /%%3E'));
                    document.write(unescape('%%3Cscript src="'+JQUERY_JS+'" type="text/javascript"%%3E%%3C/script%%3E'));
                    document.write(unescape('%%3Cscript src="'+JQUERYUI_JS+'" type="text/javascript"%%3E%%3C/script%%3E'));
                    if (typeof console) {
                        console.log('Use self-joined jquery-ui files');
                    }
                } else {
                    if (typeof console) {
                        console.log('No jquery files!!');
                    }
                }
            }
            if (%(DEBUG)s) {
                self_joined_jquery();
            } else if (typeof jQuery == 'undefined') {
                if (typeof console) {
                    console.log('Failure on loading google libs!!!');
                }
                self_joined_jquery();
            } else {
                if (typeof console) {
                    console.log('Well done on loading google libs!!!');
                }
            }
        </script>""" % {
            'DEBUG': 'true' if settings.DEBUG else 'false',
            'jquery_version': jquery_version,
            'jqueryui_version': jqueryui_version,
            'theme_name': theme_name,
        }


@register.simple_tag
def setupButton(args):
    buttons = []
    for i in re.split(' *, *', args):
        class_name, button_note = re.split(' *: *', i)
        buttons.append(
            (u"""<button type="button" class="%s
            ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"
            role="button" aria-disabled="false">
            <span class="ui-button-text">%s</span></button>"""
            % (class_name, button_note)).encode('utf8'))
    return ' '.join(buttons)


@register.simple_tag
def rSelect(swarm=''):
    choices = [('', '')]
    options = Option.objects.filter(swarm=swarm).order_by('-id')
    if options.count() > 20:
        options = options[:20]
        choices.extend([(s.id, s.value) for s in options])
        choices.append(('20', 'more...'))
    else:
        choices.extend([(s.id, s.value) for s in options])
    select = forms.Select()
    return select.render(swarm, '', {'id': 'id_%s'%swarm, 'class': swarm}, choices)


@register.simple_tag
def loading():
    return """<img id="loading" style="display: none;" src="/static/ho600_lib/images/loading.gif"/>"""
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

import re, datetime
from django.conf import settings as dj_settings



def settings(R):
    try: from __version__ import version
    except ImportError: version = 'LOCAL_DEBUG'
    try: from __version__ import BUILD_URL
    except ImportError: BUILD_URL = 'NO_BUILD_URL'
    if version == 'LOCAL_DEBUG':
        version = R.META.get('CURRENT_VERSION_ID', '__ondjangoserver__')
        if version != '__djangoserver__':
            r = re.match('[^-]+-([^-]+)-.*-([^-]+)\.[0-9]+', version)
            if not r: version = '__version__'
            else: version = '-'.join(r.groups())
    d = {}
    for k in dir(dj_settings):
        d[k] = getattr(dj_settings, k)
    d['BUILD_URL'] = BUILD_URL
    d['version'] = version
    d['now'] = datetime.datetime.now()
    return {'settings': d}
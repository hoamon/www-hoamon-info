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

import os, sys
from shutil import copy, rmtree, copytree, ignore_patterns
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)
from trunk import settings
trunk_dir = settings.TRUNK
module_dir = os.path.join(trunk_dir, 'depends_modules')

# copy moduels to trunk/depends_modules/
for app_name in settings.INSTALLED_APPS:
    app_name = app_name.split('.')[0]
    if 'django' == app_name: continue

    old_app_dir = os.path.join(module_dir, app_name)
    if os.path.isdir(old_app_dir):
        rmtree(old_app_dir)

    app = __import__(app_name)
    app_from_dir = os.path.dirname(app.__file__)
    app_to_dir = os.path.join(module_dir, app_name)

    print '%s == copy ==> %s' % (os.path.basename(app_from_dir), app_to_dir)
    copytree(app_from_dir, app_to_dir, ignore=ignore_patterns('*.pyc', '.hg'))
    print '\tDone for %s' % os.path.basename(app_to_dir)

# run ./manage.py generatemedia to export static media file
r = os.popen('%s generatemedia'%os.path.join(trunk_dir, 'manage.py'))
print(r.read())

# copy favicon.ico and robots.txt after ./manage.py generatemedia
copy(os.path.join(trunk_dir, 'media/favicon.ico'), os.path.join(trunk_dir, '_generated_media'))
copy(os.path.join(trunk_dir, 'media/robots.txt'), os.path.join(trunk_dir, '_generated_media'))
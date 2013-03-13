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
from os.path import join
from shutil import copy, rmtree, copytree, ignore_patterns
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)
from trunk import settings
trunk_dir = settings.TRUNK
module_dir = join(trunk_dir, 'depends_modules')

# copy modules to trunk/depends_modules/
if hasattr(settings, 'ANOTHER_DEPENDS_MODULES'):
    MODULES = settings.ANOTHER_DEPENDS_MODULES + settings.INSTALLED_APPS
else:
    MODULES = settings.INSTALLED_APPS

for app_name in MODULES:
    app_name = app_name.split('.')[0]
    if app_name in ('django', 'ho600_lib'): continue

    old_app_dir = join(module_dir, app_name)
    if os.path.isdir(old_app_dir):
        print '\t\tdelete: %s' % old_app_dir
        rmtree(old_app_dir)

    app = __import__(app_name)
    app_from_dir = os.path.dirname(app.__file__)
    if (join(trunk_dir, 'modules') in app_from_dir
        or join(trunk_dir, 'depends_modules') in app_from_dir):
        continue

    app_to_dir = join(module_dir, app_name)

    print '%s == copy ==> %s' % (os.path.basename(app_from_dir), app_to_dir)
    copytree(app_from_dir, app_to_dir, ignore=ignore_patterns('*.pyc', '.hg'))
    print '\tDone for %s' % os.path.basename(app_to_dir)

if os.path.isdir(join(module_dir, 'ho600_lib')):
    rmtree(join(module_dir, 'ho600_lib'))
print '%s == copy ==> %s' % (os.path.basename(join(root, 'ho600_lib')), join(module_dir, 'ho600_lib'))
copytree(join(root, 'ho600_lib'), join(module_dir, 'ho600_lib'),
        ignore=ignore_patterns('*.pyc', '.hg'))
print '\tDone for %s' % os.path.basename(join(module_dir, 'ho600_lib'))

# run ./manage.py collectstatic to collectstatic static files
r = os.popen('%s collectstatic --noinput'%join(trunk_dir, 'manage.py'))
print(r.read())

# run ./manage.py generatemedia to export static media files
r = os.popen('%s generatemedia'%join(trunk_dir, 'manage.py'))
print(r.read())

# run ./manage.py compress --settings=compressor_settings to export static media files
r = os.popen('%s compress --settings=compressor_settings'%join(trunk_dir, 'manage.py'))
print(r.read())
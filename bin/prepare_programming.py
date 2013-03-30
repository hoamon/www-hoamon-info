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
import zipfile
from urllib2 import Request, urlopen, URLError, HTTPError
from shutil import rmtree, copytree
from distutils import dir_util
from advance_hg import AdvanceHG
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)
from trunk import settings


def unzip(file_name, dest_dir):
    zfile = zipfile.ZipFile(file_name)
    for name in zfile.namelist():
        (dirname, filename) = os.path.split(name)
        dirname = os.path.join(dest_dir, dirname)
        if not os.path.exists(dirname): os.makedirs(dirname)
        if name.endswith('/'):
            if not os.path.exists(os.path.join(dirname, filename)):
                os.makedirs(os.path.join(dirname, filename))
        else:
            fd = open(os.path.join(dirname, filename), "wb")
            fd.write(zfile.read(name))
            fd.close()
    return True


def download_file(url, file_name, dest_dir):
    req = Request(url)
    try:
        f = urlopen(req)
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url
    else:
        print "\tDownloading: " + url
        local_file = open(os.path.join(dest_dir, file_name), "wb")
        local_file.write(f.read())
        local_file.close()
    return True



class Rargs:
    def __init__(self, rargs=[]): self.rargs = rargs



# get all depends_modules by hg pull or clone
ahg = AdvanceHG(run_in_function=True)
PWD = os.path.dirname(os.path.abspath(__file__))
a = Rargs(['-j'])
ROOT = os.path.join(PWD, '..')
ahg.pullAll('', '--pullall', ROOT, a)

# delete all depends modules in trunk/moduels/
trunk_dir = settings.TRUNK
module_dir = os.path.join(trunk_dir, 'depends_modules')
if hasattr(settings, 'ANOTHER_DEPENDS_MODULES'):
    MODULES = settings.ANOTHER_DEPENDS_MODULES + settings.INSTALLED_APPS
else:
    MODULES = settings.INSTALLED_APPS
for app_name in MODULES:
    app_name = app_name.split('.')[0]
    if 'django' == app_name: continue

    old_app_dir = os.path.join(module_dir, app_name)
    if os.path.isdir(old_app_dir):
        rmtree(old_app_dir)
        print '== Delete dir: %s'%old_app_dir

print '== Find Downloads == <<<'
try:
    pss = ahg.rConfig('downloads', '.', 'depends_modules.conf')
except ValueError:
    print '\t No Set Downloads'
else:
    for ps in pss:
        dest_dir = os.path.join(ROOT, ps[0])
        if os.path.isdir(dest_dir):
            rmtree(dest_dir)
            print '== Delete dir: %s' % dest_dir
        dir, file_name = os.path.split(ps[1])
        if download_file(ps[1], file_name, os.path.join(ROOT, 'asset')):
            if '.zip' in file_name.lower():
                unzip(os.path.join(ROOT, 'asset', file_name), os.path.join(ROOT, ps[0]))
            elif '.tgz' in file_name.lower() or '.gz' in file_name.lower():
                raise Exception('Not Yet!')
print '>>> == Find Downloads =='

print '== Find Copies == <<<'
try:
    pss = ahg.rConfig('copies', '.', 'depends_modules.conf')
except ValueError:
    print '\t No Set Copies'
else:
    for ps in pss:
        to_file, from_file = ps
        to_file = os.path.join(ROOT, to_file)
        from_file = os.path.join(ROOT, from_file)
        to_dir = os.path.dirname(to_file)
        if not os.path.isdir(to_dir):
            os.makedirs(to_dir)
        print from_file
        print to_file
        dir_util.copy_tree(from_file, to_file)
print '>>> == Find Copies =='

print '== Find Deletes == <<<'
try:
    pss = ahg.rConfig('copies', '.', 'depends_modules.conf')
except ValueError:
    print '\t No Set Deletes'
else:
    for ps in pss:
        none, del_file = ps
        del_file = os.path.join(ROOT, del_file)
        print del_file
        rmtree(del_file)
print '>>> == Find Deletes =='

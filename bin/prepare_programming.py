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
from shutil import rmtree, copytree
from advance_hg import AdvanceHG
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)
from trunk import settings



class Rargs:
    def __init__(self, rargs=[]): self.rargs = rargs



# get all depends_modules by hg pull or clone
ahg = AdvanceHG(run_in_function=True)
pwd = os.path.dirname(os.path.abspath(__file__))
a = Rargs(['-j'])
ahg.pullAll('', '--pullall', os.path.join(pwd, '..'), a)

# delete all depends modules in trunk/moduels/
trunk_dir = settings.TRUNK
module_dir = os.path.join(trunk_dir, 'depends_modules')
for app_name in settings.INSTALLED_APPS:
    app_name = app_name.split('.')[0]
    if 'django' == app_name: continue

    old_app_dir = os.path.join(module_dir, app_name)
    if os.path.isdir(old_app_dir):
        rmtree(old_app_dir)
        print '== Delete dir: %s'%old_app_dir
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

from django.db import models as M



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


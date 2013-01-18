#!/usr/bin/python
# -*- coding: utf8 -*-

#Copyright (c) 2013, ho600.com and hoamon.info
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
#    Neither the name of the ho600.com and hoamon.info nor the names of its contributors
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

""" executing command:
    $ bin/get_blogger_posts_and_convert_to_rst.py 398420085248706856

    META format is suiting for tinkerer( http://www.tinkerer.me/ )

    depending lib: feedparser( http://code.google.com/p/feedparser/ )
        and html2rst( http://docutils.sourceforge.net/sandbox/cliechti/html2rst/html2rst.py )
"""

from html2rst import html2text
import sys, feedparser, os, re

META = '''

.. author:: default
.. categories:: chinese
.. tags:: %(tags)s
.. comments::'''


def get_blogger_posts(blogger_id):
    max_results = 25
    index = 1
    count = 0
    link = 'http://www.blogger.com/feeds/%s/posts/default?start-index=%%s&max-results=%s' % (blogger_id, max_results)

    while 1:
        l = link % index
        d = feedparser.parse(l)
        for e in d.entries:
            count += 1
            s = html2text(e.content[0].value)
            filepath = re.sub('^http://blog.hoamon.info/', '', e.link)
            filename = re.sub('.html$', '.rst', os.path.basename(filepath))
            dirname = os.path.join('blogger', os.path.dirname(filepath), '01')
            if not os.path.isdir(dirname):
                os.makedirs(dirname)

            file = open(os.path.join(dirname, filename), 'wb')
            title = e.title + '\n' + '='*80 + '\n\n'
            file.write(title)
            file.write(s)
            if hasattr(e, 'tags'):
                meta = META % {'tags': ', '.join([i['term'] for i in e.tags])}
            else:
                meta = META % {'tags': ''}
            file.write(meta)
            file.close()
        if len(d.entries) == 0: break
        index += max_results
    return count


if __name__ == '__main__':
    try: blogger_id = sys.argv[1]
    except IndexError:
        raise Exception('Please input your blogger ID!!!')
    res_count = get_blogger_posts(blogger_id)
    print 'final posts: %s' % res_count
#!/usr/bin/env python

import re, sys

def symbol_to_unicode(s):
    r = []
    for l in s.split('\n'):
        s = unicode(eval("u'"+l+"'"))
        print s
        #r.append(s+"\n")
    #return ''.join(r)

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename)

    result = symbol_to_unicode(f.read())
    print result

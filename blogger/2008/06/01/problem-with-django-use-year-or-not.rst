problem with django: use __year or not && use subversion or not
================================================================================

when i put the new sources in the remote web server, and something happened!

the query result had nothing!! when i 'diff' the environment of server and
mine, i got one thing difference. one is python 2.5.2 and the other is 2.5.1,
but i have no idea about why!

the problem is 『__year』, i set a datetime field in a django model, and i can
query it by year with suffix parameter __year like
filter(date__year=datetime.date.today().year). and it's work for mine but not
for remote server. so for the general case, i changed the code to two queries
like below:

filter(date__gte=datetime.date(datetime.date.today().year, 1,1),
date__lte=datetime.date(datetime.date.today().year, 12,31))

then i changed 5 files in my application. before svn commit, i use svn diff
to see what i modified and found a error.

Can you see??

::
    --- apps/supervise/views.py     (revision 1256)
    +++ apps/supervise/views.py     (working copy)
    @@ -145,7 +145,8 @@
    if h.has_key('year') and h['year'] != '':
        Y = Year.objects.get(id=h['year'])
        try:
    -            sc = sc.filter(date__year=Y.date.year)
    +            sc = sc.filter(date__get=datetime.date(Y.date.year, 1,
    1),
    +            date__lte=datetime.date(Y.date.year, 12, 31))
        except:
            pass
    ........


if i have no subversion, i will write a bug after a debug.

Old Comments in Blogger
--------------------------------------------------------------------------------



`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2009-11-13T07:49:16.010+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

because i type wrong word:

In this line:
+ sc = sc.filter(date__get=datetime.date(Y.date.year, 1, 1),

i should use "date_gte", not date_get

.. author:: default
.. categories:: chinese
.. tags:: django, subversion, python
.. comments::
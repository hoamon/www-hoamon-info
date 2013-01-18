Use django's models without running web server
================================================================================

>>This article also posts on `django-users`_<<

Because i can't find related post here, so i post this example. maybe someone
else need.

Sometimes, you just want to use the useful models of django without thinking
any sql statement.
Maybe you want to run a script to know which user's birthday in your database
is today,
this little job should not run in the view.py. It should run in the cron
table of linux os every day,
so that your users can receive birthday card from your system.

this example is so easy, all you know is loading the settings.py correctly.
Your script must place in your django project's directory.

script example:
::
    ** 1 ****#!/usr/bin/env python**
    ** 2 ****# -*- coding: utf8 -*-**
    ** 3 **
    ** 4 ****import** settings
    ** 5 ****from** django.core.management **import** setup_environ
    ** 6 **setup_environ(settings)
    ** 7 ****# before do something else,**
    ** 8 ****# the there lines above here is your first operation.**
    ** 9 **
    **10 ****from** django.db.models **import** get_model
    **11 ****from** datetime **import** date
    **12 **
    **13 ****if** __name__ == **'__main__'**:
    **14 **
    **15 **    **# the 'tmp' is your project's name, **
    **16 **    **# and this script must place in the 'tmp' directory.**
    **17 **    **# the 'person' is your model's name.**
    **18 **    Person = get_model(**'tmp'**, **'person'**)
    **19 **
    **20 **    **# when you get the model,**
    **21 **    **# you can use it just like you use it in the view.py**
    **22 **    P = Person(name=**'hoamon'**, birth=date(1977, **10**,
    **18**))
    **23 **    P.save()
    **24 **
    **25 **    **for** p **in** Person.objects.all():
    **26 **        **if** p.birth == date(1977, **10**, **18**):
    **27 **            **print** p.name
    **28 **
    **29 **    **for** p **in** Person.objects.filter(birth=date(1977,
    **10**, **18**)):
    **30 **        **print** p.name

now you can put /somepath/tmp/birthday.py in the cron table.

.. _django-users: http://groups.google.com/group/django-users?lnk=ig


Old Comments in Blogger
--------------------------------------------------------------------------------



`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2007-11-25T19:19:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After i posted this comment on `django-users`_, i found the keyword is "use
models outside django", not "without web server".

.. _django-users: http://groups.google.com/group/django-users


.. author:: default
.. categories:: chinese
.. tags:: django
.. comments::
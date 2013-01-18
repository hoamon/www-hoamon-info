Mercurial on Google Code is available to every project
================================================================================

今天晃到自己的專案 `django-pgpauth`_ 時，才發現多了 Mercurial 的選項。原來早`在 5 月 28 日時就己經正式推出`_了。

要轉移原來的 subversion 資料庫到 hg 儲存庫中是很簡單的一件事。

在 Ubuntu 下，先安裝 python-subversion 套件。然後將 /etc/mercurial/hgrc.d/hgext.rc 中「#
hgext.convert =」的註解拿掉。

接下來，作轉換的動作。

# hg convert http://projectname.googlecode.com/svn hg-client
# cd hg-client
# hg push https://projectname.googlecode.com/hg

最後，記得到 administer > source > Repository type，把 Version control system 改成
Mercurial 即可。

.. _django-pgpauth: http://code.google.com/p/django-pgpauth/
.. _在 5 月 28 日時就己經正式推出: http://google-code-updates.blogspot.com/2009/05
    /mercurial-now-available-to-all-open.html


.. author:: default
.. categories:: chinese
.. tags:: mercurial, linux, subversion, google, ubuntu
.. comments::
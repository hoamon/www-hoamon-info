Python: 持續讚嘆中
================================================================================

我幾天都在 Python 的領域中翻滾，看了許多 `Trac`_ 及 `Django`_ 的文件，覺得 Python 開發模式實在是太棒了。這對過去常用
PHP 的人來說，是一種新鮮的經驗。

感到最大的不同點是：


1.  自己帶 web server裝

-   Trac 或 Django 的程式時，它們會自己帶一個 http deamon(lighthttpd)
    ，所以程式裝完，不太需要設定，就可以跑了。

2.  程式是裝在系統中，而不是 www 資料夾

-   並不像 PHP 的專案，要把所有的程式放在某個地方，然後設定 apache 的 DocumentRoot 。這些 Python
    程式就像是一個元件或函式庫是放在系統用的資料夾中，也就是當你要寫別的專案時，直接在程式碼中 import 進來。而不是
    require('特定位址的 php 程式')

因為第2點的特性，所以軟體工程師在開發 web 專案時，必需將程式以 class 的方式存在，所以專案的可用性也就提高了。

Python 真是好東西呀!

.. _Trac: http://trac.edgewall.org/
.. _Django: http://www.djangoproject.com/


.. author:: default
.. categories:: chinese
.. tags:: django, trac, python
.. comments::
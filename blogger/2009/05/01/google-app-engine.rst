把我的個人網站搬到 Google App Engine
================================================================================

自從上次運作 `http://www.hoamon.info/`_ 的 Ubuntu 主機硬碟掛了後，就一直怗記著要把 Djange base
的個人網站改到 GAE 去。畢竟我還是比較相信 Google 的工程師在主機維護上的能力。

這個週未，終於花了點時間作移植。有點累。

與 Django 相比，到也不是比較難，而是 GAE 用了很多與原本 LAMP 不一樣的管理/程式概念。像是資料表方面，雖然 GAE 有提供 Data
Viewer ，但這與傳統方式觀看資料表又不一樣，轉資料是我花最多時間的地方。

另外這一次比較重大的改變，則是我把原始資料格式從 html 改成 rST 了。如此一來，與我其他文件可以作更快速地轉換了，而這個 python-
docutils 的函式庫與 GAE 相容問題也讓我花了不少時間。有機會，再向各位介紹了。我累了，要睡了。

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/Shl0MUHqjhI/AAAAAAAAB4I/yY1
aRlRCljA/s400/Screenshot.png
`_

.. _http://www.hoamon.info/: http://www.hoamon.info/
.. _另外這一次比較重大的改變，則是我把原始資料格式從 html 改成 rST 了。如此一來，與我其他文件可以作更快速地轉換了，而這個
    python-docutils 的函式庫與 GAE 相容問題也讓我花了不少時間。有機會，再向各位介紹了。我累了，要睡了。: http://3.bp
    .blogspot.com/_eKM9lHjTZjs/Shl0MUHqjhI/AAAAAAAAB4I/yY1aRlRCljA/s1600-h/Sc
    reenshot.png


.. author:: default
.. categories:: chinese
.. tags:: django, linux, python, google app engine, ubuntu
.. comments::
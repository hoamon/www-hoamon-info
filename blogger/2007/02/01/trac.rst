Trac安裝筆記(上)
================================================================================

2006年在自由軟體的最佳開發人員協助工具領域獲得評審肯定大獎的 Trac 軟體，是一套結合 Wiki 及 Request Ticket
    的網頁程式。

wiki 適合來作規格書的共同開發; RT 則適合作程式專案的回饋追蹤。本來以為只有我會把這兩樣東西合在一起使用，正想裝一個 kwiki 及一個 RT
系統時(真巧兩個都是 Perl 寫的)，居然讓我發現這個用 Python 寫的整合系統 Trac ，嘿嘿~世事難料!果然如此。

Trac 官網： http://trac.edgewall.org/ (原 http://trac.edgewall.com/ )
它本來應是一間公司，不過現在改成 .org 的，站上也沒看見任何販賣及商業支援的資訊，應該不會是搞 Python
的，都賺不了錢吧!希望是錢賺太多，不想賺了。

安裝 Trac ，要先決定兩個部份：資料庫及應用伺服器。

資料庫方面，與 Python 配合度最高的是 SQLite ，官方也是推薦這個資料庫管理系統，另外也有兩個選擇 PostgreSQL 及 MySQL
，但注意 MySQL 仍在測試當中。所以我選擇 SQLite 。

應用伺服器有3個選擇，直接使用 Trac 內建的 Tracd 、 FastCGI 及 Mod_Python ，執行速度是後者較前者快 。這部份我們使用
Mod_Python 配合 apache2 來作我們的應用伺服器。

其他還有須先期安裝的有：
subversion
subversion-tools
libapache2-svn
python2.4( 任何一套 Linux 套件應該都已安裝了，沒有的話請寄信跟我說，我送你一套 )
python2.4-subversion
python2.4-pysqlite2
python2.4-clearsilver
python2.4-dev
python2.4-setuptools
python2.4-docutils
以上軟體為 Ubuntu 套件名，下面則是 Fedora 套件名。
subversion
mod_dav_svn
python-subversion
python-sqlite2
python-clearsilver
python-docutils
python-devel
python-setuptools

接下來安裝 SilverCity( 官網：http://sourceforge.net/projects/silvercity/ )
----解壓縮下載包
----# cd SilverCity ; sudo python setup.py install #你應該要有 gcc 及 g++ 編譯器

在正式的系統安裝前，我們先來進行小規模的測試安裝：使用 Tracd 、 sqlite3。這種安裝方式十分簡單，如 下面5個步驟就結束了。



1.  # cd /your/trac/dir/path ; sudo python setup.py install
    --prefix=/usr/local/Trac
2.  # svnadmin create /wanted/svn/repository/path
3.  # export PYTHONPATH=/usr/local/Trac/lib/python2.4/site-packages/
4.  # /usr/local/Trac/bin/trac-admin /wanted/myproject/path initenv

-   並依序回答
-   專案名稱：XXXX(例如：我的第一個專案)
-   資料庫連結方式：sqlite:db/XXXX(例如：sqlite:db/first.db)
-   儲存庫格式：svn
-   儲存庫位置：/wanted/svn/repository/path
-   樣本資料夾：XXXX(就用它預設的吧)

5.  # /usr/local/Trac/bin/tracd --port 8000 /wanted/myproject/path


接下來，打開你的瀏覽器key上 http://localhost:8000/ 即可。結果如附圖。

`.. image:: http://4.bp.blogspot.com/_eKM9lHjTZjs/ReKST2Ogh0I/AAAAAAAAAC0/yBt
q4LcQsqk/s200/Screenshot-1.png
`_ `.. image:: http://1.bp.blogspot.com/_eKM9lHjTZjs/ReKSUGOgh1I/AAAAAAAAAC8
/_C-JfGPkPdw/s200/Screenshot-2.png
`_
到此我們可以確定 Trac 系統是可以運作的。而在下一篇文章，我們要把應用伺服器換成比較耐操、比較快的 `Apache2 加 mod_python`_ 。


> 為了讓大家了解 Trac 的強大，我架了一個`測試站`_給大家玩。我也會在這個站中，把 TracGuide
文件作一些簡單的中文介紹(不完全照翻)。使用的測試帳號/密碼如下：

ptra.hoamon.info /demo
www.hoamon.info / demo
album.hoamon.info / demo

以上請任選一組。


.. _接下來，打開你的瀏覽器key上 http://localhost:8000/ 即可。結果如附圖。: http://4.bp.blogspo
    t.com/_eKM9lHjTZjs/ReKST2Ogh0I/AAAAAAAAAC0/yBtq4LcQsqk/s1600-h/Screenshot
    -1.png
.. _                     :
    http://1.bp.blogspot.com/_eKM9lHjTZjs/ReKSUGOgh1I/AAAAAAAAAC8/_C-
    JfGPkPdw/s1600-h/Screenshot-2.png
.. _Apache2 加 mod_python: http://hoamon.blogspot.com/2007/02/trac_27.html
.. _測試站: http://ptrac.hoamon.info/


Old Comments in Blogger
--------------------------------------------------------------------------------



`yungyuc <http://www.blogger.com/profile/03040900487805390584>`_ at 2007-03-27T00:36:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Debian 有包 trac，我猜 ubuntu 也會有。懶的話 (像我) 就會直接用人家包好的 trac。

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2007-03-27T08:57:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我的習慣是網頁程式抓原廠的，而桌面程式、函式庫…這些，才用 linux 套件的。

.. author:: default
.. categories:: chinese
.. tags:: wiki, trac, subversion, sqlite, python, request ticket, apache, mod_python
.. comments::
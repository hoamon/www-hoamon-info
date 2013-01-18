Install Python2.5 on Ubuntu 11.04 x86_64 for Google App Engine
================================================================================

之前所提的「`Install Python2.5 on Ubuntu 10.04 i386 for Google App Engine`_」，主要是在
i386 Ubuntu 的安裝方式。我這一次換了電腦，也裝了 Ubuntu 11.04 amd64 的版本，所以安裝方式有些許不同：

1. 系統內建的 sqlite 函式庫無法連結。
2. 某些 .so 檔不再放在 /usr/lib ，而是在 /usr/lib32, /usr/lib64, /usr/lib/x86_64
    -linux-gnu 等地。

另外在安裝 python2.5 時，也想順便套上 readline 及 ipython 。以下是安裝過程：

先裝上 Ubuntu 內建的函式庫：

$ apt-get install liblcms1-dev zlib1g-dev libfreetype6-dev libjpeg62-dev
libsqlite3-dev libssl-dev tk-dev libreadline-dev

安裝 sqlite3：

$ cd sqlite-autoconf-3070603/
$ ./configure --prefix=/usr/local/sqlite3 --enable-readline --enable-
threadsafe --enable-dynamic-extensions
$ make && sudo make install

安裝 Python2.5.6：

$ cd Python2.5.6/
$ ./configure --prefix=/usr/local/python25 --with-zlib -with-zlib-
library=/usr/lib/x86_64-linux-gnu --with-zlib-include=/usr/include --with-tk
--with-tk-library=/usr/lib32 --with-tk-include=/usr/include --with-tcl
--with-tcl-library=/usr/lib32 --with-tcl-include=/usr/include
--libdir=/usr/local/sqlite3/lib --includedir=/usr/local/sqlite3/include
--with-freetype2 --with-jpeg --with-readline
$ make && sudo make install

安裝 ipython

$ cd ipython/
$ sudo /usr/local/python25/bin/python2.5 setup.py install

安裝 GAE 相依模組 ipaddr：

$ cd ipaddr-2.1.1/
$ sudo /usr/local/python25/bin/python2.5 setup.py install

安裝 GAE 相依模組 python-ssl：

$ cd python-ssl-1.15/
$ cp -rf ../Python2.5.6/Include/* /usr/local/python25/include/ # 需要 Python 源碼
$ sudo /usr/local/python25/bin/python2.5 setup.py install

安裝 PIL：

修改 Imaging-1.1.7/setup.py 中的參數如下：

TCL_ROOT = '/usr/lib32'
JPEG_ROOT = '/usr/lib32'
ZLIB_ROOT = '/usr/lib/x86_64-linux-gnu/'
TIFF_ROOT = '/usr/lib32'
FREETYPE_ROOT = '/usr/lib32'
LCMS_ROOT = '/usr/lib32'

檢查模組是否可使用

$ /usr/local/bin/python2.5 setup.py build_ext -i

測試模組

$ /usr/local/bin/python2.5 selftest.py

看到如下訊息，就代表模組皆有支援

　--- PIL CORE support ok
　--- TKINTER support ok
　--- JPEG support not installed
　--- ZLIB (PNG/ZIP) support not installed
　--- FREETYPE2 support ok
　--- LITTLECMS support ok

再執行

$ sudo /usr/local/python25/bin/python2.5 setup.py install

最後，再把 dev_appserver.py, appcfg.py 中的 #!/usr/bin/env python 改成 #!/usr/bin/env
python2.5 即可(也不是必須的，只要你知道執行 GAE server 時是用 python2.5 就夠了)。

完成後就可以在 Ubuntu 11.04+ x86_64 中開發 GAE 程式了。

.. _Install Python2.5 on Ubuntu 10.04 i386 for Google App Engine:
    http://hoamon.blogspot.com/2010/05/install-python25-on-
    ubuntu-1004-for.html


.. author:: default
.. categories:: chinese
.. tags:: linux, python, amd64, google app engine, ubuntu, x86_64
.. comments::
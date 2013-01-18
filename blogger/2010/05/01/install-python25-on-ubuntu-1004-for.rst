Install Python2.5 on Ubuntu 10.04 i386 for Google App Engine
================================================================================

Ubuntu 10.04 已經預設不包 Python2.5 了，對寫 GAE 的人來說，這有點麻煩，到目前為止 `GAE 並未正式地支援 2.6`_
，所以最好認命地在 Ubuntu 10.04 中創建一個 Python2.5 的環境。




裝 2.5 的目的是為了開發 GAE 程式，所以我們需要額外下載這些程式碼：

1.  `Python2.5`_
2.  `PIL`_
3.  `python-ipaddr`_
4.  `python-ssl`_

# 利用 apt-get 安裝相關函式庫，除 libssl-dev 外，其他的套件是給 PIL 用的

$ sudo apt-get install liblcms1-dev zlib1g-dev libfreetype6-dev libjpeg62-dev
libsqlite3-dev libssl-dev




# 安裝 Python2.5.5 至 /usr/local

$ tar -jxf Python-2.5.5.tar.bz2

$ cd Python-2.5.5

$ ./configure -with-zlib-library=/usr/lib --with-zlib-include=/usr/include
--with-tk --with-tcl-library=/usr/lib --with-tcl-include=/usr/include --with-
tk-library=/usr/lib --with-tk-include=/usr/include

$ make

$ sudo make install




# 安裝 GAE 相依模組 ipaddr

$ tar -zxf ipaddr-2.1.1.tar.gz

$ cd ipaddr-2.1.1/

$ sudo /usr/local/bin/python2.5 setup.py install




# 安裝 GAE 相依模組 python-ssl

$ tar -zxf python-ssl-1.15.tgz

$ cd python-ssl-1.15/

$ sudo /usr/local/bin/python2.5 setup.py install




#安裝 PIL

$ tar -zxf Imaging-1.1.7.tar.gz

$ cd Imaging-1.1.7

# 修改 setup.py 中的使用函式庫位置

# LCMS_ROOT = '/usr/lib'

# TCL_ROOT = '/usr/lib'

# JPEG_ROOT = "/usr/lib"

# ZLIB_ROOT = "/lib"

# TIFF_ROOT = '/usr/lib'

# FREETYPE_ROOT = "/lib"




#檢查模組是否可使用

$ /usr/local/bin/python2.5 setup.py build_ext -i

#測試模組

$ /usr/local/bin/python2.5 selftest.py

　PIL 1.1.7 TEST SUMMARY

　--------------------------------------------------------------------

　Python modules loaded from ./PIL

　Binary modules loaded from ./PIL

　--------------------------------------------------------------------

　--- PIL CORE support ok

　--- TKINTER support ok

　*** JPEG support not installed

　*** ZLIB (PNG/ZIP) support not installed

　--- FREETYPE2 support ok

　--- LITTLECMS support ok

　--------------------------------------------------------------------




雖然有過 build_ext ，但到了 selftest.py 時，我總是會得到 JPEG 及 ZLIB
兩種函式庫不支援的情形，但因為我的網頁程式不太用到影像處理的功能，所以我直接強制安裝 pil 。




$ sudo /usr/local/bin/python2.5 setup.py install




最後，再把 dev_appserver.py, appcfg.py 中的 #!/usr/bin/env python 改成 #!/usr/bin/env
python2.5 即可(也不是必須的，只要你知道執行 GAE server 時是用 python2.5 就夠了)。




完成後就可以在 Ubuntu 10.04+ 中開發 GAE 程式了。

.. _GAE 並未正式地支援 2.6:
    http://code.google.com/p/googleappengine/issues/detail?id=757
.. _Python2.5: http://www.python.org/
.. _PIL: http://www.pythonware.com/products/pil/
.. _python-ipaddr: http://code.google.com/p/ipaddr-py/
.. _python-ssl: http://pypi.python.org/pypi/ssl


.. author:: default
.. categories:: chinese
.. tags:: linux, python, google app engine, ubuntu
.. comments::
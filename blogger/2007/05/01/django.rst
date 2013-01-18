django處理靜態資料的方法
================================================================================

感謝 `yungyuc`_ 提醒，我看過 stitac_files 文件後，重新整理如下：

方法目前有3種：
1、使用 mod_python
利用高效率的 Apache 幫你處理，設定檔範例如下：
::** 1 ****<VirtualHost**** *:80****>**
    ** 2 **    **ServerName** somedomain
    ** 3 **    **<Location**** "/"****>**
    ** 4 **        **SetHandler** python-program
    ** 5 **        PythonHandler django.core.**handlers**.modpython
    ** 6 **        PythonPath **"['/path/to/djangoproject_parentpath'] +
    sys.path"**
    ** 7 **        **SetEnv** PYTHON_EGG_CACHE /tmp
    ** 8 **        **SetEnv** DJANGO_SETTINGS_MODULE
    djangoprojectname.settings
    ** 9 **        PythonDebug **Off**
    **10 **    **</Location>**
    **11 **    **Alias** /media
    /path/to/djangoproject_parentpath/djangoprojectname/media
    **12 **    **<Location**** "/media"****>**
    **13 **        **Options** **None**
    **14 **        **SetHandler** **None**
    **15 **    **</Location>**
    **16 **    **ErrorLog** /var/log/apache2/somedomain_error.log
    **17 **    **LogLevel** **warn**
    **18 **    **CustomLog** /var/log/apache2/somedomain_access.log
    combined
    **19 ****</VirtualHost>**

這種方式應該只用在 product (上線模式) 中，在程式開發時，是不應使用這種方法的(除非你不厭其煩地下 sudo service httpd
restart)。而這種方式的輸出效率是最快的，不須透過其他程式，直接從 Apache 輸出，但缺點是沒有彈性，如果你的專案中，有分多個 apps
的話，你得手動把 apps/media 放到 media 中。但這點麻煩還算可以忍受的，如果你的網站是成千上萬人用的話。

2、使用 django.views.static.serve 函式
在你的 urls.py 中設定如下：

(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
'/path/to/media', 'show_indexes': True}),

show_indexes 選項的意思是「要秀出這個資料夾下的所有檔案嗎」，預設是 False ，也建議你用 False 。
'/path/to/media' 可以是相對路徑也可以是絕對路徑。而 site_media 不要與你的 settings.py 中的
ADMIN_MEDIA_PREFIX 設定相同。相同的話，會造成上線模式及開發模式的行為有所不同，增加困惱。

使用這種方法的優點是你的 media 資料夾可以跟著 apps 跑，而且上線及開發模式所使用的資料夾架構是一樣的。缺點是少了效率及多了安全隱憂。

3、使用 `limodou`_ 開發的 ` staticview.py`_
staticview.py 是延伸了 django.views.static 的程式，多了一項功能，可以比對整個專案下 apps 的 media
資料夾，讓你的靜態文件，只需要放在某一個 app/media 下即可。設定方式略有不同：

(r'^site_media/(?P<path>.*)$', ' myprj.utils.staticview.serve',
{'document_root': '/path/to/media', 'app_media_folder':'media',
'show_indexes': True}),

多一個 app_media_folder 設定值。

本文已修改，若要看舊版錯誤，請看本文的原始碼。



.. _yungyuc: http://blog.seety.org/everydaywork/
.. _limodou: http://blog.donews.com/limodou/
.. _ staticview.py:
    http://openbookplatform.googlecode.com/svn/trunk/utils/staticview.py


Old Comments in Blogger
--------------------------------------------------------------------------------



`yungyuc <http://www.blogger.com/profile/03040900487805390584>`_ at 2007-05-12T00:38:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我看不出 http://www.djangoproject.com/documentation/static_file 哪裡有說不能用在產用
(production) 模式裡；只是不建議，不是不能用。

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2007-05-12T10:07:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我是在`這裡`_看到的，但因為文件我是跳著看的，所以我沒有看到 static_files 這一篇。感謝 yungyuc 。等我看完
static_files ，再重寫本文。

.. _這裡: http://www.djangoproject.com/documentation/modpython/#serving-
    media-files


.. author:: default
.. categories:: chinese
.. tags:: django
.. comments::
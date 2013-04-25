Trac安裝筆記(下)
================================================================================

:doc:`上一篇文章 <./trac>` 我們談了使用內建的 Tracd 來執行 Python 的 CGI 程式，\
本篇文章則是要介紹用 Apache2 + mod_python 來跑 Trac 程式。

事實上，這沒什麼難度，3個步驟就結束了：

1.  安裝 mod_python
2.  設定 apache.conf
3.  設定 .htpasswd

.. more::

1 的步驟看各家套件， Ubuntu 的是這樣：

.. code-block:: bash

    # sudo apt-get install libapache2-mod-python

2 的步驟請將下列設定放到你的 `apache 設定檔 <http://hoamon.blogspot.com/2006/11/apache.html>`_ 中。

.. code-block:: apache

    <virtualhost>
        ServerAdmin some@some
        ServerName ptrac.hoamon.info
        DocumentRoot /mnt/A2/PTrac
        <location /repository>
            #這個設定是讓你可以使用 svn co http://ptrac.hoamon.info/repository/svn/XX
            DAV svn
            SVNParentPath /mnt/A2/PTrac
            AuthType Basic
            AuthName "if you have no idea about account / password, and you can
    type hoamon / demo"
            AuthUserFile /mnt/A2/PTrac/.htpasswd
            # .htpasswd 放置我們所設定的帳號/密碼
            Require valid-user
            Satisfy Any
        </location>
        <location />
            SetHandler mod_python
            PythonHandler trac.web.modpython_frontend
            PythonPath "sys.path+['/usr/local/Trac/lib/python2.4/site-
    packages/']"
            PythonDebug On
            #當系統正式上線時，請將 PythonDebug Off
            PythonOption TracEnv /mnt/A2/PTrac/tracwww
            # tracwww 就是你之前用 trac-admin 所創建的專案資料夾
            PythonOption TracUriRoot /
            # 這個 / 與 Location 的 / ，應該是一樣的
            SetEnv PYTHON_EGG_CACHE /mnt/A2/PTrac/tractmp
            #如果你有用到 egg 格式的外掛，才須要設定
        </location>
        <location /login>
            AuthType Basic
            AuthName "Trac Server"
            AuthUserFile /mnt/A2/PTrac/.htpasswd
            Require valid-user
        </location>
        ErrorLog logs/PTrac-error.log
        LogLevel warn
        CustomLog logs/PTrac-access.log combined
        ServerSignature Off
    </virtualhost>

3 的步驟則是建立一個帳號/密碼檔：

.. code-block:: bash

    # sudo htpasswd -c /mnt/A2/PTrac/.htpasswd hoamon
    # Type your Password
    # Type your Password twice

接下來，重開 apache 即可。

另外在使用 Trac 時，如果能配合一些外掛，那將更得心應手。下面是主要的3種外掛的裝法。

.. code-block:: bash

    # sudo easy_install http://svn.edgewall.com/repos/trac/sandbox/webadmin
    # sudo easy_install http://trac-hacks.org/svn/iniadminplugin/trunk/
    # sudo easy_install http://trac-hacks.org/svn/accountmanagerplugin/0.10

要使用 easy_install 指令安裝前，請先安裝 python-setuptools 。\
webadmin 外掛是讓你可以用網頁的方式來作系統的設定，\
而 iniadmin 及 accountmanager 則是嵌在 webadmin 頁面中，\
讓你可以作帳號管理及 trac.ini 檔的管理。

安裝好外掛好，把下面內容加入 trac.ini 中，區塊順序不重要。

.. code-block:: ini

    [account-manager]
    password_file = /mnt/A2/PTrac/.htpasswd
    password_store = HtPasswdStore

    [components]
    acct_mgr.admin.accountmanageradminpage = enabled
    acct_mgr.api.accountmanager = enabled
    acct_mgr.htfile.htpasswdstore = enabled
    acct_mgr.web_ui.accountmodule = enabled
    acct_mgr.web_ui.loginmodule = enabled
    acct_mgr.web_ui.registrationmodule = enabled
    iniadmin.iniadmin.iniadminplugin = enabled
    trac.web.auth.loginmodule = enabled
    webadmin.* = enabled

最後加入 admin 的權限即可。 XXXXX 表你的系統管理員帳號。

.. code-block:: bash

    # trac-admin /mnt/A2/PTrac/tracwww permission add XXXXX TRAC_ADMIN

而如果你不想要給匿名使用者權限的話，請執行下面這一行。

.. code-block:: bash

    # trac-admin /mnt/A2/PTrac/tracwww permission remove anonymous *

最後，當你使用系統管理員帳號登入後，就可以看到選單上多了 admin 的連結了。

延伸閱讀： `在 Windows 上使用 Trac on Apache - 使用說明篇 <http://blog.roodo.com/jaceju/archives/2772843.html>`_

.. author:: default
.. categories:: chinese
.. tags:: trac, python, apache, mod_python
.. comments::
把 Mercurial 用 mod_python 裝在 Apache 中
================================================================================

實際上， Mercurial 這種分散式版本控制器是不太需要架個 Web Server 來 Run 的，尤其是我多半都是獨自在寫程式，但架了個 Web
Server 後，我會比較方便在多台個人電腦中轉移陣地，且這也多了一種備份的機制。

不過，目前已有人將 hg 成功移植成 GAE 版(hg-repos.appspot.com)，現在只待作者把說明文件完成，我就會將跑在 apache
上的部份儲存庫再移至 GAE 去。

廢話不多說，透過 mod_python 來跑 HTTPS 版的 Mercurial 儲存庫方式如下：

一、 下載 modpython_gateway.py ，載點何處? Google 比較快且安全。下載後放到 /raid1/A2B2/www/HG/
(可自行更換其他資料夾) ，也就是在 apache.conf 中所設定 PythonPath 。此檔案內容不用修改。

二、 設定如何執行 modpython_gateway.py ，一樣在 /raid1/A2B2/www/HG/ 下，新增一個 hgwebdir.py
，其內容如下：
::
    import os
    os.environ["HGENCODING"] = "UTF-8"

    from mercurial.hgweb.hgweb_mod import hgweb
    from mercurial.hgweb.hgwebdir_mod import hgwebdir
    from mercurial.hgweb.request import wsgiapplication

    def make_web_app():
        return hgwebdir("/raid1/A2B2/www/HG/hgweb.config")

    def test(environ, start_response):
        toto = wsgiapplication(make_web_app)
        return toto (environ, start_response)


三、 設定你的檔案庫位置，一樣在 /raid1/A2B2/www/HG 下新增一個 hgweb.config 其內容如下：
::
    [paths]
    /trachg = /raid1/A2B2/www/trac/hg

    [collections]
    #我把 /raid1/A2B2/www/HG/product soft link 到 /product
    #這樣在連結上，才會是用 /product/product1 來觀看 product1 儲存庫。
    /PathDoesNotMatter = /product/

    [web]
    style = gitweb
    allow_archive = bz2 gz zip


四、 apache.conf 設定如下：

<virtualhost *:443>
--ServerSignature Off
--ServerName hg.yoursite.name
--DocumentRoot /raid1/A2B2/www/HG/tmp
--RewriteEngine On
--RewriteRule ^/(.*) /DoesNotMatter/$1
--<Location />
----PythonPath "sys.path + [ '/raid1/A2B2/www/HG' ]"
----#PythonDebug On #Uncomment this ligne if you got a problem and need debug
information
----SetHandler mod_python
----PythonHandler modpython_gateway::handler
----#PythonOption SCRIPT_NAME /repo
----PythonOption wsgi.application hgwebdir::test
----AuthType Basic
----AuthName "Mercurial Repository"
----AuthUserFile /raid1/A2B2/www/auth_users
----Require valid-user
--</Location>
--LogLevel warn
--ErrorLog /var/log/apache2/hg_error.log
--CustomLog /var/log/apache2/hg_access.log combined
--SSLEngine On
--SSLCertificateFile /etc/apache2/ssl/apache.pem
</virtualhost>

五、 重啟 apache

你就會在 https://hg.yoursite.name/ 中，看到 trachg 、 product/product1 、
product/XXXproduct ... 的儲存庫了。

Old Comments in Blogger
--------------------------------------------------------------------------------



`yungyuc <http://www.blogger.com/profile/03040900487805390584>`_ at 2009-02-11T23:24:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

為什麼用比較麻煩的 mod_python，不用 fcgi?

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2009-02-12T06:53:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

嘿嘿~因為我用習慣 mod_python 了。還沒有機會裝 fastcgi

.. author:: default
.. categories:: chinese
.. tags:: mercurial, apache, mod_python
.. comments::
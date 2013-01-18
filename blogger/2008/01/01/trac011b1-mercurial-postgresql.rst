Trac0.11b1 + Mercurial + Postgresql
================================================================================

基於對 Python 的喜愛，所以想要把 subversion 換成 Mercurial ，但目前還只是測試階段，真正上線使用的還是 subversion
。另外一直都想要找個機會把 Mysql 換掉，到不是說 Mysql 不好用，而是我對於 PostgreSQL 本來就有一分感情，那是在 Mysql3,4
還不支援 UTF-8 時，我用 Perl 寫了一個 unicode 字的查詢系統。

而今天所要介紹的，不過是我在工餘之際把玩的小小玩意，既然成功了，那就作個紀錄。

在 Ubuntu 安裝軟體是一點都不難的(只要有 .deb 檔)，所以要裝 Trac + PostgreSQL + Mercurial ，請執行下面指令：

# sudo apt-get install postgresql-client-8.2 postgresql-8.2 python-psycopg2 \
> python-setuptools python-genshi \
> python-psycopg2 python-pygments python-docutils mercurial

接下來，安裝 Trac 0.11b1 主程式
# sudo easy_install http://ftp.edgewall.com/pub/trac/Trac-0.11b1.tar.gz

最後安裝 Trac 控制 Mercurial 的外掛
# svn co http://svn.edgewall.com/repos/trac/sandbox/mercurial-plugin-0.11
# cd mercurial-plugin-0.11/
# sudo python setup.py install

再來是設定，首先我們建立一個 dbuser ，這方面， PostgreSQL 有點奇怪，或許是我 Mysql 用久了，
# sudo -u postgres createuser trac -P
Enter password for new role:
再輸入一次:
Shall the new role be a superuser? (y/n) n
Shall the new role be allowed to create databases? (y/n) n
Shall the new role be allowed to create more new roles? (y/n) n
CREATE ROLE
# sudo createdb -O trac trac
並將 pg_hba.conf 中的
local all all ident sameuser
改成
local all all password

這樣你的 trac 程式就可以透過帳號: trac 密碼: trac host: localhost 的方式與 PostgreSQL 連接了。

接下來，初始化 trac 設定目錄及 hg 儲存庫：
# trac-admin /path/to/myproject initenv
# hg init /path/to/myproject/hg

另外在 trac.ini 中加入
[components]
tracext.hg.* = enabled

[hg]
show_rev = yes
node_format = short

用 tracd --port 8000 /path/to/myproject 測試一下有沒有問題，沒有問題就讓 mod_python 來跑吧!

下面則是 mod_python 的設定檔
::
    NameVirtualHost *:443

      ServerAdmin admin@xxx.com
      ServerName trac.xxx.com
      DocumentRoot /www/trac

          SetHandler mod_python
          PythonHandler trac.web.modpython_frontend
          #PythonPath "sys.path+['/usr/local/Trac/lib/python2.5
          /site-packages/']"
          PythonOption TracEnv /www/trac
          PythonOption TracUriRoot /
          PythonDebug Off
          SetEnv PYTHON_EGG_CACHE /www/trac/tmp
          SetEnv LANG UTF-8
          SetEnv HTTPS 1
          AuthType Basic
          AuthName "Trac Server"
          AuthUserFile /www/htpasswd_users
          Require valid-user

      ErrorLog /var/log/apache2/trac_error.log
      LogLevel warn
      CustomLog /var/log/apache2/trac_access.log combined
      ServerSignature Off
      SSLEngine On
      SSLCertificateFile /etc/apache2/ssl/apache.pem



.. author:: default
.. categories:: chinese
.. tags:: mercurial, trac, subversion, python, postgresql
.. comments::
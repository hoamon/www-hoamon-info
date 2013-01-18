Django0.96與MySQLdb之間的小問題
================================================================================

使用 0.96 版有一個小麻煩，在 ubuntu 上所編入的 MySQLdb 是 1.2.1g3 版，但 0.96 要求使用 1.2.1p2
以上版本，這事不難辦，重裝一個 MySQLdb 就好了，問題是出在手動安裝 MySQLdb 套件時，需要使用 MySQL-server 的
mysql_config 指令，這個程式是包在 devel 套件中時，在 ubuntu 中，它的名字叫 libmysqlclient15-dev ，在
fedora 中，它叫作 mysql-devel 。麻煩的地方就在這， mysql_config 與 mysql-devel
兩個字看起來沒關係，所以我花了一段時間，才找到應該要裝的是這個套件。詳細指令如下：

::$ sudo apt-get install libmysqlclient15-dev
    $ cd MySQLdb-1.2.2 ; # edit site.cfg; set
    mysql_config=/usr/bin/mysql_config
    $ sudo python setup.py install


.. author:: default
.. categories:: chinese
.. tags:: mysqldb, django, mysql, python
.. comments::
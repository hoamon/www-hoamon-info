在 django-based 系統中，將MyISAM 轉換成 InnoDB
================================================================================

詳細請見`官方文件`_。

我簡單整理如下：

一、將 settings.py 中的資料庫引擎從 MyISAM(預設值) 換成 InnoDB , 加下以下設定，

::
    DATABASES = {
        'default': {
            'NAME': 'xxx',
            'USER': 'xxx',
            'PASSWORD': 'xxx',
            'ENGINE': 'mysql',
            'OPTIONS': {
                "init_command": "SET storage_engine=INNODB",
            },
        }
    }


二、將原來的表格作

::
    mysql> ALTER TABLE ????? ENGINE=INNODB;


至於第二種方法該如何處理，我是使用 mysql 指令手動處理：

::
    mysql> \T /home/hoamon/alter.sql;
    mysql> show tables;
    mysql> \q;
    sh# perl -i -pe 's/| +([^ ]+) +|/ALTER TABLE \1 ENGINE=INNODB;/g'
    /home/hoamon/alter.sql
    sh# mysql -u xxx -pxxx xxx < /home/hoamn/alter.sql


我在將 MyISAM => InnoDB 時，遇到一個問題 MySQL Error code 1071錯誤('Specified key was too
long; max key length is 767 bytes')。

因為原本的 models.py 有一個 Model 設定了 unique_together = (('name', 'uplevel_id'), )
，而它會造成 1071 Error code，因為 name 的原長度是 256 ，而我們又使用 utf8 ，所以它的實際長度為 256 * 3 =
768 ，但在 InnoDB 的索引中，限制為 767 以下，所以我們必須將 name 的長度限制改為 255 才行。

.. _官方文件:
    http://docs.djangoproject.com/en/dev/ref/databases/?from=olddocs


.. author:: default
.. categories:: chinese
.. tags:: django, mysql, python, perl
.. comments::
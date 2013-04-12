Django 在使用 MySQL 或 PostgreSQL 時的差別(關於 autocommit )
================================================================================

.. figure:: mysql.png

    MySQL 的圖示，非 hoamon 著作

.. figure:: postgresql.gif

    PostgreSQL 的圖示，非 hoamon 著作

因為 Oracle 買下 MySQL 的關係，再加上我們有了新業主，\
所以本研究室( `NCHU-CM.COM <http://www.nchu-cm.com>`_ )確定放棄使用 MySQL 作為我們網頁系統的後端資料庫。\
未來改以 `PostgreSQL <http://www.postgresql.org/>`_ 為主。

也因為我們使用 `Django <http://www.djangoproject.com/>`_ 作為主要開發框架，\
理論上只要在 DATABASE ENGINE 換個設定，從 mysql 改成 postgresql_psycopg2 ，\
一切應該是馬照跑、舞照跳的。但世事如此美好，人類怎麼能進步呢？ \
有問題就是給我們成長的機會。

所以我們遇到一個 DatabaseError 訊息。

.. raw:: html

    <div style="background-color: #E5E5E5;"><h3>DatabaseError at /</h3>
    <h5>current transaction is aborted, commands ignored until end of transaction block</h5></div>

這個問題出現時，往往與真正出錯的訊息無關，它是指我們的錯誤報告儲存工具無法把本次錯誤訊息紀錄下來。\
也就是本次錯誤可能是因為 IntegrityError 或是 DatabaseError(欄位值超過 model 預設長度) ... 等，\
但是它一律出現 DatabaseError(current transaction is aborted, commands ignored until end of transaction block) 。

.. more::

原因就出在我們過去使用 MySQL InnoDB 時，並未開啟 autocommit 。但到了 PostgreSQL 時，\
它預設使用 read committed 模式。

下面是預設執行時所產生的 SQL LOG(settings.DATABASES['default']['OPTIONS']['autocommit']=False)， \
Django(或 psycopg2) 會以 read committed 模式去跑 transaction 。\
所以在跑一批 SQL 語句時，會在前面加上 BEGIN ，並在最後面會加上 END ，\
但本批次的 SQL 語句中途有錯（current transaction is aborted, commands ignored until end of transaction block），\
所以被 PostgresQL 中斷執行，並自動補上 ROLLBACK 。

.. code-block:: sql

    LOG:  statement: SHOW default_transaction_isolation
    LOG:  statement: SET default_transaction_isolation TO DEFAULT
    LOG:  statement: SET TIME ZONE 'UTC'
    LOG:  statement: SET default_transaction_isolation TO 'read committed'
    LOG:  statement: BEGIN
    LOG:  statement: SELECT "django_session"."session_key",
                        "django_session"."session_data",
                        "django_session"."expire_date"
                        FROM "django_session" WHERE
                        ("django_session"."session_key"
                        = 'f1d73aead869d513c72898c'
                        AND "django_session"."expire_date"
                        > '2013-04-12 04:58:51.112841+00:00' )
    LOG:  statement: SELECT cache_key, value, expires
                        FROM "xxx_cache"
                        WHERE cache_key = ':1:public_key_n'
    ERROR:  relation "xxx_cache" does not exist at character 39
    STATEMENT:  SELECT cache_key, value, expires
                    FROM "xxx_cache"
                    WHERE cache_key = ':1:public_key_n'
    LOG:  statement: SELECT "ho600_lib_bugpage"."id",
                        ...
                        FROM "ho600_lib_bugpage"
                        WHERE "ho600_lib_bugpage"."code" = '8Z69'
    ERROR:  current transaction is aborted,
                    commands ignored until end of transaction block
    STATEMENT:  SELECT "ho600_lib_bugpage"."id",
                    ...
                    FROM "ho600_lib_bugpage"
                    WHERE "ho600_lib_bugpage"."code" = '8Z69'
    LOG:  statement: ROLLBACK

也因為如此，本來系統在執行出錯時，是會被我們的 bugrecord 模組捕抓到，\
並偷天換日地把實際錯誤寫入資料庫，再拋出一個提醒用戶的 500 頁面，\
雖然它還是 HTTP500 ，但它是我們預料中的 HTTP500 。

可是因為在 read commited 模式，所有的 SQL 語句都會被包在 BEGIN ... END 中。
這樣若在 BEGIN ... END 中有錯（relation "xxx_cache" does not exist）卻未作好 ROLLBACK ，
直接在錯誤後面插入一個 SELECT SQL 語句（ bugrecord 會先查有無歷史錯誤，若無才寫入本次錯誤報告），\
這樣就引發了 PostgresQL 本身的 DatabaseError 了。

我們可以改使用 autocommit = True ，讓每句 SQL 本身都是 transaction ，單句 SQL 出錯， \
PostgresQL 會直接對該句作 rollback 動作，這樣就不會引發 PostgresQL 的 DatabaseError 。

.. code-block:: sql

    LOG:  statement: SHOW default_transaction_isolation
    LOG:  statement: SET default_transaction_isolation TO DEFAULT
    LOG:  statement: SET TIME ZONE 'UTC'
    LOG:  statement: SELECT "django_session"."session_key",
                            "django_session"."session_data",
                            "django_session"."expire_date"
                            FROM "django_session"
                            WHERE ("django_session"."session_key"
                            = 'd73aead869d513c72898c32'
                            AND "django_session"."expire_date"
                            > '2013-04-12 05:35:21.358909+00:00' )
    LOG:  statement: SELECT cache_key, value, expires FROM
                            "xxx_cache"
                            WHERE cache_key = ':1:public_key_n'
    ERROR:  relation "xxx_cache" does not exist at character 39
    STATEMENT:  SELECT cache_key, value, expires FROM "xxx_cache"
                    WHERE cache_key = ':1:public_key_n'
    LOG:  statement: SELECT "ho600_lib_bugpage"."id",
                            ...
                            FROM "ho600_lib_bugpage"
                            WHERE "ho600_lib_bugpage"."code" = '659K'
    LOG:  statement: INSERT INTO "ho600_lib_bugpage"
                            ("kind_id", ...)
                            VALUES (NULL, ...)
                            WHERE "ho600_lib_bugpage"."id" = 38
    LOG:  statement: SELECT "ho600_lib_bugkind"."id",
                            ...
                            FROM "ho600_lib_bugkind"
                            WHERE "ho600_lib_bugkind"."id" = 9
    LOG:  statement: SELECT (1) AS "a" FROM "ho600_lib_bugkind"
                            WHERE "ho600_lib_bugkind"."id" = 9  LIMIT 1
    LOG:  statement: UPDATE "ho600_lib_bugkind" SET
                            ...
                            WHERE "ho600_lib_bugkind"."id" = 9
    LOG:  statement: SELECT "django_site"."id",
                            "django_site"."domain",
                            "django_site"."name"
                            FROM "django_site"
                            ORDER BY "django_site"."id" ASC LIMIT 1
    LOG: ...
    LOG: ...

上面是改用 autocommit=True 後的 SQL LOG 。發生 ERROR 後，還是可以一直跑後續的 SQL 語句。

.. author:: default
.. categories:: none
.. tags:: none
.. comments::

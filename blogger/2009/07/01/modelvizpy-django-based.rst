使用 modelviz.py 來製作 Django-Based 應用系統的資料庫結構圖
================================================================================

要看懂應用系統的運作原理，從資料庫下手是一定要的。

了解了資料庫結構後，對其他執行方法的解讀就容易了。當然如果原本開發的人，其想法與別人太不一樣的話，在「他是比較優秀」的原因下，那對後面來看系統的人來說，就
是一種莫大的幫助; 如果是程度太低的話，那就只能怪當初給他作教育訓練的人。為什麼程式設計師那麼不長進，還讓他開發系統。

如果系統是使用 django 架構開發出來的，那麼在資料表的展示上，我們可以使用 `modelviz.py`_ 程式，把資料表結構匯出成 dot
格式，然後再利用 `Graphviz`_ 軟體繪製成 PNG 圖檔。

這個方法理論上是可以在 Linux/Mac/Windows 上運作的，不過，你知道的，我愛用 Linux ，所以我保證在 Linux
可以這麼作，其他系統就有賴你們了。

首先是使用 modelviz.py 把 app 的資料表內容及關係匯出成 dot 格式。在 settings.py 同一層的資料夾中，鍵入

> ./modelviz.py [-d] project general > XXX.dot

project, general 是我的 app name，看你想知道那些 app 的資料表關係，就填那些。且你想知道的 app ，必須是有存在於
settings.py 的 INSTALLED_APPS 中的。另外在有加 -d 的情況下，它不會列出資料表的欄位，只顯示關係。

有了 XXX.dot 後，再利用 Graphviz 軟體把它轉成圖檔。

> dot XXX.dot -Tpng -o XXX.png

這樣你就可以從 XXX.png 中了解這些資料表之間的關係了。

如下圖：

`.. image:: http://4.bp.blogspot.com/_eKM9lHjTZjs/SlKk2leNLRI/AAAAAAAAB7k
/RQWYe3o-CnU/s400/cim.png
`_

其中，可以看到 User, Company 兩個表格並沒有顯現它們的欄位，這是因為這兩個表格處於 user app 中，但我並沒有在
modelviz.py 指令中要求它要秀出這個 app 。

.. _modelviz.py: http://code.djangoproject.com/wiki/DjangoGraphviz
.. _Graphviz: http://www.graphviz.org/
.. _如下圖：: http://4.bp.blogspot.com/_eKM9lHjTZjs/SlKk2leNLRI/AAAAAAAAB7k
    /RQWYe3o-CnU/s1600-h/cim.png


.. author:: default
.. categories:: chinese
.. tags:: modelviz, django, linux, graphviz
.. comments::
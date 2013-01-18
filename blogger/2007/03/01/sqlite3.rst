sqlite3的資料備份及回復
================================================================================

因為我的系統從 fedora 改成 ubuntu 6.10 ，造成 trac 系統無法運作，它出現的錯誤訊息是：

Command failed: unsupported file format

查了一下，問題是出在 ubuntu 的 sqlite3 版本不夠新，所以無法讀取之前 fedora 的 db 檔。這問題不大，把 db 檔的資料 dump
出來，再用舊版本的 sqlite3 import 進去就行了。

$ sqlite3 xxx.db .dump > xxx.sql # 在 fedora 上執行 $ sqlite3 xxx.db < xxx.sql #
在 ubuntu 上執行

這樣你的 db 檔就可以給 trac 用啦。

.. author:: default
.. categories:: chinese
.. tags:: linux, fedora, trac, sqlite, ubuntu
.. comments::
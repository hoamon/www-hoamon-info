Eclipse + PyDev + Django
================================================================================

到工具列上的 [Window] => [Preferences] => [PyDev] => [Interpretter - Python] ，把
PYTHONPATH 加入一個 New Folder 。
位置就是你的 django project 的所在位置，如果你的專案 settings.py 是在 C:\www\project\settings.py
，則你要設定的 PYTHONPATH 為 C:\www 。

然後到你的工具列上的 [Run] 去設定 ./manage.py runserver ，專案名為 project 、 module 為 manage.py
、引數為 runserver 。

目前惟一的問題時，啟動了 ./manage.py runserver 後，無法中斷它。只能利用 Windows 工作管理員 或是 Linux 下的
kill 指令來中斷。

.. author:: default
.. categories:: chinese
.. tags:: django, eclipse, PyDev
.. comments::
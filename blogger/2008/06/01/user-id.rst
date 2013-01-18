找出舊 user id 的檔案，並全部改成新使用者的
================================================================================

sudo chown -R hoamon:hoamon `sudo find -uid 500|head -n 100`

因為找出來 uid=500 的檔案數太多了，所有用 head 截取前 100 個，多作幾次上面的指令就可以把目前目錄下 uid=500 的檔案擁有者改成
hoamon 了。

.. author:: default
.. categories:: chinese
.. tags:: linux
.. comments::
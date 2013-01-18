Mercurial 的 Windows 使用者應該要注意 \r 的問題
================================================================================

目前常見的作業系統有 Solaris, Ubuntu Linux, Fedora Linux, FreeBSD, XXX Linux, YYY BSD,
Mac OS X 及 Windows ，而這些系統中，除了 Windows 的換行符號是用 \r\n 外，其他的都是用 \n 。

所以當 Windows 使用者將他們的程式碼上傳至版本控制器時，換行符號會以 \r\n 為主，然後我們其他使用 Mac OS X 及 Ubuntu
Linux 的人，在上傳程式碼時，又可能會將換行符號換成 \n ，那麼在作版本比對的時候，只差 \r
的資料行也秀出來了，這實在不利於比對效率。不過這一點， NetBeans 倒是聰明地將只差 \r 及空白的資料行作忽略。

但話說回來，有時候，我們是在遠端 ssh 連線下，作設定檔或是程式碼的比對，這時候，如果出現一堆 ^M 符號也是挻困惱的。

所以這時候，就要請 Windows 使用者多作一個設定，讓他們在 push 檔案時，能自動將 \r 移除。

如果你安裝的是 TortoiseHg ，那麼請到你的安裝目錄下找一個 Mercurial.ini 的檔案，把它打開，加入下列內容：

[extensions]

hgext.win32text=


[encode]
** = cleverencode:


[decode]
** = cleverdecode:


[patch]
eol = crlf


[hooks]
pretxncommit.crlf = python:hgext.win32text.forbidcrlf

一般而言， extensions, encode, decode 區塊是預設就有的，只是需要移除註解，而 patch, hooks 則是自行增加。




這樣以後在作 push 時， hg 會事先把 \r 移除才送出去。

.. author:: default
.. categories:: chinese
.. tags:: mercurial, linux, windows, tortoisehg, solaris
.. comments::
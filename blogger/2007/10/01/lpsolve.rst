Lp_solve 安裝
================================================================================

lp_solve 是以 C 語言寫成的 Mixed Integer Linear Programming (MILP) solver ，所以基本上，你是用
C 語言的人是可以直接把它的函式庫包在所寫的程式中的。

但我們是用 Python 的人，那要如何能在 python 語言把 lp_solve 載入呢!要作到這個，你首先要知道 lpsolve55.dll
(windows)/liblpsolve55.so(unix) 就是 lp_solve 的函式庫，你只要有這個檔案，你就可以使用 C 語言來寫 MILP
應用了。

而用 Python 的人，則是要多安裝一個 lpsolve55.pyd(windows)/lpsolve55.so(unix) ，這個檔是 Python
與 lp_solve 函式庫的溝通者/包裝者，你的 Python 程式都是先載入
lpsolve55.pyd(windows)/lpsolve55.so(unix) ，然後它會幫你處理與 lpsolve55.dll
(windows)/liblpsolve55.so(unix) 的資料傳輸。

Ubuntu 7.04 版： 請到 `sourceforge.net`_ 下載 5.5.0.10 的檔案。

1.  lp_solve_5.5.0.10_dev.tar.gz - 裡面放的是 liblpsolve55.so
2.  lp_solve_5.5.0.10_Python_source.tar.gz - 裡面放的是 lpsolve55.so 的程式碼

把 liblpsolve55.so 放到你的 /usr/lib 下(而其他解出來的檔案則拿到
lp_solve_5.5.0.10_Python_source 的資料夾中，與 extra 同一層)。接下來確定你有安裝 python-dev
套件，如果沒有，你應該知道如何安裝它吧!(# sudo apt-get install python-dev)，接下來解開
lp_solve_5.5.0.10_Python_source.tar.gz ，進入到 extra/Python 中，執行 # sudo python
setup.py install 。

如果沒有意外出現的話，你可以在 python 直譯器中見到如下訊息：

::Python 2.5.1 (r251:54863, May  2 2007, 16:56:35)
    [GCC 4.1.2 (Ubuntu 4.1.2-0ubuntu4)] on linux2
    Type "help", "copyright", "credits" or "license" for more
    information.
    >>> from lpsolve55 import lpsolve
    >>> lpsolve()
    lpsolve  Python Interface version 5.5.0.5
    using lpsolve version 5.5.0.10

    Usage: [ret1, ret2, ...] = lpsolve('functionname', arg1, arg2, ...)


.. _sourceforge.net: https://sourceforge.net/project/showfiles.php?group_
    id=145213&package_id=159735&release_id=478442


.. author:: default
.. categories:: chinese
.. tags:: lp, python
.. comments::
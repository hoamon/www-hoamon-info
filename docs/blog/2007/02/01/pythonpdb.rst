Python: 簡易除錯模組 pdb
================================================================================

我很習慣用Vim來作任何有關文字編輯的工作，包含改設定檔、寫程式、寫網頁，\
甚至是大量改檔名的時候，我也是先用Vim編輯要打的指令之後才送shell處理。 Vim 真的是文字編輯領域的佼佼者。

然寫程式時，總要用到debug，而目前一般用來寫 perl、python 的 IDE 工具，像是 Eclipse、komodo 等，\
有方便的 debug 功能，卻少了像 Vim 般強大的編輯方法，使得我用起來總是少了那麼一點點的感覺。

還好如 perl、python 強大的語言，自己會帶著除錯工具。 perl 除錯器是在執行時帶入 -d 參數即可，如：

.. code-block:: sh

    # perl -d some.pl

而 python 則是提供一個模組 pdb 。本文即是一個 pdb 模組的簡易教學文件。

使用 pdb 模組十分簡單，在你的程式中載入 pdb 模組，並設定好中斷點，即可執行。程式範例如下：

.. code-block:: python
    :linenos:

    #!/usr/bin/python
    #本檔名為 pdb_example.py

    import pdb #載入pdb模組
    def complex_sum(x1, x2):
        print 'do something 1'
        value1 = 1 * x1
        value2 = 1 * x2
        return value1 + value2

    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    pdb.set_trace() #中斷點
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in a:
        for j in b:
            print complex_sum(i, j)

我在第 12 行設了一個中斷點。接下在 shell 中執行 python pdb_example.py ，執行後，它會給你一個(Pdb) 命令列。

進入 Pdb 後，它先到中斷點的下一行，本範例是 b = [1, 2, 3, 4, 5, 6, 7, 8, 9] ，\
但秀出的這一行實際上是還未執行的。如果整個程式你只有載入 pdb ，但未設定中斷點，\
則 python 會直接執行你的程式。事實上，你只要學會了 q、p、n、c、s、r、l、!，\
你就能輕易操作 python debugger 了。

執行任何程式，一定要先知道離開方法是什麼。打個 q ，按下 [Enter] 即可離開。\

| q(quit)：離開
| p [some variable](print)：秀某個變數的值
| n(next line)：下一行
| c(continue)：繼續下去
| s(step into)：進入函式
| r(return): 到本函式的return敘述式
| l(list)：秀出目前所在行號
| !： 改變變數的值

P.S. Vim 的離開指令是 [Esc]:q! ，不知道請勿使用 Vim 。

.. author:: default
.. categories:: chinese
.. tags:: python, pdb
.. comments::
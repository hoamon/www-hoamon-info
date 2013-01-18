Python: 簡易除錯模組 pdb
================================================================================

我很習慣用Vim來作任何有關文字編輯的工作，包含改設定檔、寫程式、寫網頁，甚至是大量改檔名的時候，我也是先用Vim編輯要打的指令之後才送shell處理。V
im真的是文字編輯領域的佼佼者。

然寫程式時，總要用到debug，而目前一般用來寫perl、python的IDE工具，像是eclipse、komodo等，有方便的debug功能，卻少了像V
im般強大的編輯方法，使得我用起來總是少了那麼一點點的感覺。

還好如perl、python強大的語言，自己會帶著除錯工具。perl除錯器是在執行時帶入-d參數即可，如：

**# perl -d some.pl
**
而python則是提供一個模組pdb。本文即是一個pdb模組的簡易教學文件。

使用pdb模組十分簡單，在你的程式中載入pdb模組，並設定好中斷點，即可執行。程式範例如下：

01-#!/usr/bin/python
02-#本檔名為 pdb_example.py
03-
04-import pdb #載入pdb模組
05-def complex_sum(x1, x2):
06-----print 'do something 1'
07-----value1-= 1 * x1
08-----value2-= 1 * x2
09-----return value1-+ value2
10-
12-a = [0,1,2,3,4,5,6,7,8]
13-pdb.set_trace()#中斷點
14-b = [1,2,3,4,5,6,7,8,9]
15-
16-for i in a:
17-----for j in b:
18---------print complex_sum(i, j)

我在第13行設了一個中斷點。接下在shell中執行 python pdb_example.py ，執行後，它會給你一個(Pdb) 命令列。

進入(Pdb) 後，它先到中斷點的下一行，本範例是 b = [1,2,3,4,5,6,7,8,9]
，但秀出的這一行實際上是還未執行的。如果整個程式你只有載入pdb，但未設定中斷點，則python會直接執行你的程式。事實上，你只要學會了q、p、
n、c、s、r、l、!，你就能輕易操作python debugger了。

q(quit)：離開
執行任何程式，一定要先知道離開方法是什麼。打個q，按下[Enter]即可離開。
(p.s. Vim的離開指令是 [Esc]:q! ，不知道請勿使用Vim)

p [some variable](print)：秀某個變數的值

n(next line)：下一行

c(continue)：繼續下去

s(step into)：進入函式

r(return): 到本函式的return敘述式

l(list)：秀出目前所在行號

!： 改變變數的值

.. author:: default
.. categories:: chinese
.. tags:: python, pdb
.. comments::
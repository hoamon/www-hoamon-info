python2.5真的與2.4有差
================================================================================

在 Ubuntu 上開發程式的環境是 2.5 ，但網頁伺服器是用 Fedora Core 5 ，所以它的版本還在 2.4
，已經跑過無數個程式了，一直都是相容的，直到今天。

在 2.5 中，抓日期物件如下：

dateobj = datetime.datetime.strptime('2007-1-1', '%Y-%m-%d').date()

但在 2.4 中，卻不能這樣用，因為 datetime.datetime 並沒有 strptime 函式。那麼 strptime 函式在那裡呢!在
time 下。所以要改成如下的寫法：

dateobj = datetime.date(*time.strptime('2007-1-1', '%Y-%m-%d')[:3])

這樣在 2.4 及 2.5 下才能同時正確執行。

不過，我認為 2.5 改得好，因為我一直認為 time 物件是用來抓時間用的，而 datetime 是用作時間日期格式轉換用的， strptime 放在
datetime.datetime 下比較適合。

.. author:: default
.. categories:: chinese
.. tags:: python25, linux, fedora, ubuntu
.. comments::
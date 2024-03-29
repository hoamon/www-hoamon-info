Python: def 函式中的變數空間
================================================================================

Python 有一個和其他語言不同的地方，這個奇異點有點奇怪。當然，這一定是我不懂這麼作有什麼好處的關係。

當我們宣告一個函式如下：

.. code-block:: python

    def func():
        print X

這個 X 變數的值，會從 func 函式中找尋區域變數定義，找不到就往整個程式的全域變數來作套用，\
再找不到，就會去找整個 python 直譯器所擁用的內建變數搜尋，再找不到，就會丟出一個 NameError 的例外訊息。

.. more::

而整個搜尋賦值的動作是在 func 呼叫時進行，並不是在宣告時進行的。

.. code-block:: python

    X = 20
    def func():
        print X
    X = 30
    func() # print 30
    X = 40
    func() # print 40

在這種特別尋值的機制下，有一點是須要注意的，如果你在函式中也定義 X 變數的話，\
那麼尋值動作必定停止在這個函式區塊中。所以下方的程式碼會產生一個區域變數未賦值的例外錯誤，\
因為 func 函式中已定義 X 變數，但在定義前卻已經要列印它，這時的 X 變數是無法套用全域值的。

.. code-block:: python

    X = 20
    def func():
        print X
        X = 10
    X = 30
    func() # throw UnboundLocalError Exception

最後一行會丟出一個 UnboundLocalError 。

.. author:: default
.. categories:: chinese
.. tags:: python
.. comments::
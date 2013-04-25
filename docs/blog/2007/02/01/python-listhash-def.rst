Python: 可變物件(list、hash)在 def 函式的引數傳遞部份有著特別的行為
================================================================================

很多語言在函式傳遞的部份，都是用記憶體位址來作傳遞，具有不同習性語言的，\
我只知道有 Perl 及 Linux shell script 而已。 Python 也是用記憶體位址來傳遞引數的。

.. more::

但在 Python 中，如果你傳入的引數是 :doc:`可變物件 <../../../2007/02/01/python>` 的話，\
那結果可能不是你所相像的那樣。

.. code-block:: python

    list = [1]
    def f(a, List):
        List.append(a)
        return List
    f(2, list) # List = [1, 2]
    f(3, list) # List = [1, 2, 3]
    f(4, list) # List = [1, 2, 3, 4]

上面的例子，我們可以看到 List 變數的值是一直附加進去的，\
原因出在於 f 函式傳入的第二個引數是 list 的記憶體位置，\
所以在f函式中所作的改變，也會影響 list 變數，\
也就造成 List 並不是從 [1] 開始附加的，而可能是由 [1, 2]、[1, 2, 3] 開始附加的。

下面例子中的引數也是可變物件，這也是值得你注意且當心的。\
如果設定 List 的預設值為可變物件時，結果應該也不會是你所想要的。

.. code-block:: python

    def g(a, List = []):
        List.append(a)
        return List
    g(2) # List = [2]
    g(3) # List = [2, 3]
    g(4) # List = [2, 3, 4]

如果你希望在不傳入 List 變數值時，能使用 [] 作為預設值的話，你應該改成下面的寫法：

.. code-block:: python

    def h(a, List = None):
        if List is None: List = []
        List.append(a)
        return List
    h(2) # List = [2]
    h(3) # List = [3]
    h(4) # List = [4]

這樣回傳的結果會比較接近你的期待。

.. author:: default
.. categories:: chinese
.. tags:: hash, python, list
.. comments::
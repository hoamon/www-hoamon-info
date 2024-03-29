python trick: 可變物件應用在簡寫的賦值表示式上
================================================================================

我在`Python: 可變物件(list、hash)在 def 函式的引數傳遞部份有著特別的行為`_已經談過可變物件在函式傳址時的特別行為。

再來談談在簡寫的賦值表示式時，會遇到的陷阱。我們利用 a = b = [] 表示式來作到 a = []; b = []; 應用如下：
::**1 ****if** __name__ == **'__main__'**:
    **2 **    a = b = []
    **3 **    **for** i **in** range(1,3):
    **4 **        a.append(i)
    **5 **        b.append(**2** * i)
    **6 **    **print** **'a: %s'** % a
    **7 **    **print** **'b: %s'** % b
    上式結果為：
a: [1, 2, 2, 4]
b: [1, 2, 2, 4]

是不是和你想的：
a: [1, 2]
b: [2, 4]
不一樣。

原因在於使用 a = b = [] 時，它也表示 a = b ，而又因為你賦給它們的值是一個可變物件 [] ，所以 a 實際上得到的是 b
的記憶體位址。於是你改變 a ，同時也改變了 b ，改變了 b ，也改變了 a 。

.. _Python: 可變物件(list、hash)在 def 函式的引數傳遞部份有著特別的行為:
    http://hoamon.blogspot.com/2007/02/python-listhash-def.html


.. author:: default
.. categories:: chinese
.. tags:: python, list
.. comments::
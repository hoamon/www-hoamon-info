Python: 淺談 lambda 函式
================================================================================

lambda是用來定義一個小小函式用的，與一般使用的 def 有些許不同， Lisp 語言也有這個功能。因為這個 lambda 函式，讓 Python
語言可以更靈活地使用。

一個 def 函式：

def plus(x, y):
----return x + y

可以改寫為：

plus = lambda x, y: x + y
print plus(1, 2) # print 3
而

def show():
----return 'X'

可以改寫為：

show = lambda: 'X'

.. author:: default
.. categories:: chinese
.. tags:: python
.. comments::
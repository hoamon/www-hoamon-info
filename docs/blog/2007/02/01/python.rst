Python: 可變物件
================================================================================

在 Python 中，幾乎每樣東西都是物件。而可變物件的意思即允許使用者對物件作新增、刪除、修改的動作。

.. more::

可變物件常見的有 :doc:`list 及 dictionary(hash) <./python-listhash-def>` 。

不可變物件常見的是 tuple :

.. code-block:: python
    :linenos:

    TUPLE = (1, 2, 3)
    TUPLE[1] = 4 # throw TypeError

第 2 行執行時，會丟出 TypeError: 'tuple' object does not support item assignment 。\
因為 tuple 型別一經建構就不得修改。

.. author:: default
.. categories:: chinese
.. tags:: python, list, dictionary
.. comments::
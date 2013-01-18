一個小錯誤
================================================================================

在配置 django + mod_python 時，出了點小問題，在 python24 時，我可以用

PythonPath "['somewhere/sompath/'] + sys.path"
也可以用
PythonPath "['somewhere/sompath '] + sys.path"

但在 python25 必須寫成

PythonPath "['somewhere/sompath'] + sys.path"
結尾就是不准你用 /

唉~我找了好久。

.. author:: default
.. categories:: chinese
.. tags:: python25, django
.. comments::
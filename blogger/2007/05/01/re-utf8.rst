在 re 中使用 utf8 字串
================================================================================

如果你在 utf8 的環境中使用下面這個語句，你會發現這是 True 的。

re.compile('[年度]').search('要旨')

原因在於中文字在 utf8 中，是2~3個碼的，如：
年：\xe5\xb9\xb4
度：\xe5\xba\xa6
要：\xe8\xa6\x81
旨：\xe6\x97\xa8

所以在 re 比對時，[\xe5\xb9\xb4\xe5\xba\xa6] 的確可以比對出 '\xe8 \xa6\x81\xe6\x97\xa8' 。

解決之道就是使用 unicode 字串，如下：

re.compile(u'[年度]').search(u'要旨')

.. author:: default
.. categories:: chinese
.. tags:: regular expression, python
.. comments::
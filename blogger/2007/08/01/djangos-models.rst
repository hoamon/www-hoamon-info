django's models 中殺了父物件時，預設也會殺了子物件
================================================================================

如果你宣告了兩個 model：

class Journal(models.Model):
publishdate = models.DateField()
price = models.IntegerField()

class Article(models.Model):
journal = models.ForeignKeyField(Journal)
content = models.TextField()

那麼當你使用

>>> j = Journal.objects.get(publishdate=datetime.date(2007, 10, 1))
>>> j.delete()

時，會一併把 2007/10/1 出版的期刊內所有的文章紀錄一併刪除。

.. author:: default
.. categories:: chinese
.. tags:: django, python
.. comments::
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

Old Comments in Blogger
--------------------------------------------------------------------------------



`TerryH <http://www.blogger.com/profile/00198432946574471177>`_ at 2007-10-24T14:14:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Don't want to kill all atticle





from django.db import models

# Create your models here.



class Journal(models.Model):
publishdate = models.DateField()
price = models.IntegerField()
def nodel(self):
for a in self.article_set.all():
a.journal = None
a.save()
super(Journal, self).delete()

class Article(models.Model):
journal = models.ForeignKey(Journal,blank=True,null=True)
content = models.TextField()

.. author:: default
.. categories:: chinese
.. tags:: django, python
.. comments::
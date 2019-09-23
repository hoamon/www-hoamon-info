# -*- coding:utf8 -*-
# Copyright (c) 2010, ho600.com
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#     Redistributions in binary form must
#     reproduce the above copyright notice, this list of conditions and the
#     following disclaimer in the documentation and/or other materials provided
#     with the distribution.
#
#     Neither the name of the ho600.com nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from django.db import models as M
import cPickle


class StoreModel(M.Model):
    """ 儲存任意類型的資料。

    save() 乃將 value 的原值，轉成 cPickle 格式。

    但注意一個現象，當我們對一個 StoreModel object save() 後，
    若不修改 value 的值，就再作一次 save() ，
    一定會把 value 改成 StringType 。

    >>> sm = StoreModel(name='test', value=30)
    >>> sm.save()
    >>> print sm.value
    'I30\n.'
    >>> sm.save() #未重後賦值，就作 save() ，一定會將 value 改成 StringType
    >>> print sm.value
    "S'I30\\n.'\n."
    >>> sm.value = datetime.date(2010, 1, 1)
    >>> sm.save()
    >>> print sm.value
    "cdatetime\ndate\np1\n(S'\\x07\\xda\\x01\\x01'\ntRp2\n."
    """
    name = M.CharField(verbose_name=u'欄位名稱', max_length=255)
    value = M.CharField(verbose_name=u'值', null=True, max_length=512)

    def convertValue(self):
        return cPickle.loads(str(self.value))

    def save(self):
        self.value = cPickle.dumps(self.value)
        super(StoreModel, self).save()


class ExpandoModel(M.Model):
    """ 本類別主要是供其他類別繼承的，並不直接使用。
    本類別可讓繼承類別擁有不特定的資料表欄位。

    本類別被繼承後，若繼承類別有新建紀錄時，本類別將同時新增一筆紀錄，並載明繼承類別的資料表名到
    table_name 欄位。其實這個 table_name 是沒有實質意義的，只是單純在 DEBUG 時，
    比較容易看出 common_expandomodel 資料表的紀錄是那個繼承類別創建的。

    本類別的浮動(onfly)欄位功能乃是使用與 StoreModel 作 ManyToMany Relation 而來的。

    使用方式如下：
    >>> em = ExpandoModel.object.get(id=1)
    >>> em.xxx = 'yyy'
    >>> em.save() #這樣就會在 StoreModel 中多一筆紀錄(name=u'xxx', value=u"S'yyy'\np1\n.")
    >>>           #然後在 common_expandomodel_extra_fields 表格中，會再多一筆 em 與 sm 的關係
    >>> print em.xxx
    'yyy'

    整個類別的運作機制是在 em.xxx = 'yyy' 時，將 'xxx' 登記到 READY_TO_SAVE_KEY_NAMES 的 list 上，
    待 em.save() 執行時，將 READY_TO_SAVE_KEY_NAMES 中有存在的 key 值抓出來，
    然後創造相對應的 StoreModel object 。

    而 NOT_ALLOW_FIELD_NAMES list 則是紀錄了本類別及繼承類別中，有手動設定的欄位名，
    這些手動設定的欄位名，如： table_name, extra_fields, id 等，在賦值時是不會創造相對應的
    StoreModel object 。

    另外，本類別一被實例化，則會把它的相對應 StoreModel object 紀錄抓出來並放到 EXTRA_FIELDS 中。
    >>> em = ExpandoModel.object.get(id=1)
    >>> print em.EXTRA_FIELDS
    {u'xxx': 'yyy'}
    """
    NOT_ALLOW_FIELD_NAMES = []
    READY_TO_SAVE_KEY_NAMES = []
    EXTRA_FIELDS = {}

    table_name = M.CharField(verbose_name=u'繼承的資料表名', max_length=100)
    extra_fields = M.ManyToManyField(StoreModel, verbose_name=u'額外欄位')

    def __init__(self, *args, **kw):
        self.NOT_ALLOW_FIELD_NAMES = self._meta.get_all_field_names()
        self.READY_TO_SAVE_KEY_NAMES = []

        super(ExpandoModel, self).__init__(*args, **kw)

        if hasattr(self, 'id') and self.id:
            for ef in self.extra_fields.all():
                self.EXTRA_FIELDS[str(ef.name)] = ef.convertValue()

    def __setattr__(self, key, value):
        if (key[0] != '_'
            and key not in self.NOT_ALLOW_FIELD_NAMES
            and re.sub('_id$', '', key) not in self.NOT_ALLOW_FIELD_NAMES
            and key not in self.READY_TO_SAVE_KEY_NAMES):
            self.READY_TO_SAVE_KEY_NAMES.append(key)
        super(ExpandoModel, self).__setattr__(key, value)

    def __getattr__(self, key):
        key = str(key)
        if key in self.EXTRA_FIELDS.keys():
            return self.EXTRA_FIELDS[key]
        else:
            try:
                return super(ExpandoModel, self).__getattr__(key)
            except AttributeError:
                return None

    def save(self):
        if self.READY_TO_SAVE_KEY_NAMES and (not hasattr(self, 'id') or not self.id):
            super(ExpandoModel, self).save()

        while self.READY_TO_SAVE_KEY_NAMES:
            key = self.READY_TO_SAVE_KEY_NAMES.pop(0)
            try:
                ef = self.extra_fields.get(name=key)
            except StoreModel.DoesNotExist:
                sm = StoreModel(name=key, value=getattr(self, key))
                sm.save()
                self.extra_fields.add(sm)
            else:
                ef.value = getattr(self, key)
                ef.save()
            self.EXTRA_FIELDS[str(key)] = getattr(self, key)

        if not (hasattr(self, 'table_name') and self.table_name):
            self.table_name = self._meta.db_table
        super(ExpandoModel, self).save()


class ProjectExpandoModel(ExpandoModel):
    """
    >>> try:
    >>>     o = ProjectExpandoModel.objects.get(id=1)
    >>> except ProjectExpandoModel.DoesNotExist:
    >>>     o = ProjectExpandoModel(no='no%s'%random.random(), name=u'隨便的名稱')
    >>> # ProjectExpandoModel 只有 no, name 是手動設定的。
    >>> key, value = 'attr%s'%random.randint(0, 10000), random.random()
    >>> setattr(o, key, value)
    >>> o.integer = 1333
    >>> o.float = 499.99
    >>> o.datetime = datetime(2010, 9, 10, 12, 32, 45)
    >>> # 若要設定的屬性，其名稱是多位元組(就是中文)，要用 setattr 而不能用 o.測試 = 'whatever~~'
    >>> setattr(o, u'測試', 'whatever~~')
    >>> o.save() # 這樣就會在 StoreModel 中，生成 5 筆紀錄。
    >>>
    """
    no = M.CharField(verbose_name=u'序號', unique=True, max_length=255)
    name = M.CharField(verbose_name=u'名稱', max_length=255)

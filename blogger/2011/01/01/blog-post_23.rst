道路施工的排程問題，類似背包問題，但須考慮不同的排列方式
================================================================================

如：長度 10 公尺的路面，若有 7 公尺/日、 5 公尺/日、 3 公尺/日的施工工班可供選擇，則有幾種的排程組合?
此問題很像`背包問題`_，但在背包問題中，它不須考慮裝入物品的順序，而只考慮種類。若問題改為路面總長度 1000 公尺，而有 [260, 230,
190, 140, 80] 幾種工班時，我的解答是 69225 種。以下是我的解法：
::
    ** 1 ****class** **LineSerial**:
    ** 2 **    **u"""  目的：解路面排程問題，如：長度 10 公尺的路面，若有 7 公尺/日、 5 公尺/日、 3
    公尺/日**
    ** 3 ****        的施工工班可供選擇，則有幾種的排程組合。**
    ** 4 **
    ** 5 ****        解如下，共 17 種：**
    ** 6 ****            [7, 7], [7, 5], [7, 3],**
    ** 7 ****            [5, 7], [5, 5],**
    ** 8 ****            [5, 3, 7], [5, 3, 5], [5, 3, 3],**
    ** 9 ****            [3, 7],**
    **10 ****            [3, 5, 7], [3, 5, 5], [3, 5, 3],**
    **11 ****            [3, 3, 7], [3, 3, 5],**
    **12 ****            [3, 3, 3, 7], [3, 3, 3, 5], [3, 3, 3, 3],**
    **13 ****    """**
    **14 **    **def** **__init__**(self, total, sizes):
    **15 **        **""" serial_times 則是在計算 serial 函式被呼叫幾次。**
    **16 ****        """**
    **17 **        sizes.sort(reverse=True)
    **18 **        self._sizes = sizes
    **19 **        self.serial_times = **0**
    **20 **        self.result = []
    **21 **        self.serial(total, None, [])
    **22 **
    **23 **
    **24 **    **def** **serial**(self, total, length, tmp):
    **25 **        **u""" 將 total 依序給 _sizes 中的所有元素去切，切完後就放入 tmp ，**
    **26 ****            當 total <= 0 時, 再放入 self.result 中。**
    **27 ****        """**
    **28 **        **#self.serial_times += 1**
    **29 **        tmp.append(length)
    **30 **        **if** total <= 0:
    **31 **            self.result.append(tmp[1:])
    **32 **            **return**
    **33 **
    **34 **        **for** s **in** self._sizes: self.serial(total-s, s,
    tmp[:])
    **35 **
    **36 **
    **37 **
    **38 ****if** __name__ == **'__main__'**:
    **39 **    **from** time **import** time
    **40 **    total = **1000**
    **41 **    lengths = [**260**, **230**, **190**, **140**, **80**]
    **42 **    time0 = time()
    **43 **    cs = LineSerial(total, lengths)
    **44 **    **print** time() - time0
    **45 **    **print** **u'總組合數: %s'** % len(cs.result)
    **46 **    **print** **u'serial 遞迴次數: %s'** % cs.serial_times
    **47 **    **#for i in cs.result: print i**


.. _背包問題: http://hoamon.blogspot.com/2007/12/blog-post_20.html


.. author:: default
.. categories:: chinese
.. tags:: python, math, cmclass
.. comments::
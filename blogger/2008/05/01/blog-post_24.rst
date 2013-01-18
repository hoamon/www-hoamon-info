我的第二張運動彩券(五場命中)(誤)
================================================================================

繼`我的第一張運動彩券`_後，朋友相繼要求我下次購買運彩時，務必告知一下。所以，請注意啦，這次我買的是：

台灣 2008/5/25 賽程
#6001 西雅圖水手+1.5 @ 紐約洋基 -1.5 => 主勝
#6003 洛杉磯天使+1.5 @ 芝加哥白襪 -1.5 => 客勝
#6015 聖路易紅雀+1.5 @ 洛杉磯道奇 -1.5 => 客勝
#6013 波士頓紅襪-1.5 @ 奧客蘭運動家 +1.5 => 主勝
#6009 費城費城人-1.5 @ 休士頓太空人 +1.5 => 客勝

= 後記 =
這一次卻是五場皆中，實在是令人難以相信。只不過獎金算來，這張彩券只值 1189 元，賠率連 8
都不到。最後還是提醒大家，運動比賽的結果是沒有計算公式的，如果有的話，那就不值得花三個小時期待了。下注運彩，快樂就好，別太認真。

= 後後記 =
兌獎時，居然只有 270 元，再仔細地比對賽事結果，才發現『#6009 費城費城人-1.5 @ 休士頓太空人 +1.5 =>
客勝』這場我看錯了，所以實際上，我只中了四場。

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/SDkIMNLn1FI/AAAAAAAABOY/Dsq
bSz3sLIY/s400/DSCN6836.JPG
`_`.. image:: http://4.bp.blogspot.com/_eKM9lHjTZjs/SDkIMdLn1GI/AAAAAAAABOg/r
zpk6Vno1VY/s400/Screenshot.png
`_

順便提供一個可以快速計算獎金的 Python 程式：
::** 1 ****#!/usr/bin/env python**
    ** 2 ****# -*- coding:utf8 -*-**
    ** 3 ****class** **Combination**:
    ** 4 **    **def** **__init__**(self, list, num):
    ** 5 **        self.line = []
    ** 6 **        list = range(len(list))
    ** 7 **        self.Line(list, len(list), [], len(list) - num)
    ** 8 **
    ** 9 **        self.combination = []
    **10 **        **for** l **in** self.line:
    **11 **            l.sort()
    **12 **            **if** l **not** **in** self.combination:
    self.combination.append(l)
    **13 **
    **14 **    **def** **Line**(self, ori, level, res, limit):
    **15 **        **if** level == limit:
    **16 **            self.line.append(res[:])
    **17 **            **return**
    **18 **
    **19 **        **for** i **in** xrange(len(ori)):
    **20 **            res.insert(**0**, ori[i])
    **21 **            tmp = ori[:]
    **22 **            null = tmp.pop(i)
    **23 **            self.Line(tmp, level-**1**, res, limit)
    **24 **            res.pop(**0**)
    **25 **
    **26 ****def** **_product**(list):
    **27 **    product = **1**
    **28 **    **for** l **in** list: product *= l
    **29 **    **return** product
    **30 **
    **31 ****if** __name__ == **'__main__'**:
    **32 **    **""" 以下設定適用於 6X42, 5X16, 4X5, 3X1 的情況 """**
    **33 **    ori = [**2**, **1.46**, **1.6**, **1.7**, **2.1**]
    **#有猜中的賠率**
    **34 **    dollar = **10** **#每注金額**
    **35 **
    **36 **    result = []
    **37 **    **for** i **in** xrange(**3**, len(ori)+**1**):
    **38 **        C = Combination(ori, i)
    **39 **
    **40 **        **for** j **in** C.combination:
    **41 **            r = []
    **42 **            **for** k **in** j: r.append(ori[k])
    **43 **            result.append(r)
    **44 **
    **45 **    sum = **0**
    **46 **    **for** r **in** result: sum += int(dollar * _product(r))
    **47 **
    **48 **    **print** **'中獎注數: %s'** % len(result)
    **49 **    **print** **'可領彩金: %s'** % sum

.. _我的第一張運動彩券: http://hoamon.blogspot.com/2008/05/blog-post.html
.. _兌獎時，居然只有 270 元，再仔細地比對賽事結果，才發現『#6009 費城費城人-1.5 @ 休士頓太空人 +1.5 =>
    客勝』這場我看錯了，所以實際上，我只中了四場。: http://3.bp.blogspot.com/_eKM9lHjTZjs/SDkIMNLn1F
    I/AAAAAAAABOY/DsqbSz3sLIY/s1600-h/DSCN6836.JPG
.. _兌獎時，居然只有 270 元，再仔細地比對賽事結果，才發現『#6009 費城費城人-1.5 @ 休士頓太空人 +1.5 =>
    客勝』這場我看錯了，所以實際上，我只中了四場。: http://4.bp.blogspot.com/_eKM9lHjTZjs/SDkIMdLn1G
    I/AAAAAAAABOg/rzpk6Vno1VY/s1600-h/Screenshot.png


.. author:: default
.. categories:: chinese
.. tags:: python, baseball
.. comments::
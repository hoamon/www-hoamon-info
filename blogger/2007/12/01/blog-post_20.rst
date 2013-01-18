原來這就是背包問題呀!
================================================================================

日前(好久前了)提了一個讀研究所時所解決的`問題`_，那時還滿自傲的，畢竟在讀土木的同學中，還沒看到有人會解。

那是一個解決鋼筋裁切的廢料量最佳化所衍生的難題。也就是要列出一根原料鋼筋要切成工地用尺寸的組合問題，如：18公尺的鋼筋若要切成 10, 7, 5, 4,
3 公尺長的鋼筋，則有那幾種切法。

`Thinker`_ 提了一個很好的`方法`_來計算它的組合數有多少。不過，因為我要的是有那幾種組合，所以不曉得他的方法能否套用(`當然可以`_)。

之前，我是用 Perl 來解這個問題的，不過，程式已經找不到了，不是我沒作版本控制，那時候用的是 CVS，然而在歷經多次系統安裝， CVS
的儲存庫已經不知在那了。

所以，我用 Python 重寫這個方法。有兩種解法，第一種是用我之前的觀念來解的。第二種是昨天想的，不過，第二種卻比較沒效率。
::** 1 ****#!/usr/bin/env python**
    ** 2 ****# -*- coding: utf8 -*-**
    ** 3 ****def** **cut**(length, k, tmp):
    ** 4 **    **if** k == sizeslen:
    ** 5 **        **if** length >= sizes[-**1**]:
    ** 6 **            **return**
    ** 7 **        **else**:
    ** 8 **            tmps.append(tmp[:])
    ** 9 **            **return**
    **10 **
    **11 **    comp = int(length/sizes[k])
    **12 **    **for** i **in** xrange(comp+**1**):
    **13 **        j = comp - i
    **14 **        tmp[k] = j
    **15 **        cut(length-sizes[k]*j, k+**1**, tmp[:])
    **16 **
    **17 ****from** time **import** time
    **18 ****import** sys
    **19 ****if** __name__ == **'__main__'**:
    **20 **    bar = float(sys.argv[**1**])
    **21 **    sizes = [float(s) **for** s **in** sys.argv[**2**:]]
    **22 **    sizes.sort()
    **23 **    sizes.reverse()
    **24 **    sizeslen = len(sizes)
    **25 **    tmps = []
    **26 **    tmp = [**0**,]*sizeslen
    **27 **    time0 = time()
    **28 **    cut(bar, **0**, tmp[:])
    **29 **    **print** time() - time0
    **30 **    **print** len(tmps)

第二種：
::** 1 ****#!/usr/bin/env python**
    ** 2 ****# -*- coding: utf8 -*-**
    ** 3 ****def** **cut**(L, x, k, tmp, num):
    ** 4 **    num[**0**] += **1**
    ** 5 **    diff = L-x[**0**]
    ** 6 **    **if** diff > mat[**0**][**0**]:
    ** 7 **        **if** tmp[x[**1**][**0**]] != **0**: **return**
    ** 8 **        **else**: tmp[x[**1**][**0**]] = x[**1**][**1**]
    ** 9 **    **elif** diff < mat[**0**][**0**] **and** diff >= **0**:
    **10 **        **if** tmp[x[**1**][**0**]] != **0**: **return**
    **11 **        **else**: tmp[x[**1**][**0**]] = x[**1**][**1**]
    **12 **        tmps.append(tmp[:])
    **13 **        **return**
    **14 **    **else**:
    **15 **        **return**
    **16 **    **for** (i, s) **in** enumerate(mat[k+**1**:]):
    **17 **        cut(L-x[**0**], s, i+k+**1**, tmp[:], num)
    **18 **
    **19 ****def** **sort_by_value**(k):
    **20 **    **return** (k, k[**0**])
    **21 **
    **22 ****from** time **import** time
    **23 ****import** sys
    **24 ****if** __name__ == **'__main__'**:
    **25 **    time0 = time()
    **26 **    bar = float(sys.argv[**1**])
    **27 **    sizes = [float(s) **for** s **in** sys.argv[**2**:]]
    **28 **    lensizes = len(sizes)
    **29 **    tmps = []
    **30 **    mat = []
    **31 **    **for** (i, s) **in** enumerate(sizes):
    **32 **        comp = int(bar/s)
    **33 **        **for** j **in** xrange(**1**, comp+**1**):
    **34 **            mat.append((s*j, (i, j)))
    **35 **    mat.sort(key=sort_by_value)
    **36 **    tmp = [**0**, ]*lensizes
    **37 **    num = [**0**]
    **38 **    **for** (i, m) **in** enumerate(mat):
    **39 **        cut(bar, m, i, tmp[:], num)
    **40 **
    **41 **    **print** time() - time0
    **42 **    **print** len(tmps)
    **43 **    **print** num[**0**]

新的觀念是把需求尺寸的倍數尺寸拿來當切割尺寸。如：10公尺要給7, 5, 3, 2 來切的話，我先把需求尺寸變成 7, 10, 5, 9, 6, 3,
10, 8, 6, 4, 2 等尺寸來切，如果在切的過程，剛好又遇到擁有相同因數的尺寸則跳過，像是10公尺已經被 8 切掉了，後來又遇到 2
的話，就停止處理。

在人工演練的過程中，覺得第二種方法所跑的迴圈數比較少，然而寫成程式後，效率卻比較差，且實際的迴圈數也比較多。

== 後記 ==

`這裡`_有最新且更有效率的解法。

.. _問題: http://hoamon.blogspot.com/2007/03/cmclass_08.html
.. _Thinker: http://heaven.branda.to/%7Ethinker/GinGin_CGI.py
.. _方法: http://heaven.branda.to/%7Ethinker/GinGin_CGI.py/show_id_doc/230
.. _當然可以: http://hoamon.blogspot.com/2011/09/blog-post_15.html


.. author:: default
.. categories:: chinese
.. tags:: python, math, knapsack problem, computer, cmclass
.. comments::
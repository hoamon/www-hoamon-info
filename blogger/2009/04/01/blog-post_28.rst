二分逼近法求債券殖利率
================================================================================

一債券殖利率等式(`原理`_)如下，試求 r 值：

.. image:: http://latex.codecogs.com/gif.latex?99.2679%20=-%20%5Cfrac%7B0
    .875%5Ctimes%20%281-%5Cfrac%7B280%7D%7B365%7D%29%7D%7B%281+r%29%5E%7B0%7D
    %7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r%29%5E%7B%280+%5Cfrac%7B280%7D%7B365
    %7D%29%7D%7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r%29%5E%7B%281+%5Cfrac%7B280
    %7D%7B365%7D%29%7D%7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r%29%5E%7B%282+%5Cf
    rac%7B280%7D%7B365%7D%29%7D%7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r%29%5E%7B
    %283+%5Cfrac%7B280%7D%7B365%7D%29%7D%7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r
    %29%5E%7B%284+%5Cfrac%7B280%7D%7B365%7D%29%7D%7D


如果該等式中 (1+r)^t 的期別 t 皆為大於 0 的整數時，我們可以直接使用
numpy.lib.financial.irr([0.875*(1-280/365.), 0.875, 0.875, 0.875, 0.875,
100.875]) 求解債券殖利率 r 。但可惜它不是，所以我們使用二分逼近法來求得近似解。

概念乃是先把等式左邊移位至右邊，變成 -99.2679 - .... + 0.875/(1+r)^(4+280/365) = f(r) ，再將 r0=0,
r1=1 代入 f(r)，則會得到一正值及一負值，所以我們可相信真實的 r' 值的確位於 0 ~ 1 之間。

接下來，就進行一系列的迭代。令新 r 值等於 (r0 + r1)/2 ，再代入 f(r) 中，若 f(r) 為正，則表 r' 必在 (r0+r1)/2 ~
r1 之間; 若 f(r) 為負，則表 r' 必在 r0 ~ (r0+r1)/2 之間。持續進行此一動作，直到 r 值的差異值小於設定值為止。

以下則是我的 Python 程式：
::** 1 ****class** **AnnumYield**:
    ** 2 **    **""" 求解年化殖利率。**
    ** 3 ****    """**
    ** 4 **
    ** 5 **    **def** **__init__**(self, PV=**0**, Ci=[], Ni=[],
    precision=**6**, start_rate=**0**, end_rate=**1**):
    ** 6 **        **""" Ci: 第 i 個現金流量**
    ** 7 ****            Ni: 第 i 個期別的真實時間**
    ** 8 ****            PV: 現值。為債券購入價格，其值應為負值。**
    ** 9 ****            precision: 數值分析時的精度，當殖利率變化值小於 10**(-1*precision)
    ，則停止求解。**
    **10 ****            start_rate，end_rate: 起始利率。**
    **11 **
    **12 ****            self.equation: 現金流量的方程式**
    **13 ****            self.yieldrate: 債券殖利率**
    **14 ****        """**
    **15 **        self.Ci = Ci
    **16 **        self.Ni = Ni != [] **and** Ni **or** range(len(Ci))
    **17 **        self.PV = PV < **0** **and** PV **or** -**1***PV
    **18 **        self.precision = precision
    **19 **        self.start_rate = start_rate
    **20 **        self.end_rate = end_rate
    **21 **
    **22 **        equations = []
    **23 **        **for** i, c **in** enumerate(Ci):
    **24 **            equations.append(**'%s/(1+r)**(%s)'**%(c, Ni[i]))
    **25 **        self.equation = **'%s + '** % self.PV + **' +
    '**.join(equations)
    **26 **
    **27 **        self.yieldrate = self.getYield()
    **28 **
    **29 **    **def** **getYield**(self):
    **30 **        **""" 利用二分逼近法求 self.equation 的根。**
    **31 ****            當所求出的 yieldrate 與前一個解的差值小於 10 ** (-1*precision)
    即停止求解。**
    **32 **
    **33 ****            預設代入 start_rate 及 end_rate 去作逼近，**
    **34 ****            所以真實的 yieldrate 必須滿足 start_rate < yieldrate <
    end_rate 的條件，**
    **35 ****            否則無解。**
    **36 ****        """**
    **37 **        r = self.start_rate
    **38 **        self.list = [(self.start_rate, eval(self.equation))]
    **39 **        r = self.end_rate
    **40 **        self.list.append((self.end_rate, eval(self.equation)))
    **41 **
    **42 **        i0, (r0, res0) = **0**, self.list[**0**]
    **43 **        i1, (r1, res1) = **1**, self.list[**1**]
    **44 **        precision = **10** ** (-**1***self.precision)
    **45 **        **while** abs(r0 - r1) > precision:
    **46 **            r = (r0 + r1)/**2.**
    **47 **            res = eval(self.equation)
    **48 **            self.list.insert(i1, (r, res))
    **49 **            **if** res * res0 < **0:**
    **50 **                i0, (r0, res0) = i1-**1**, self.list[i1-**1**]
    **51 **                i1, (r1, res1) = i1  , self.list[i1]
    **52 **            **elif** res * res1 < **0:**
    **53 **                i0, (r0, res0) = i1  , self.list[i1]
    **54 **                i1, (r1, res1) = i1+**1**, self.list[i1+**1**]
    **55 **            **elif** res == **0:**
    **56 **                **break**
    **57 **            else:
    **58 **                **raise** ValueError, **\**
    **59 **                    **'無解。 end_rate 設定為 %s ，此數值比 yieldrate
    解還小'** % self.end_rate
    **60 **
    **61 **        **return** round((r0 + r1)/**2.**, self.precision)
    **62 **
    **63 ****if** __name__ == **'__main__'**:
    **64 **    t = **280.**/**365**
    **65 **    Ci = [-**0.875***(**1**-t), **0.875**, **0.875**,
    **0.875**, **0.875**, **100.875**]
    **66 **    Ni = [**0**,            **0**+t,   **1**+t,   **2**+t,
    **3**+t,   **4**+t]
    **67 **    annumyield = AnnumYield(Ci=Ci, Ni=Ni, PV=**99.2679**)
    **68 **    **print** annumyield.yieldrate



.. _原理: http://hoamon.blogspot.com/2009/04/foclass.html


.. author:: default
.. categories:: chinese
.. tags:: python, bond, foclass
.. comments::
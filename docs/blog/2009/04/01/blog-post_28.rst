FOClass: 二分逼近法求債券殖利率
================================================================================

一債券殖利率等式( :doc:`原理 <../../04/01/foclass>` )如下，試求 r 值：

.. figure:: http://latex.codecogs.com/gif.latex?99.2679%20=-%20%5Cfrac%7B0.875%5Ctimes%20%281-%5Cfrac%7B280%7D%7B365%7D%29%7D%7B%281+r%29%5E%7B0%7D%7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r%29%5E%7B%280+%5Cfrac%7B280%7D%7B365%7D%29%7D%7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r%29%5E%7B%281+%5Cfrac%7B280%7D%7B365%7D%29%7D%7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r%29%5E%7B%282+%5Cfrac%7B280%7D%7B365%7D%29%7D%7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r%29%5E%7B%283+%5Cfrac%7B280%7D%7B365%7D%29%7D%7D%20+%20%5Cfrac%7B0.875%7D%7B%281+r%29%5E%7B%284+%5Cfrac%7B280%7D%7B365%7D%29%7D%7D
    :width: 600px
    :align: center

如果該等式中 (1+r)^t 的期別 t 皆為大於 0 的整數時，我們可以直接使用 \
numpy.lib.financial.irr([0.875*(1-280/365.), 0.875, 0.875, 0.875, 0.875, 100.875]) \
求解債券殖利率 r 。但可惜它不是，所以我們使用二分逼近法來求得近似解。

.. more::

概念乃是先把等式左邊移位至右邊，變成 -99.2679 - .... + 0.875/(1+r)^(4+280/365) = f(r) ，\
再將 r0=0, r1=1 代入 f(r)，則會得到一正值及一負值，所以我們可相信真實的 r' 值的確位於 0 ~ 1 之間。

接下來，就進行一系列的迭代。令新 r 值等於 (r0 + r1)/2 ，再代入 f(r) 中，若 f(r) 為正，則表 r' 必在 (r0+r1)/2 ~ r1 之間; \
若 f(r) 為負，則表 r' 必在 r0 ~ (r0+r1)/2 之間。持續進行此一動作，直到 r 值的差異值小於設定值為止。

以下則是我的 Python 程式：

.. code-block:: python
    :linenos:

    class AnnumYield:
        """ 求解年化殖利率。 """

        def __init__(self, PV=0, Ci=[], Ni=[],
            precision=6, start_rate=0, end_rate=1):
            """ Ci: 第 i 個現金流量
                Ni: 第 i 個期別的真實時間
                PV: 現值。為債券購入價格，其值應為負值。
                precision: 數值分析時的精度，
                    當殖利率變化值小於 10**(-1*precision) ，
                    則停止求解。
                start_rate，end_rate: 起始利率。

                self.equation: 現金流量的方程式
                self.yieldrate: 債券殖利率
            """
            self.Ci = Ci
            self.Ni = Ni != [] and Ni or range(len(Ci))
            self.PV = PV < 0 and PV or -1*PV
            self.precision = precision
            self.start_rate = start_rate
            self.end_rate = end_rate

            equations = []
            for i, c in enumerate(Ci):
                equations.append('%s/(1+r)**(%s)'%(c, Ni[i]))
            self.equation = ('%s + ' % self.PV
                                + ' + '.join(equations))

            self.yieldrate = self.getYield()

        def getYield(self):
            """ 利用二分逼近法求 self.equation 的根。
                當所求出的 yieldrate 與前一個解的差值小於
                    10 ** (-1*precision) 即停止求解。

                預設代入 start_rate 及 end_rate 去作逼近，
                所以真實的 yieldrate 必須滿足
                    start_rate < yieldrate < end_rate 的條件，
                否則無解。
            """
            r = self.start_rate
            self.list = [(self.start_rate,
                            eval(self.equation))]
            r = self.end_rate
            self.list.append((self.end_rate,
                            eval(self.equation)))

            i0, (r0, res0) = 0, self.list[0]
            i1, (r1, res1) = 1, self.list[1]
            precision = 10 ** (-1*self.precision)
            while abs(r0 - r1) > precision:
                r = (r0 + r1)/2.
                res = eval(self.equation)
                self.list.insert(i1, (r, res))
                if res * res0 < 0:
                    i0, (r0, res0) = i1-1, self.list[i1-1]
                    i1, (r1, res1) = i1  , self.list[i1]
                elif res * res1 < 0:
                    i0, (r0, res0) = i1  , self.list[i1]
                    i1, (r1, res1) = i1+1, self.list[i1+1]
                elif res == 0:
                    break
                else:
                    raise ValueError, \
                        '無解。 end_rate 設定為 %s ' \
                            % self.end_rate + \
                            '，此數值比 yieldrate 解還小'

            return round((r0 + r1)/2., self.precision)

    if __name__ == '__main__':
        t = 280./365
        Ci = [-0.875*(1-t),
                    0.875, 0.875, 0.875, 0.875, 100.875]
        Ni = [0,    0+t,   1+t,   2+t,   3+t,   4+t]
        annumyield = AnnumYield(Ci=Ci, Ni=Ni, PV=99.2679)
        print annumyield.yieldrate

:doc:`../../05/01/blog-post_07` 系列文章
--------------------------------------------------------------------------------

    #. :doc:`../../04/01/foclass`
    #. :doc:`../../04/01/blog-post_28` (本文）
    #. :doc:`../../05/01/foclass`
    #. :doc:`../../05/01/foclass_07`

.. author:: default
.. categories:: chinese
.. tags:: python, bond, foclass
.. comments::
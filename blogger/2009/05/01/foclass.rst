FOClass: 零息債券殖利率計算
================================================================================

市場上，我們能觀察到的公債交易標的多半都是附息債券，而此附息債券因為有息票收入的關係，所以無法視為即期利率。在本文中，我們將利用存續期間(Macaulay
duration)調整法來消除息票影響。

存續期限最先由 Macaulay(1938) 提出。依 Macaulay duration 之定義，存續期限相同的債券，不論 Coupon rate
為何，不論是附息或零息債券，皆視為有著相同「有效」到期期限 (effective maturities) 或「真正」到期期限(true term to
maturities)之債券。

也可將存續期限視為回收本金時間。

由於債券市場之交易型態中，存續期限是買賣報價之重要依據，亦即在流動性與稅負等條件皆相同之情況下，市場上對一張附息債券與另一張有著相同存續期限之零息債券所要
求的殖利率是相同的。

因而可透過此種定義來作期限調整，將各附息債券之殖利率與其存續期限之關係描繪出一條存續期限殖利率曲線 (yield to duration)
，以此當作零息債券殖利率曲線之估計值。

以下則是在 2009/4/16 所觀察的中央政府公債交易資訊：
::||公債碼||交易價格||票面利率%||到期日     ||
    ||A93109||110.4412|| 3       ||2024/11/18 ||
    ||A94107||100.3904|| 1.63    ||2015/9/12  ||
    ||A95101||102.3168|| 1.75    ||2011/1/6   ||
    ||A95103||100.6188|| 1.75    ||2016/3/31  ||
    ||A96101||103.0834|| 1.88    ||2012/1/26  ||
    ||A97106||103.8367|| 2.13    ||2018/9/24  ||
    ||A98101||99.2679 || 0.875   ||2014/1/21  ||
    ||A98102||98.8824 || 2.125   ||2029/2/16  ||
    ||A98103||98.5211 || 1.375   ||2019/3/5   ||
    首先利用`二分逼近法求各債券殖利率`_ y，接下來代入下列公式：

`.. image:: http://latex.codecogs.com/gif.latex?D%20=%20%5Cfrac%7B%5Csum_%7Bi
=1%7D%5E%7Bn%7D%20%5Cfrac%7Bt_%7Bi%7DC_%7Bi%7D%7D%7B%281+r%29%5E%7Bt_%7Bi%7D%
7D%7D%7D%7BB%7D
`_


-   ti: 期別
-   Ci: ti 期別的現金流量
-   B: 債券現值，也就是交易價格
-   D: 存續期間
-   y: 殖利率


再代入下列公式得到修正後的存續期間：

`.. image:: http://latex.codecogs.com/gif.latex?D%5E%7B*%7D%20=%20%5Cfrac%7BD
%7D%7B1+%5Cfrac%7By%7D%7Bm%7D%7D
`_

-   m: 為每幾個月配息一次

::** 1 ****class** **ModifiedDuration**:
    ** 2 **    **""" 存續期間 D 的公式定義如下：**
    ** 3 ****        D = ****\f****rac{\sum_{i=1}^{n}
    ****\f****rac{t_{i}C_{i}}{(1+y)^{t_{i}}}}{B}**
    ** 4 **
    ** 5 ****        再經殖利率 y 的修正後，得到 D^{*}**
    ** 6 **
    ** 7 ****        D^{*} = ****\f****rac{D}{1+****\f****rac{y}{m}}**
    ** 8 ****        y: 為年化殖利率**
    ** 9 ****        m: 為每幾個月配息一次**
    **10 **
    **11 ****    """**
    **12 **    **def** **__init__**(self, PV=**0**, Ci=[], Ni=[],
    yieldrate=**0**, coupon_duration=**12**):
    **13 **        self.PV = PV < **0** **and** -**1***PV **or** PV
    **14 **        self.Ci = Ci
    **15 **        self.Ni = len(Ni) != **0** **and** Ni **or**
    range(len(Ci))
    **16 **        self.yieldrate = yieldrate
    **17 **        self.coupon_duration = coupon_duration
    **18 **
    **19 **        equations = []
    **20 **        **for** i, c **in** enumerate(Ci):
    **21 **
    equations.append(**'%s*%s/(1+%s)**(%s)'**%(self.Ni[i], c,
    **22 **                self.yieldrate, self.Ni[i]))
    **23 **        self.equation = **' + '**.join(equations)
    **24 **        self.D = eval(self.equation) / self.PV
    **25 **        self.modified_duration = round(self.D/(**1**+
    **26 **            self.yieldrate/(self.coupon_duration/**12**)),
    **2**)
    最後，我們可以把附息債券的存續期間繪製出來如下圖，我們可以知道在相同存續期間下，該附息債券殖利率也就是零息債券殖利率：

`.. image:: http://2.bp.blogspot.com/_eKM9lHjTZjs/Sf_1Qj127oI/AAAAAAAAB3Y/W2r
Ul32MSAk/s400/duration_method.png
`_


-   紅十字的 X 軸為附息債券的到期日
-   綠三角的 X 軸為附息債券的存續期限
-   X 軸表期別
-   Y 軸表殖利率




在`下篇`_中，我們將討論如何迴歸一條殖利率函式供實務應用。

.. _二分逼近法求各債券殖利率: http://hoamon.blogspot.com/2009/04/blog-post_28.html
.. _ y，接下來代入下列公式：: http://www.codecogs.com/eqnedit.php?latex=D%20=%20%5Cf
    rac%7B%5Csum_%7Bi=1%7D%5E%7Bn%7D%20%5Cfrac%7Bt_%7Bi%7DC_%7Bi%7D%7D%7B%281
    @plus;r%29%5E%7Bt_%7Bi%7D%7D%7D%7D%7BB%7D
.. _再代入下列公式得到修正後的存續期間：: http://www.codecogs.com/eqnedit.php?latex=D%5E%7B
    *%7D%20=%20%5Cfrac%7BD%7D%7B1@plus;%5Cfrac%7By%7D%7Bm%7D%7D
.. _最後，我們可以把附息債券的存續期間繪製出來如下圖，我們可以知道在相同存續期間下，該附息債券殖利率也就是零息債券殖利率：: http://2
    .bp.blogspot.com/_eKM9lHjTZjs/Sf_1Qj127oI/AAAAAAAAB3Y/W2rUl32MSAk/s1600-h
    /duration_method.png
.. _下篇: http://hoamon.blogspot.com/2009/05/foclass_07.html


.. author:: default
.. categories:: chinese
.. tags:: python, bond, foclass
.. comments::
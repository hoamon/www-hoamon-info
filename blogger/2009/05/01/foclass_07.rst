FOClass: 債券殖利率曲線計算
================================================================================

在`前篇文章`_中，我們已可算出零息債券的殖利率，但如果要套用在實務上的應用中，我們必須將觀察到的各點作一迴歸函式，讓我們可以找到各天期的殖利率。

運用原理為 Cubic Spline 方法。假設債券的 Discount 因子為一個三次方程式：

`.. image:: http://latex.codecogs.com/gif.latex?D%28t%29%20=%201%20+%20a%5Cti
mes%20t%20+%20b%5Ctimes%20t%5E2%20+%20c%5Ctimes%20t%5E3
`_

而每張債券的現金流量再套入下方方程式：

`.. image:: http://latex.codecogs.com/gif.latex?PV%20=%20\sum_{i=1}^{n}C_{i}%
20\times%20D_{i}
`_

可得到類似 3.3a + 1.2b + 5.5c = 30 的等式。像是代入`前篇文章`_的九張債券可得如下式子：

`.. image:: http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20x_%7B
11%7D%20&%20x_%7B12%7D%20&%20x_%7B13%7D%5C%5C%20...%20&%20...&%20...%5C%5C%20
x_%7B91%7D%20&%20x_%7B92%7D%20&%20x_%7B93%7D%20%5Cend%7Bbmatrix%7D%20%5Cbegin
%7Bbmatrix%7D%20a%5C%5C%20b%5C%5C%20c%20%5Cend%7Bbmatrix%7D%20=%20%5Cbegin%7B
bmatrix%7D%2043.33%5C%5C%20...%5C%5C%203,4%20%5Cend%7Bbmatrix%7D
`_

`.. image:: http://latex.codecogs.com/gif.latex?%5Cbegin%7Bbmatrix%7D%20a%5C%
5C%20b%5C%5C%20c%20%5Cend%7Bbmatrix%7D%20=%20%5Cleft%20%28%5Cbegin%7Bbmatrix%
7D%20x_%7B11%7D%20&%20x_%7B12%7D%20&%20x_%7B13%7D%5C%5C%20...%20&%20...&%20..
.%5C%5C%20x_%7B91%7D%20&%20x_%7B92%7D%20&%20x_%7B93%7D%20%5Cend%7Bbmatrix%7D%
5E%7Bt%7D%20%5Ccdot%20%5Cbegin%7Bbmatrix%7D%20x_%7B11%7D%20&%20x_%7B12%7D%20&
%20x_%7B13%7D%5C%5C%20...%20&%20...&%20...%5C%5C%20x_%7B91%7D%20&%20x_%7B92%7
D%20&%20x_%7B93%7D%20%5Cend%7Bbmatrix%7D%5Cright%20%29%5E%7BINV%7D%20%5Ccdot%
20%5Cbegin%7Bbmatrix%7D%20x_%7B11%7D%20&%20x_%7B12%7D%20&%20x_%7B13%7D%5C%5C%
20...%20&%20...&%20...%5C%5C%20x_%7B91%7D%20&%20x_%7B92%7D%20&%20x_%7B93%7D%2
0%5Cend%7Bbmatrix%7D%5E%7Bt%7D%20%5Ccdot%20%5Cbegin%7Bbmatrix%7D%2043.33%5C%5
C%20...%5C%5C%203,4%20%5Cend%7Bbmatrix%7D
`_

透過 OLS(ordinary least square) 方法求出 a, b, c 的適當值後，再代入：

`.. image:: http://latex.codecogs.com/gif.latex?Y%28t%29%20=%20%5Csqrt%5Bt%5D
%7B%5Cfrac%7B1%7D%7BD%28t%29%7D%7D%20-%201
`_

即可算出殖利率曲線。如下圖：

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/SgJYg1tT3VI/AAAAAAAAB3g/3rt
Uyq_w1nQ/s400/zero_bond_yield_curve.png
`_


-   綠色線為零息債券殖利率曲線
-   紅色線為附息債券殖利率曲線

我們可以看到 20~30年期的殖利率下降的十分奇怪。原因是我們的觀察值債券的年期最大只有 20 年，所以這一條函式在預測 20~30
年期的數據應該是有問題。

相關的 Python 程式如下：
::** 1 ****class** **CubicSpline**:
    ** 2 **    **""" 使用最小平方和原則作三次方方程式的迴歸**
    ** 3 ****    """**
    ** 4 **    **def** **__init__**(self):
    ** 5 **        self.PVs = array([])
    ** 6 **        self.X = array([])
    ** 7 **
    ** 8 **    **def** **addBondData**(self, PV=**0**, Ci=[], Ni=[]):
    ** 9 **        self.PV = PV < **0** **and** PV **or** -**1***PV
    **10 **        **if** Ni[**0**] == **0:**
    **11 **            self.PVs = append(self.PVs, -**1***self.PV-
    Ci[**0**])
    **12 **            self.Ci = array(Ci[**1:**])
    **13 **            self.Ni = array([[**1**, t, t****2**, t****3**]
    **for** t **in** Ni[**1:**]])
    **14 **        else:
    **15 **            self.PVs = append(self.PVs, -**1***self.PV)
    **16 **            self.Ci = array(Ci)
    **17 **            self.Ni = array([[**1**, t, t****2**, t****3**]
    **for** t **in** Ni])
    **18 **
    **19 **        self.dt = dot(self.Ci, self.Ni)
    **20 **        **if** len(self.X):
    **21 **            self.X = append(self.X, [self.dt[**1:]],
    axis**=**0**)
    **22 **        else:
    **23 **            self.X = array([self.dt[**1:**]])
    **24 **
    **25 **        self.PVs[-**1**] -= self.dt[**0**]
    **26 **
    **27 **    **def** **runOLS**(self):
    **28 **        self.X = matrix(self.X)
    **29 **        self.PVs = matrix(self.PVs).T
    **30 **        self.b = linalg.inv(self.X.T * self.X) * self.X.T *
    self.PVs
    **31 **        **return** self.b


.. _前篇文章: http://hoamon.blogspot.com/2009/05/foclass.html
.. _運用原理為 Cubic Spline 方法。假設債券的 Discount 因子為一個三次方程式：: http://www.codecogs
    .com/eqnedit.php?latex=D%28t%29%20=%201%20@plus;%20a%5Ctimes%20t%20@plus;
    %20b%5Ctimes%20t%5E2%20@plus;%20c%5Ctimes%20t%5E3
.. _而每張債券的現金流量再套入下方方程式：: http://www.codecogs.com/eqnedit.php?latex=PV%20=
    %20\sum_{i=1}^{n}C_{i}%20\times%20D_{i}
.. _的九張債券可得如下式子：: http://www.codecogs.com/eqnedit.php?latex=%5Cbegin%7Bbm
    atrix%7D%20x_%7B11%7D%20&%20x_%7B12%7D%20&%20x_%7B13%7D%5C%5C%20...%20&%2
    0...&%20...%5C%5C%20x_%7B91%7D%20&%20x_%7B92%7D%20&%20x_%7B93%7D%20%5Cend
    %7Bbmatrix%7D%20%5Cbegin%7Bbmatrix%7D%20a%5C%5C%20b%5C%5C%20c%20%5Cend%7B
    bmatrix%7D%20=%20%5Cbegin%7Bbmatrix%7D%2043.33%5C%5C%20...%5C%5C%203,4%20
    %5Cend%7Bbmatrix%7D
.. _的九張債券可得如下式子：: http://www.codecogs.com/eqnedit.php?latex=%5Cbegin%7Bbm
    atrix%7D%20a%5C%5C%20b%5C%5C%20c%20%5Cend%7Bbmatrix%7D%20=%20%5Cleft%20%2
    8%5Cbegin%7Bbmatrix%7D%20x_%7B11%7D%20&%20x_%7B12%7D%20&%20x_%7B13%7D%5C%
    5C%20...%20&%20...&%20...%5C%5C%20x_%7B91%7D%20&%20x_%7B92%7D%20&%20x_%7B
    93%7D%20%5Cend%7Bbmatrix%7D%5E%7Bt%7D%20%5Ccdot%20%5Cbegin%7Bbmatrix%7D%2
    0x_%7B11%7D%20&%20x_%7B12%7D%20&%20x_%7B13%7D%5C%5C%20...%20&%20...&%20..
    .%5C%5C%20x_%7B91%7D%20&%20x_%7B92%7D%20&%20x_%7B93%7D%20%5Cend%7Bbmatrix
    %7D%5Cright%20%29%5E%7BINV%7D%20%5Ccdot%20%5Cbegin%7Bbmatrix%7D%20x_%7B11
    %7D%20&%20x_%7B12%7D%20&%20x_%7B13%7D%5C%5C%20...%20&%20...&%20...%5C%5C%
    20x_%7B91%7D%20&%20x_%7B92%7D%20&%20x_%7B93%7D%20%5Cend%7Bbmatrix%7D%5E%7
    Bt%7D%20%5Ccdot%20%5Cbegin%7Bbmatrix%7D%2043.33%5C%5C%20...%5C%5C%203,4%2
    0%5Cend%7Bbmatrix%7D
.. _透過 OLS(ordinary least square) 方法求出 a, b, c 的適當值後，再代入：: http://www.cod
    ecogs.com/eqnedit.php?latex=Y%28t%29%20=%20%5Csqrt%5Bt%5D%7B%5Cfrac%7B1%7
    D%7BD%28t%29%7D%7D%20-%201
.. _即可算出殖利率曲線。如下圖：: http://3.bp.blogspot.com/_eKM9lHjTZjs/SgJYg1tT3VI/AAA
    AAAAAB3g/3rtUyq_w1nQ/s1600-h/zero_bond_yield_curve.png


.. author:: default
.. categories:: chinese
.. tags:: python, bond, foclass
.. comments::
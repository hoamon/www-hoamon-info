CMClass: GA 演算法
================================================================================

老師出了一題求函數最小化的問題，要我們用 Partical Swarm 求解，它與螞蟻王國演算法很類似，但尚未認真研究。先用 GA 求解。再來用
Partical Swarm 求解。

題目是：

f(x)= (x1/x2)* (sin(x2))^2 + (x2-x1)* cos(x1+10)
where
10<= x1 <= 30
30<= x2 <= 50
考題：
x1, x2 = any real value
try to find the minimum f(x)

我自已寫了一個 GA 物件(請到 https://ssvn.hoamon.info/OpenRelease/GA-0.1.py 下載，帳/密：
guest/guest)

而解題的 ConvVar, FUNC 函式如下：

::
    ** 1 ****def** **ConvVar**(chromosom):     **#轉換基因組到決策變數**
    ** 2 **    variables = []
    ** 3 **    variables.append((int(chromosom[**0**]***3**) +
    **1**)***10**)
    ** 4 **    variables[**0**] += int(chromosom[**1**]***10**)
    ** 5 **    variables[**0**] += int(chromosom[**2**]***10**)***0.1**
    ** 6 **    variables[**0**] += int(chromosom[**3**]***10**)***0.01**
    ** 7 **    variables[**0**] += int(chromosom[**4**]***10**)***0.001**
    ** 8 **
    ** 9 **    variables.append((int(chromosom[**5**]***3**) +
    **3**)***10**)
    **10 **    variables[**1**] += int(chromosom[**6**]***10**)
    **11 **    variables[**1**] += int(chromosom[**7**]***10**)***0.1**
    **12 **    variables[**1**] += int(chromosom[**8**]***10**)***0.01**
    **13 **    variables[**1**] += int(chromosom[**9**]***10**)***0.001**
    **14 **
    **15 **    **return** variables
    **16 **
    **17 ****from** math **import** sin, cos
    **18 ****def** **FUNC**(variables):        **#定義目標函數**
    **19 **    (x1, x2) = variables
    **20 **    **if** x1 > **30** **or** x1 < **10**: **return**
    float(**'infinity'**)
    **21 **    **if** x2 > **50** **or** x2 < **30**: **return**
    float(**'infinity'**)
    **22 **    sum = (x1/x2) * (sin(x2)) * (sin(x2)) + (x2-x1) *
    cos(x1+**10**)
    **23 **    **return** sum


.. author:: default
.. categories:: chinese
.. tags:: genetic algorithm, python
.. comments::
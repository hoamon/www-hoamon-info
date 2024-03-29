指派問題使用 python + lp_solve 解決
================================================================================

指派問題乃線性規劃的一種特例，它的特性是不須強調解為 0-1 變數或整數值，但最後算出來它卻一定就是 0 或 1
，只是這種說法是學理上的，當我們使用程式來計算時，往往因為這些工具在計算過程中使用數值分析的方法，造成解的結果只會接近 0 或是 接近 1 ，而不是純正的
0 或 1。

這也就是我在第 73 行中，使用 v > 0 而不是 v == 1 的原因，如果是寫 v == 1 的話，有些 v 值是 0.999999
的，就不會顯現了。事實上，使用 v > 0.5 會更好。不過，我最後檢查時，發現 > 0 就可以秀出這 50 個 x 的值，也就算了。

lp_solve 函式庫安裝方法請見`舊文`_。

::
    ** 1 ****# -*- coding: utf8 -*-**
    ** 2 ****""" 問題： **
    ** 3 ****    **
    ** 4 ****    指定 0, 1, 2, ..., 49 等 50 個不可重複的數字給 x0 ~ x49，例如 x0 = 12,
    x1 = 33, ...**
    ** 5 **
    ** 6 ****    y = sin(1*x0) + sin(2*x1) + sin(3*x2) + ... +
    sin(50*x49)**
    ** 7 **
    ** 8 ****    求解 y 之最大值？**
    ** 9 **
    **10 ****    解法：**
    **11 **
    **12 ****    此問題可視為一種指派問題，也就是說有 0 ~ 49 等員工，要放到 x0 ~ x49 的職位去，**
    **13 ****    這樣決策變數就會變成 p00(值為 1 代表 x0=0), p01(值為 1 代表 x1=0),**
    **14 ****    p02 , ..., p49_49 等 2500 個決策變數，且其值必為 0 或 1 。**
    **15 **
    **16 ****    雖然目標函式看起來是非線性的，但其實是線性的， y 函式的係數應該長得如下：**
    **17 **
    **18 ****            x0          x1          x2          ...**
    **19 ****    0       0(C00)      0(C01)      0(C02)      ...**
    **20 ****    1       0.84(C10)   0.91(C11)   0.14(C12)   ...**
    **21 ****    2       0.91(C20)   -0.76(C21)  -0.28(C22)  ...**
    **22 ****    ...     ...         ...         ...         ...**
    **23 **
    **24 ****    所以如果決策變數是 p20 = p01 = p12 = 1，其餘為 0 ，則代表 x0 = 2，x1 =
    0，x2 = 1，**
    **25 ****    這樣 y = 0.91 + 0 + 0.14 = 1.05 。**
    **26 **
    **27 ****    所以目標式可以寫成 y = C00 * p00 + C01 * p01 + ... + C49_49 *
    p49_49 。**
    **28 **
    **29 ****    最後再加上限制式**
    **30 ****    **
    **31 ****    p00 + p01 + ... + p0_49 = 1**
    **32 ****    p10 + p11 + ... + p1_49 = 1**
    **33 ****    ...**
    **34 ****    p49_0 + p49_1 + ... + p49_49 = 1**
    **35 **
    **36 ****    p00 + p10 + ... + p49_0 = 1**
    **37 ****    p01 + p11 + ... + p49_1 = 1**
    **38 ****    ...**
    **39 ****    p0_49 + p1_49 + ... + p49_49 = 1**
    **40 **
    **41 ****    等 100 條限制式後，就能求 y 的最佳解。**
    **42 **
    **43 ****"""**
    **44 ****from** math **import** sin
    **45 ****import** lpsolve55 **as** L
    **46 **
    **47 **LENGTH = **50**
    **48 **C = []
    **49 **
    **50 ****for** i **in** xrange(LENGTH):
    **51 **    **for** j **in** xrange(LENGTH):
    **52 **        C.append(-**1***sin((j+**1**)*i)) **# lp_solve
    預設解極小值問題，所以我把目標函數係數全乘以 -1**
    **53 **
    **54 **lp = L.lpsolve(**'make_lp'**, **0**, LENGTH****2**)
    **55 **L.lpsolve(**'set_verbose'**, lp, L.IMPORTANT)
    **56 **ret = L.lpsolve(**'set_obj_fn'**, lp, C)
    **57 **
    **58 ****for** i **in** xrange(LENGTH):
    **59 **    p = [**0**,] * (LENGTH ** **2**)
    **60 **    **for** j **in** xrange(i*LENGTH, i*LENGTH+LENGTH): p[j] =
    **1**
    **61 **    ret = L.lpsolve(**'add_constraint'**, lp, p, L.EQ, **1**)
    **62 **
    **63 **    p = [**0**,] * (LENGTH ** **2**)
    **64 **    **for** j **in** xrange(**0**, LENGTH):
    **65 **        p[j*LENGTH+i] = **1**
    **66 **    ret = L.lpsolve(**'add_constraint'**, lp, p, L.EQ, **1**)
    **67 **
    **68 **L.lpsolve(**'solve'**, lp)
    **69 ****print** **u'目標值： %s'** % (L.lpsolve(**'get_objective'**, lp)
    * -**1**) **#要乘以 -1 來還原目標值。**
    **70 **vars = L.lpsolve(**'get_variables'**, lp)[**0**]
    **71 ****print** **u'決策變數： %s'** % vars
    **72 ****for** (ij, v) **in** enumerate(vars):
    **73 **    **if** v > 0:
    **74 **        i = ij / LENGTH
    **75 **        j = ij % LENGTH
    **76 **        **print** **'x%s = %s, '** % (j, i),
    **77 **        **if** i % **5** + **1** == 5: print

目標值最佳解為 47.8620523191 。

各變數值如下：
x21 = 0, x32 = 1, x47 = 2, x33 = 3, x1 = 4,
x37 = 5, x16 = 6, x45 = 7, x11 = 8, x25 = 9,
x18 = 10, x30 = 11, x7 = 12, x17 = 13, x0 = 14,
x41 = 15, x36 = 16, x22 = 17, x49 = 18, x9 = 19,
x44 = 20, x26 = 21, x43 = 22, x13 = 23, x42 = 24,
x35 = 25, x8 = 26, x20 = 27, x39 = 28, x40 = 29,
x29 = 30, x10 = 31, x34 = 32, x4 = 33, x2 = 34,
x38 = 35, x24 = 36, x6 = 37, x46 = 38, x5 = 39,
x27 = 40, x28 = 41, x14 = 42, x23 = 43, x48 = 44,
x19 = 45, x31 = 46, x12 = 47, x15 = 48, x3 = 49,

=== 後記 ===

經老師指導後，使用

ret = L.lpsolve('set_binary', lp, [1,]*(LENGTH**2)) #大約加在第 59 行後

令決策變數為 0-1 二元變數後，計算時間馬上減少了 60% 。

.. _舊文: http://hoamon.blogspot.com/2007/10/lpsolve.html


.. author:: default
.. categories:: chinese
.. tags:: lp, python, math, cmclass
.. comments::
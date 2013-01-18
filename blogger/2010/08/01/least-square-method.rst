以 least square method 搜尋非線性方程式的係數值
================================================================================

針對非線性迴歸求解其係數值，我寫了一份文件，考慮了其中繁雜的數學，我是用 rst 格式撰寫，配合 latex 轉成 PDF 。因為要轉 html
時，那些數學式實在是太麻煩了，所以我想就只提供 `PDF`_, `rst`_ 給各位下載。

本文件用途說明:

當我們有一堆觀測數據，想要找出一條方程式可以將自變數、應變數的關係明確表示時，可以使用 least square method 求解，例如我們有 10
個觀察值(1, 4), (4, 5), (1, 2), (4, 5), (6, 9), (1, 8), (4, 5), (3, 4), (5, 5),
(6, 6) 等，而我們先猜測它們的關係是二次的，應該要符合 Y = a * X^2 + b * X + c
方程式，有了觀測值及預估方程式形式後，接下來就可以利用 least square method 計算出 a, b, c 三個係數，期使它們能讓計算出來的
Y 值與觀察值的誤差最小。

在求取 a, b, c 三個係數上，我介紹了 4 種方法： the steepest descent method, Newton's method,
the Guass-Newton method 和 levenberg-marquardt method 。

`PDF表文下載`_

`rst全文下載`_

** 以下純供搜尋引擎使用，生人勿近 **

應用問題說明
-----------------------------------------------------------------------------
---

當我們有一堆觀測數據，想要找出一條方程式可以將自變數、應變數的關係明確表示時，
可以使用 least square method 求解，例如我們有 10 個觀察值
(1, 4), (4, 5), (1, 2), (4, 5), (6, 9),
(1, 8), (4, 5), (3, 4), (5, 5), (6, 6) 等，
而我們先猜測它們的關係是二次的，應該要符合 :math:`$Y = a \times X^2 + b \times X + c$` 方程式，
有了觀測值及預估方程式形式後，接下來就可以利用 least square method 計
算出 :math:`$a$`, :math:`$b$`, :math:`$c$` 三個係數。

評估非線性方程式的係數值
-----------------------------------------------------------------------------
---

假定一含有 :math:`$n$` 個未知係數的
方程式 :math:`$E(x_1, x_2, ..., x_k, p_1, p_2, ..., p_n)$` ,
在 :math:`$m$` 組觀測值
(:math:`$(y_1, x_{11}, ..., x_{1k})$`, :math:`$(y_2, x_{21}, ..., x_{2k})$`,
..., :math:`$(y_m, x_{m1}, ...x_{mk})$`) 下，
欲求出此 :math:`$n$` 個係數的值，
期使 :math:`$E(x_1, x_2, ..., x_k, p_1, p_2, ..., p_n)$` 與觀測值的誤差最小。

首先定義理論值與觀測值的誤差如式 :ref:`\ref{errors define}` 的 :math:`$f_i$` 。

.. raw:: latex

\begin{equation}\label{errors define}
f_i(p_1, p_2, ..., p_n) = y_i - E(X_i, p_1, p_2, ..., p_n), i \in 1, ..., m
\end{equation}

\begin{equation}\label{F function}
F(p_1, p_2, ..., p_n) = \sum_{i=0}^{m} (f_i(p_1, p_2, ..., p_n))^2, m \geq n
\end{equation}

將每一觀測值誤差平方並加總起來，可得到一目標函式 :math:`$F$` 其定義如式 :ref:`\ref{F function}` 。
當 :math:`$ F $` 函式的值為全域最小值或是區域最小值，
其特定 :math:`$ [p_1^*, p_2^*, ..., p_n^*] $` 組合，
也就是 :math:`$P^*$` ，即為該 :math:`$ E $` 函式的係數全域或區域最佳解。

所有的非線性最佳化都是用迭代方法計算的：
從一個起點 :math:`$P_0$` 開始搜尋，產生一系列的向量 :math:`$P_1, P_2, ..., $` ，
希望可以收斂至一個 :math:`$ P^{*} $` ，使得函式成為全域或區域
最佳解 :cite:`\cite{k_madsen_imm_2004}` 。

.. raw:: latex

\begin{equation}\label{Taylor expansion}
F(P_{k+1}) = F(P_k) + h^{\top} {F}'(P_k) + \frac {1}{2} h^{\top} {F}''(P_k) h
+ O(||h||^3)
\end{equation}

\begin{equation}
h = P_{k+1} - P_k
\end{equation}

如式 :ref:`\ref{Taylor expansion}` ，首先以 Taylor expansion 改寫 :math:`$ F $` 函式，
:math:`$O(||h||^3)$` 代表後面無窮盡的項目，
:math:`$ k $` 代表的是第幾次 iteration 。在每次 iteration 中，
我們先找出 :math:`$ h $` ，使得 :math:`$F(P_{k+1}) < F(P_k)$` 。
目前常見計算 :math:`$h$` 的逼近法有 The Steepest Descent method,
Newton's method, Guass-Newton method, The Levenberg-Marquardt method。

The Steepest Descent method
*****************************************************************************
***

Steepest Descent method 將式 :ref:`\ref{Taylor expansion}` 改寫
為式 :ref:`\ref{Taylor expansion2}` ，忽略二階以後項目。

.. raw:: latex

\begin{equation}\label{Taylor expansion2}
F(P_{k}+\alpha h) \simeq F(P_k) + \alpha h^{\top} {F}'(P_k), \alpha > 0
\end{equation}

而原來的 h 改寫成一個純量 :math:`$\alpha$` 再乘以向量，這樣在 :math:`$P_{k+1}$` 接
近 :math:`$P^{*}$` 時， :math:`$\alpha$` 必定近似 0 ，
所以我們又可以得到式 :ref:`\ref{steepest descent}` ，

.. raw:: latex

\begin{equation}\label{steepest descent}
\lim_{\alpha \to 0} \frac{F(P) - F(P + \alpha h)}{\alpha \left \| h \right
\|}
= - \frac{1}{\alpha \left \| h \right \|} h^{\top} {F}'(P)
= - \frac{h^{\top}}{\alpha \left \| h \right \|} \frac{{F}'(P)}{\left \|
{F}'(P) \right \|} \left \| {F}'(P) \right \|
= - \left \| {F}'(P) \right \| cos \theta
\end{equation}

:math:`$\alpha \left \| h \right \|$` 為純量，所以我們
希望 :math:`$F(P)-F(P+\alpha h)$` 的值愈大愈好，
這樣 :math:`$ cos \theta $` 就必須為 -1 ，
而 :math:`$cos \theta$` 是 :math:`$h$` 與 :math:`${F}'(P)$` 的夾角，
所以如式 :ref:`\ref{sd}` ，最佳的 :math:`$h_{sd}$` 必為 :math:`$-{F}'(P)$` 。

.. raw:: latex

\begin{equation}\label{sd}
h_{sd} = - {F}'(P)
\end{equation}

如式 :ref:`\ref{sd}` ，陡降法中的 :math:`$h_{sd}$` 是以斜率值負值為移動方向。
而 :math:`$\alpha$` 的值，
我們需用 line search 求得，但效率通常會是個問題，所以也可以使用 binary search 方式來求得，
其概念是先取得一個 :math:`$\alpha_{min}$` 值讓 :math:`$F(P)-F(P+\alpha h)$` 大於 0 ，
再取得一個 :math:`$\alpha_{max}$` 值讓 :math:`$F(P)-F(P+\alpha h)$` 小於 0 ，
接下來以 :math:`$\frac{1}{2}(\alpha_{min} + \alpha_{max})$` 為
新的 :math:`$\alpha_{middle}$` 值，
去計算 :math:`$F(P)-F(P+\alpha h)$` 是大於 0 還是小於 0 。若大於 0 ，則
新的 :math:`$\alpha$` 值
應為 :math:`$\frac{1}{2}(\alpha_{middle} + \alpha_{max})$` ，若小於 0 ，則新
的 :math:`$\alpha$` 應為 :math:`$\frac{1}{2}(\alpha_{middle} + \alpha_{min})$` ，
如此迭代計算後，當 :math:`$\alpha$` 滿足預設條件或達迭代次數即可決定。

Newton's method
*****************************************************************************
***

牛頓法則考慮以 :math:`$ F $` 函式的二階 Hessian 矩陣來計算 h 。
它將式 :ref:`\ref{Taylor expansion2}` 再取其一次微分得到
式 :ref:`\ref{Taylor expansion for newton}` ，若 :math:`$(P_k + \alpha h) =
P^{*}$` ，
則 :math:`${F}'(P_k + \alpha h )$` 必等於 0 。

.. raw:: latex

\begin{equation}\label{Taylor expansion for newton}
{F}'(P_{k}+\alpha h) \simeq {F}'(P_k) + \alpha h^{\top} {F}''(P_k), \alpha >
0
\end{equation}

所以我們可以得到式 :ref:`\ref{newton}` ，而 :math:`$h_{n}$` 就等於
式 :ref:`\ref{newton2}` 定義。

.. raw:: latex

\begin{equation}\label{newton}
0 = {F}'(P_k) + \alpha h^{\top} {F}''(P_k)
\end{equation}

.. raw:: latex

\begin{equation}\label{newton2}
h_{n} = - \frac{{F}'(P)}{\alpha {F}''(P)}
\end{equation}

在搜尋效率上，牛頓法為二元收斂，而陡降法為線性收斂，所以牛頓法在接近最佳解時比較快，
而陡降法則是離最佳解較遠時比較快，且因 Hessian matrix 在計算上
不一定為 positive definite ，所以牛頓法往往會混合陡降法來實作。

The Guass-Newton method
*****************************************************************************
***

Least squares problems 一般能用陡降法或是牛頓法求解，但要追求效率的話，我們應該作部份調整。
像是盡量使用二元收斂或是不需實作出 :math:`$F$` 函式 :cite:`\cite{k_madsen_imm_2004}` 。

我們將式 :ref:`\ref{Taylor expansion}` 的 :math:`$F$` Taylor expansion 改使用
在 :math:`$f$` 上，如式 :ref:`\ref{f Taylor expansion}` 。

.. raw:: latex

\begin{equation}\label{f Taylor expansion}
f(x + h) = f(x) + J(x) h + O(||h||^2)
\end{equation}

\begin{equation}
(J(x))_{ij} = \frac{\partial f_i}{\partial x_j}(x) = {f}'(x)
\end{equation}

式 :ref:`\ref{f Taylor expansion}` 可再整理為式 :ref:`\ref{f Taylor expansion2}` 。

.. raw:: latex

\begin{equation}\label{f Taylor expansion2}
f(x + h) \simeq l(h) \equiv f(x) + J(x) h
\end{equation}

\begin{equation}\label{new F Taylor expansion}
F(x + h) \simeq L(h) \equiv \frac{1}{2}l(h)^{\top}l(h)
= \frac{1}{2}f^{\top}f + h^{\top}J^{\top}f + \frac{1}{2}h^{\top}J^{\top}Jh
\end{equation}

再將式 :ref:`\ref{new F Taylor expansion}` 對 h 作一次微分得到式 :ref:`\ref{gn function}`
。

.. raw:: latex

\begin{equation}\label{gn function}
{L}'(h) = J^{\top}f + J^{\top}Jh
\end{equation}

因為在最佳解時， :math:`${L}'(h)$` 等於 0 ，所以我們可以得到 :math:`$h_{gn}$` 如
式 :ref:`\ref{guass-newton}` 。

.. raw:: latex

\begin{equation}\label{guass-newton}
h_{gn} = - \frac{J^{\top}f}{J^{\top}J}
\end{equation}


The Levenberg–Marquardt method
*****************************************************************************
***

The Newton's method may not be defined beacause of the singularity of
:math:`$ {F}''(P_k) $` at
a given point :math:`$ P_k $` , or the search direction :math:`$ h_n $`
may not be a descent direction
:cite:`\cite{bazaraa_nonlinear_2006}` .
The algorithm used the gradient methods their ability to converge from an
initial guess which may be outside
the region of convergence of other methods. The algorithm uses the Taylor
series method the ability to close
in on the converged values rapidly after the vicinity of the converged
values has been
reached. Thus, The method combines the best features of its predecessors
while avoiding their most serious
limitations. :cite:`\cite{marquardt_algorithm_1963}` .

Levenberg-Marquardt 方法乃加入一 damping parameter :math:`$ \mu $` 。

.. raw:: latex

\begin{equation}
h_{lm} = - \frac{J^{\top} f(P)}{J^{\top} J + \mu I}, J = {f}'(P), I =
Identity\ Matrix
\end{equation}

此自定參數的效益在於，For all :math:`$ \mu > 0 $` the coefficient matrix is positive
definite,
and this ensures that :math:`$h_{lm}$` is a descent direction. For large
values of :math:`$ \mu $` we get

.. raw:: latex

\begin{equation}
h_{lm} \simeq - \frac{1}{\mu}{F}'(P)
\end{equation}

If :math:`$ \mu $` is very small, then :math:`$ h_{lm} \simeq h_{gn} $` ,
which is a good step in the
final stages of the iteration, when P is close to :math:`$ P^{*} $` .
If :math:`$ F(P^{*})=0 $` (or very small),
then we can get (almost) quadratic final convergence
:cite:`\cite{k_madsen_imm_2004}` .

:math:`$\mu$` 值在每個 iteration 中，皆不同，而 :math:`$ \mu_{k} $` 的選擇，
主要有兩種方法，
一是看 :math:`$J(P_{k})^{\top} J(P_{k}) $` 中，
對角線元素中最大值再乘以 :math:`$ \gamma $` ，
一般來說， :math:`$\gamma$` 的值介於 :math:`$ 10^{-6} \sim 1 $` 之間。
或是也可以用 :math:`$ F(P_{k}) - F(P_{k-1}) $` 的值 :math:`$s_{k}$` 來判斷，
當 :math:`$ s_k \geq 0 $` 時
， :math:`$ \mu_k $` 增加 10 倍，
當 :math:`$ s_k \le 0 $` 時， :math:`$ \mu_k $` 減少 10 倍，
:math:`$ \mu_0 $` 的初始值則是設為 0.001 。

小結
-----------------------------------------------------------------------------
---

理論上，非線性最佳化是很難求得全域最佳解的，就算你運氣真的很好，
瞎貓怕上死耗子，讓你遇到全域最佳解，但你還是沒有辦法去驗證它的確是全域最佳解。
只有在某些特殊題型下，你才知道所求出的解是全域最佳解，最簡單的例子就一元二次方程式，
當它是凹向上時，有全域最小值，當它是凸向上時，有全域最大值。

所以，以上介紹的 4 種找尋 h 的方法，都只是一種有系統的找尋技巧，這些方法經過數學推導，
可算是比較有效率罷了，不代表只有這些方法可以用在 least square problem 上。
你也可以任意混合這 4 種方法，如在第 1 ~ 10 次迭代時，使用陡降法，在第 11 ~ 20 次時，
使用 Levenberg-Marquardt 方法，在第 20 次以後一律使用高斯-牛頓法，
這種方法是沒有對錯的，只有解題時間的快與慢而已，而這快與慢就又牽扯到起始值的挑選及非線性函式的特性。
這次這樣用比較快，不表示這對其他問題的解題速度就會比較快。

References
[1] M. S. Bazaraa, Hanif D. Sherali, and C. M. Shetty. Nonlinear programming.
John Wiley
and Sons, 2006.
[2] K. Madsen, H. B. Nielsen, O. Tingleﬀ, and Mathematical Modelling. IMM
METHODS
FOR NON-LINEAR LEAST SQUARES PROBLEMS, 2004.
[3] Donald W. Marquardt. An algorithm for Least-Squares estimation of
nonlinear parameters.
Journal of the Society for Industrial and Applied Mathematics, 11(2):431–441,
June 1963.
ArticleType: primary_article / Full publication date: Jun., 1963 / Copyright
1963 Society
for Industrial and Applied Mathematics.

.. _PDF: http://www.hoamon.info/opentrunk/least_square_problem_v4.pdf
.. _rst: http://www.hoamon.info/opentrunk/least_square_problem_v4.rst


.. author:: default
.. categories:: chinese
.. tags:: the guass-newton method, the steepest descent method, levenberg-marquardt method, least square method, math, Newton's method
.. comments::
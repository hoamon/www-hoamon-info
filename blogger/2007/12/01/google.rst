讓 google 幫你作圖表
================================================================================

過去作研究時，為了要看清楚數據的結果是不是與我們所想的一樣，我們會把數值轉成圖表的方式展示，這比起看到 1,2,4.0,8,...
的數字能更快速了解答案的正確與否。

因為以前都是用 matlab 作研究，所以生圖表時，是在單機上生成一個圖檔來看，若不用 matlab 也可以，把生成的數據倒給 gnuplot
一樣可行，或者是直接用 GNU Octave 也成。

我們現在都是用 python 了，而在 python 上也有十分優秀的圖表函式庫 `matplot`_ 可以用。

只不過，現在不只是要求數學程式化，我們也要作模式商業化，一個可行的解題方式，我們要讓使用者方便使用，最簡單的方法是讓它變成網站。這時候使用 matplot
就有點麻煩了。

如果可以使用 `google chart api`_ ，就會比較輕鬆，而且流量還可以丟過 google 處理。只不過，機密的數據還是不要透過 GET
方法讓 Proxy 儲存到，這時候，還是用 matplot 吧!

打個廣告，歡迎有程式設計能力且數學(離散、管理數學、統計)底子好的人才來我們 `lab`_ 唸碩博士，我們 lab 的目標主要是用資訊技術讓工程的品質、生
產力提高。考試科目有營建管理概論、工程經濟/工程統計，基本上，我在土木系的大學部也只學過營建管理概論(三學分)，工程經濟/工程統計是得自己另外唸的。

.. _matplot: http://matplotlib.sourceforge.net/
.. _google chart api: http://code.google.com/apis/chart/
.. _lab: http://www.ce.nchu.edu.tw/teacher30.htm


.. author:: default
.. categories:: chinese
.. tags:: gnuplot, python, matlab, math, cmclass
.. comments::
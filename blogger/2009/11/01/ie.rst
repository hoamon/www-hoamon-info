莫明奇妙的 _ 網域名稱錯誤： 只發生在 IE 上
================================================================================

嚴格地說，這也不是 IE 的錯， IE 只是遵守規範而已。但是因為 Firefox 的容錯能力，讓我們一時以為是 IE 太爛了。

問題是這樣的：

我學弟使用 Windows 加 apache 配置一個測試網站給業主使用時，一直面臨 IE 不能登入，但 Firefox 卻正常的問題，而該網站在
django development server 運作時，卻又沒有問題。他搞了非常久，大概有一個月吧!

我幫他 debug 時，一開始，我就把問題縮小在 IE 瀏覽這 apache 上的測試網站時，它不會紀錄 Cookies，沒用 Cookies
，那怎麼保持認證連線呢! 只是那時候，我也是找不出為什麼那該死的 IE 就是沒法使用 Cookies ，而優秀的 Firefox 就可以呢!
然後，我使用了 Ubuntu Linux 配置這個測試網站結果發現它可以讓 IE 正常運作，所以我們當時只能歸納這問題，一定是他的 XP 出了狀況。

結果前兩天，他要把測試網站放到業主的機器上去 run 時，還是出了相同的問題，然而這次不一樣的是那個機器有兩個 django-based site
，但一個正常，一個不正常。這就有點說不過去了。

於是，這次我請教了 Google 大神，問它： django cookie session problem ie ，而它回我：
`http://code.djangoproject.com/ticket/7264#comment:3`_。

這原來是 _ 的錯，因為學弟習慣將測試網址設成 test_XXX.YYY.ZZZ ，而我習慣設成 XXXtest.YYY.ZZZ
，因為我知道在買網址時只可以買英數字加連字詞(-)的，所以我不會在網域名稱中放入 _ ，也就是這個習慣讓我在 Ubuntu Linux
中架的測試網站是可以讓 IE 正常使用，但學弟架在 Windows 上的測試網址卻包含了 _ ，讓 IE 勇於拒絕他的要求了。

這同時也解釋了為什麼在 django development server 運作時， IE 可以正常的現象，因為它會使用
http://127.0.0.1:8000/ 作瀏覽網址。

哈哈，真不曉得該怪 IE ，還是得怪 Firefox 呢! 不過，話說回來，要是早點問 Google 大神，這問題就不會拖一個月了。

.. _http://code.djangoproject.com/ticket/7264#comment:3:
    http://code.djangoproject.com/ticket/7264#comment:3


.. author:: default
.. categories:: chinese
.. tags:: firefox, ie, django, linux, python, google, apache, ubuntu
.. comments::
使用「公認機構簽核公錀」所發生的不知名問題
================================================================================

在 `How to get a free HTTPS web certification authority by StartSSL.com`_
一文中，我申請了 A.hoamon.info 的公錀簽核，也正確地跑在 https 上，在使用瀏覽器觀看時，完全沒有問題。然而在 hg 軟體上，卻會發生
SSL: Server certificate verify failed. 的錯誤訊息，從 `Mercurial on Windows vs
Linux, spot the problem`_ 一文中，作者解釋是 Windows 的 ssl 版本太舊的原因，但照他的解決方案處理，我的 hg
軟體卻是報 URLError. 錯誤。

後來在檢查 apache.conf 時發現，這台機器有三個 https 站台，一個是用 A.hoamn.info 的公錀，另外兩個 B, C 站台卻都是用
whatever.hoamon.info 的公錀。而 B, C 站台的設定檔寫得比 A.hoamon.info 站台還前面。所以試著調動
A.hoamon.info 到 B, C 站台設定的前面，結果 hg 軟體就正常了。

問題是解決了，但我反而混亂了。印象中， https 協定中，公錀是在 IP 層(或表現層，我不確定)就發送至使用者的瀏覽器，既然沒到應用層，則網頁伺服器就
不知道該拿那一個虛擬站台的公錀給使用者，於是它總是拿第一個看到的公錀(也就是寫在最前面的)，所以這篇`教學文章`_，才會寫到：「…一個 Apache
，也只能架一個 SSL 站，用一個站名。除非妳跑很多份 Apache ，各自跑在不 同的 IP 或不同的 TCP 埠上，才能在同一臺伺服 器上，跑好幾個
SSL 站。」

實際上，在 Windows XP 的 IE, Safari 上觀看 A, B, C 三個站台，也的確都是拿到 A.hoamon.info 的公錀。但在
Chrome, Firefox 上，卻是看到 A 用 A.hoamon.info ，但 B, C 用的是 whatever.hoamon.info
的公錀。




這我頭大了，為什麼跟基本原理不一樣??? 還是因為某些瀏覽器有「重拿公錀的機制」存在???



.. _How to get a free HTTPS web certification authority by StartSSL.com:
    http://hoamon.blogspot.com/2011/04/how-to-get-free-https-web-
    certification.html
.. _Mercurial on Windows vs Linux, spot the problem:
    http://notes.benv.junerules.com/all/software/mercurial-on-windows-vs-
    linux-spot-the-problem/
.. _教學文章: http://www.study-area.org/tips/certs/certs.html#apache


.. author:: default
.. categories:: chinese
.. tags:: ie, linux, ssl, windows, chrome, apache
.. comments::
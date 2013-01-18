ExplorerCanvas:IE瀏覽器上的js修正檔
================================================================================

之前還信心滿滿地跟人家說，不會有人在瀏覽器上開發圖形函式庫呢~今天就被打巴掌了。

這個 `ExplorerCanvas`_ 程式也不算是讓 IE 瀏覽器上跑 2D 圖形運算的函式庫，它其實是一個讓 javascript
程設師能設計跨瀏覽器的 javascript 程式。為什麼要這樣作呢!原因就出在微軟喜歡用自己的方式來造輪子，所以其他的 Firefox 、 Opera
、 Safari 都支援相同的 tags 來完成 2D 的圖形運算，但 IE 用自己的 ActiveX 元件。

所以只要在你的網頁前頭先載入這個 ExplorerCanvas.js 檔，那麼你呼叫執行的 js 就不用分瀏覽器了。

下面是它的一些範例：

`http://www.nchu-cm.com/examples/example3.html`_ - 裡面的圖有4mb，請小心使用。
` http://www.nchu-cm.com/examples/example2.html`_
`http://www.nchu-cm.com/examples/example1.html`_

世界何其大，還是仔細研究過再說吧!

.. _ExplorerCanvas: http://code.google.com/p/explorercanvas/
.. _http://www.nchu-cm.com/examples/example3.html: http://www.nchu-
    cm.com/examples/example3.html
.. _ http://www.nchu-cm.com/examples/example2.html: http://www.nchu-
    cm.com/examples/example2.html
.. _http://www.nchu-cm.com/examples/example1.html: http://www.nchu-
    cm.com/examples/example1.html


.. author:: default
.. categories:: chinese
.. tags:: javascript, firefox, explorercanvas, ie, safari, opera
.. comments::
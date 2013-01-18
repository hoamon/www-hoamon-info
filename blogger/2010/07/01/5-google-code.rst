「郵遞區號」： 3+2 = 5 碼郵遞區號查詢離線網頁程式(已放上 Google Code)
================================================================================

當我開始開發資訊系統時，就一直認為地址處理是一般資訊系統中最基本且常見的功能。不過，目前使用過的資訊系統，了不起就是把 3
碼郵遞區號作完而已，很少看到網頁系統有作到無碼 5 碼的地址處理功能(當然啦，郵局自家的確有提供 5
碼查詢功能，但是不好用)。所以我想郵局苦心推動大家使用 5 碼，除了能讓寄信速度加快外，未來在許多 GIS 應用愈來愈普及下，我相信大家都會利用 5
碼郵遞區號來作加值應用的。

所以為了搔自己的癢，我寫了 `http://zipcode.ho600.com/`_ 網站，除了可作`網上查詢 5 碼功能`_外，也把 HTML5 的
Offline 作進去，讓查詢功能可在無網路的本機端處理。另外也提供其他人嵌入「地址查詢表單」的方法。詳細說明請見「`嵌入方法`_」，本專案我也放到
`Google Code`_ 開發，授權條款是 NEW BSD License ，希望能聽到您們的聲音。

這個程式是跑在 GAE 上的，不過可以很容易地移稙到其他框架中，因為這個功能，我主要是用 javascript 開發的。 GAE 不過提供檔案放置的功能。

注意，第一次瀏覽會比較慢，因為要把約 2MB 的郵遞區號資訊下載下來。不過，如果你用的是支援 html5 offline 功能的瀏覽器，像
Firefox3.6+, chrome4+, safari4+ 的話，之後就不用再下載了。

範例：



.. _http://zipcode.ho600.com/: http://zipcode.ho600.com/
.. _嵌入方法: http://zipcode.ho600.com/embeded.html
.. _Google Code: http://code.google.com/p/zipcode-3plus2/


.. author:: default
.. categories:: chinese
.. tags:: javascript, zipcode, html5, google app engine
.. comments::
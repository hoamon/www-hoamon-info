ImageMagick 讚啦! 輕鬆作 PDF 2 JPG
================================================================================

因為想要使用 rst 、 latex 作為我的主要寫作格式。那麼在與別人互動時，對方想要編輯我的檔案時，該怎麼辦呢?
尤其是在專案二次外包時，計畫書可能須要上包先審視過。

那這時該如何顧及「計畫書的版本修改追蹤能力」及「對方人員編輯文件的親和力」呢? 總不能叫上包廠商的承辦人也學會 rst 格式吧!
雖然很簡單，但對認為「所見即所得就是王道」的人來說，這是不可能的事。但如果叫我用 Word + SharePoint ，我想別人也不一定好上手，單單只用
Word 的話，那就又回到原點了，它根本就不適合作一個協同平台中的文書編輯軟體，比 Google Docs 還不如，但 Google Docs
又不能吃太大的檔案，而且我就是不喜歡「所見即所得」的文書編輯軟體。

所以本來我是想找一些 Open Source 的 PDF 編輯軟體，讓他們能把意見以註解或劃線方式標記在 PDF 檔上。不過實在沒找到幾個簡單應用，而且
Windows 安裝方便的。直到看到 `http://www.pdfescape.com/`_ 這個網站的功能，才發現可以自己作一個線上編輯 PDF
的平台。

只要能把 PDF 檔先轉成 JPG 檔，然後結合 AJAX 技術讓使用者在文件圖片上，放置註解文字及劃線，編輯完成後，再通知我作修改，這樣一來，上包的意見
也可一併作版本控制了。不會發生該改未改，沒必要改的卻被弄亂的糊塗事。

好吧! 最重要的技術就是把 PDF 檔轉成 JPG 了。那該怎麼作? 在 Linux 下，實在是非常簡單，簡單到，我覺得這個線上 PDF
編輯平台已經寫好了 50% 。

指令如下：

# convert XXX.pdf XXX.jpg

這樣 ImageMagick 就幫你把 XXX.pdf 轉成 XXX-*.jpg 的圖檔了，每一頁是一張 JPG
。只不過，它的預設參數轉出來的圖檔解析度不高，所以最好再加上幾個參數。

# convert -verbose -colorspace RGB -resize 1800 -interlace none -density 300
-quality 100 XXX.pdf XXX.jpg

這樣它轉出來的圖，在 width 部份就是 1800 pixel 了。實在是讚啦!!

下圖就是成果：
`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/Si9oc08CVWI/AAAAAAAAB4o/yiz
otsMrzqM/s400/TotalWebBase-5.jpg
`_

.. _http://www.pdfescape.com/: http://www.pdfescape.com/
.. _下圖就是成果：: http://3.bp.blogspot.com/_eKM9lHjTZjs/Si9oc08CVWI/AAAAAAAAB4
    o/yizotsMrzqM/s1600-h/TotalWebBase-5.jpg


.. author:: default
.. categories:: chinese
.. tags:: pdf2jpg, linux, jpg, pdf, pdftojpg, imagemagick
.. comments::
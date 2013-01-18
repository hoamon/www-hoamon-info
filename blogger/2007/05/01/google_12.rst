我也申請了「Google 應用服務」
================================================================================

看了`Google 應用服務教育版`_後，發現它不只限定教育機構，其他像個人、公司…皆可申請。

過去(大約1年半前)，因為我十分欣賞 GMail 的功能，所以把我的 *@hoamon.info(or *@`amon.idv.tw`_) 信箱利用
Postfix Relay 轉到 ｈｏａｍ０ｎ＠ ｇmａil.c０m 。這樣我就可以利用 Gmail 介面來處理 *@`hoamon.info`_
的信件。這麼作是因為我不知道 Google app 的原因，如果使用 Google app 的話，我就可以省下2台 Postfix
伺服器了(是的，我還有作備援喔)

申請方式很簡單，只要你完全擁有1個 domain name ，可以設定 MX 及 CNAME 記錄的就行了。申請時，我還非常客氣地只寫下20個帳戶，沒想到
Google app 直接幫我升到50個。

現在，我可以停掉兩台 Postfix 了，而且我相信郵件接收的妥善率絕對比以前更高。

.. _Google 應用服務教育版: http://hoamon.blogspot.com/2007/05/google.html
.. _amon.idv.tw: http://amon.idv.tw/
.. _hoamon.info: http://hoamon.info/


.. author:: default
.. categories:: chinese
.. tags:: dns, google apps, postfix
.. comments::
千萬不要相信任何一個網頁系統(包含 Google)，除非你用了公私錀(如 PGP)加密
================================================================================

當我們在作業系統(尤其是 Linux)中使用 Open Source 軟體時，我們有一定的信心認為程式作者不會呼隆我們。因為只要有心，我們看得到程式碼。

但對於任何一個網頁系統而言，基本上，你必須將它們都視為壞人，它們絕對拿得到你所上傳的資料，包含密碼 *1。就算它標榜著 Open Source
出品，也不能保證它放置網頁伺服器上的程式碼與 Open Source 版本是一模一樣的。

事實上，在使用網頁系統時，請保持著一種信念：「若要人不知，除非己莫為」。放到網站上的資料，除了你，別人(閘道器管理員、系統管理員、程式設計師甚至是客服小妹
)絕對有辦法打開看，除非你使用公錀加密內文。這一點，就連 Google 網站也不例外。

所以，當我看到無名網站上提供一種「密碼保護文章/相簿」的功能時，我覺得很好笑，看看它在 html form 上所設計的方式，完全是以明碼形式將密碼傳至沒有
https 的網址，這樣何謂「密碼保護」!
無名站上工程師絕對有能力看得到你所保護的內文以及密碼。甚至有可能那些性愛相簿外流的原因中，有部份就是離職員工搞的鬼，但是誰知道呢?
當你用明文形式傳遞密碼時，理論上，它就不叫「密碼」了，當你用明文形式上傳文章或相片時，它們也不會是「有保護」的。

要真正上傳儲存「有保護」的內容，以目前技術來說，最簡單的就是 PGP 加密了。像是下面的密文，你看得出我寫的是什麼了嗎? 雖然，我大方地 po 在
blogger 上，但沒有私錀的人就是看不到。

-----BEGIN PGP MESSAGE-----
Version: GnuPG v1.4.6 (GNU/Linux)
Comment: Use GnuPG with Firefox : http://getfiregpg.org (Version: 0.7.5)

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
ZvAf4PfWSCxGoarWUY+BGaGXCNUNifob+g==
=8e3M
-----END PGP MESSAGE-----

上面的密文，我用了三把公錀作加密，理論上，只有我、我老婆及 `django-pgpauth`_ 的私錀能解開。如果各位有興趣的話，我把 `django-
pgpauth`_ 的私錀(我並未設定密碼)就放在 comment 中，請自取用。

如果你真的覺得要放在網站上的資料是需要隱私的，請不要相信該站所提供的密碼保護功能，用自己的比較安心。

至於如何使用 PGP (Linux/Mac/Windows 皆適用)來加解密及簽章驗證，請參考`此篇`_。

註1： 除非它們在認證網頁上，先用 One-Way Function(如: md5， sha-1) 先將明文密碼轉換過。

.. _django-pgpauth: https://pgpauth.hoamon.info/
.. _此篇: http://hoamon.blogspot.com/2009/05/pgp-linuxmacwindows.html


.. author:: default
.. categories:: chinese
.. tags:: linux, web, pgp
.. comments::
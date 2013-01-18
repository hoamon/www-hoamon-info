我開始使用 PGP 作郵件的簽章及加解密了
================================================================================

如果你也想使用 PGP 作郵件的簽章、加解密的話，可先參照下列幾個連結


-   `http://jedi.org/blog/archives/002590.html`_
-   `http://jedi.org/blog/archives/002591.html`_
-   `http://jedi.org/blog/archives/002592.html`_
-   `http://blog.roodo.com/myroodo/archives/4581241.html`_
-   `http://firegpg.tuxfamily.org/index.php?page=home&lang=zh_tw`_
-   `http://tavi.debian.org.tw/PGPKeysigningParty`_


或是 google:// pgp key

我的作法是在 Ubuntu 7.10 上使用 Firefox + FireGPG(firefox extension) + GnuPG 來完成 Gmail
信件的簽章、加解密。

安裝步驟如下：


-   確定你的電腦裡有 gnupg ，沒有的話，請使用 # apt-get install gnupg 來安裝
-   產生自己的公私錀： # gpg --gen-key
-   將公錀上傳到伺服器，0x244E7AEB 是我的公錀 ID ，請不要照用： # gpg --server subkeys.pgp.net
    --send-key 0x244E7AEB
-   匯出公錀並放到他人容易下載的空間(我的是放在`0x244E7AEB`_)： # gpg -a --export 0x244E7AEB >
    hoamon.public.asc
-   下載 firegpg 程式： # svn co
    svn://svn.tuxfamily.org/svnroot/firegpg/firegpg
-   編譯 firegpg 程式： # cd firegpg; ./build.sh
-   安裝 firegpg 程式： 打開你的 firefox 瀏覽器，選擇安裝擴充套件 firegpg.xpi 。並重新啟動 firefox 。


使用方法：


-   先下載它人的公錀(0xB1E55D7E這是我老婆的公錀)： # gpg --server subkeys.pgp.net --recv-
    keys 0xB1E55D7E
-   進到 Gmail
    信箱中，開新信，然後寫下內容，待寫畢，點選上面的「加密」按鈕，這時候會要求你選擇用那一把公錀加密，選完後，信件內文就會變成下面這個樣子了。


-----BEGIN PGP MESSAGE-----
Version: GnuPG v1.4.6 (GNU/Linux)
Comment: http://firegpg.tuxfamily.org

hQQOAyQbH/dVXCNHEA/7B2AfasQx9MDO+bXi48fn9YoEuQwNkpKsayxXNhEg9Kom
KDYWk6nXr0tbYZuyxYdjY4e42AxuOZ28Ym59OtyOHikZ2TQoqGkjroiVtP+QgcnJ
QEUe3YhTadKr7OCmgIcd94SkOI45KjOgB29VtG3qYQm0rXMM38h9x/zMdbRl51T2
oTCvYeuwJECHg4H+NZNL/XM5ISndIzyuqfescsPbAv/dp6vV7UyB3uQU0RUJ2SwN
vX2W8mPJRklFOzStB0WZNGrGdWnokOeO+iqcbH8eyBeD78t2cm8DNs4W/bjQXLXU
s77CqWYG8jbuV3uNuhdBYw4DD+EOPYuCXZJkQus4dk6eAB3osn4fcP3GjIu7Ln79
rEZ2fBgOT/XJNkvia6jhexsdIodaEYLPYEb64UBYkLZbYZYC1yh2iUGZVdIg1MZJ
YuVLafBfvTn6/d5qpLPc0SmPaj68mDnxrGzNU2G1yUx5Z32xqB5Hp1J+j3EihlAB
R8/yB0ygmZZL3bR/TAqSjenaOj4xcOXZqxeHnaUrWfWstTp72G06w+pLdJ2RRMx3
EPidkHval8uf7SfOaPO2n2jJBNZd6uxycorWPXjTZ4kerg2npuYBu3rStI8bCHi9
Y6xElo0cs8zFcvKoyFA4zSZvfrysaqK9uFfH4VscBoK0lKoKwJb3QOYDAeVVIKsQ
ANaDqdQK5LiP0gWittEkgNVWeHWSldf5F062p+XVsGsrT5bo8IGdeTMeN5BPTMSZ
m/QfTprdEOgsditzO0gHoKioPgyFm7Cu3f+zl9sCyG73oW4/G8dQwCXm5ltElidX
rOcA+6mWfmcnCQChtRrKtVNrJ1DrtItgbzPIYqSV+6VrTo7tlOJPNagvTEUWHyGk
hWW9PwU8x0JMrfGGMzFqiy/mQqO8G6MJvYsYYYWZUkT4wtsbWQArEE2d8qdN0qq3
47oXc1YBIk9A/zEpeCq56+G48qvIBGbFXqylbn7thv3FhC5WYMGumpCZ8gAAyrEm
EdEuU9dVp3gb0GJqLkxlvyjby+Cnp4bvFXfX3teOcfejQ9JS4u84Pu1Zdo7kn3Xo
uii/ZkOWkQoPMjV/Uca/AicQLmMLDEkxJClqf6vgLKDCjh6yzzzyJWkjMQa0HY11
bQrqoxRASzcTPo+VGF8yLaD+xshKW9BZF5uhAbjWdyTUKceEp5PkSpEyAdB4ki+Y
FWc3Qc/DL8dqQrAyFBt2IovqMVzHhHR5vZc0By+qkS2c51aD2Wx/jjELNfqDAidP
c42zB+DRJMxubSFymKD7azf2fDJI7Pmu/k7Ku1ShpwKkMhK3mFHBTVYRNap9hb2e
FN+7kFz2c+rNN0/Hl3frSsxBaPdpW0n+rlh0RFNq+wVs0mABG8lUqL98yElXHbxL
6Ft5rxyJ1Js8/gU61MVJytGAxCnTQVBnPNyy2AmZR1FrYXZ636qa80KbUmf46Gg0
bbx1pNf1dd3WYE/xBcG6SYGXNMpPiO8u3FqhqlrcWyAcMCc=
=iaH4
-----END PGP MESSAGE-----

上面的內容，只有我老婆的私錀才可以解開。其他人一定不會知道內容是「我愛你」。就連我自己也不能再看到它的原始內容了，因為我沒有老婆的私錀。

有一個觀念很重要：「私錀是用來簽章及解密，而公錀用來加密」。因為我的公錀是所有人都可以下載的。如果拿私錀來加密信件的話，那麼我的網路管理員，只要知道信件是
我發的，就可以拿我的公錀來解密了。

.. _http://jedi.org/blog/archives/002590.html:
    http://jedi.org/blog/archives/002590.html
.. _http://jedi.org/blog/archives/002591.html:
    http://jedi.org/blog/archives/002591.html
.. _http://jedi.org/blog/archives/002592.html:
    http://jedi.org/blog/archives/002592.html
.. _http://blog.roodo.com/myroodo/archives/4581241.html:
    http://blog.roodo.com/myroodo/archives/4581241.html
.. _lang=zh_tw:
    http://firegpg.tuxfamily.org/index.php?page=home&lang=zh_tw
.. _http://tavi.debian.org.tw/PGPKeysigningParty:
    http://tavi.debian.org.tw/PGPKeysigningParty
.. _0x244E7AEB: http://ssvn.hoamon.info/OpenTrunk/hoamon.pgp.asc


.. author:: default
.. categories:: chinese
.. tags:: firefox, gpg, linux, firegpg, ubuntu, pgp
.. comments::
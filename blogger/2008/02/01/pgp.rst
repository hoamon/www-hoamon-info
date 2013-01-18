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


Old Comments in Blogger
--------------------------------------------------------------------------------



`yugu <http://www.blogger.com/profile/14245219047036426999>`_ at 2008-02-15T19:33:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

呵，我也在用了.

其實我是很少寄信和幾乎朋友是不會傳一些信給我，但我使用pgp最主要的原因之一是launchpad，而該服務又是對自己有用處的，因此pgp不失為一種有效的安
全工具。

話說使用pgp還是有很深的學問，其中像是協定的代理人等等.

launchpad上也有gnupg的翻譯，有空可以review看看。

`Howdy! <http://www.blogger.com/profile/00717722499874252573>`_ at 2008-03-08T08:57:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recently I am using Picasa too. I found it's quite user-freidnly!! Have you
tried the Facebook?

`visual <http://www.blogger.com/profile/08480526148733325964>`_ at 2009-03-19T15:16:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-----BEGIN PGP MESSAGE-----
Version: PGP 8.0.3 - not licensed for commercial use: www.pgp.com

qANQR1DBw04DmfE8kBUqK3cQEACKsDkrbkpG8eqhr5gOJo9Rqqv3FKMlLnRhJG/k
axSN0AQ8T23kBaIQNR2+P3eK6zruuZKJaQI6NflEMxXx8k15E5LGO50tdebi8+zT
9tICC+fc7rNF8GGTKofuGbnulc91Km1TIAoS+P18LIyYgmcdpQYDG6T9tP485pjz
JARU4NRSAkudEn5uIP8bVAvMZyuEOQCuzwHlNQvhH+8zvrUXNaxwyen6hc0Q2xuO
qmP9RICeKBviyKj8f0VFvT3xagcRzHVK0xfxk8YxyCRswcbJZqDbcC9JPr7z/6Am
ugywUhpfcuYxnPWRpG9zTGZ6TC7kl7yBkKTlZTRDj+NQ1RuSs+jctjkTGimaMiIY
9GNJXMevGwZp3SQ2q9/wWaYoRAbi2V/ZnQB6aRrfop8dVBG9Am8H9CeOPOA0W2eL
CtfPojGW/+IoVVnzlsJ7rY4ON7e+4iHG8er2GVCSuX2rifbUaSG52agVvI7p9B7i
Bg9O69GCS+t1S973Bxxx22Bd+UKaLG+LYrsYsTsMtjOEA/b3AELMAedHceIbAMhe
jEnje+X3ahVgi3szi0b1OUbRqwypApis5QMjCecU9w3HFZv8n6uaU2z3jdYSJJC1
aysin+Hn7o/N9m9x9moSLe/yrlN1TbvEgR5gC6LdMMicWC1Ols/4HdC1vhA9IwJU
9NwKrA//WA52sZrMGswx8g1bdAE2fF1iqP+eSSlvetcqjD7fygUgOUyO/bEcqhqq
A4Ks3leeRXVN9ETeuMu+0Rq0wBDyiOWa5cjmoeChe6UEsgsY3Zgg0J+Wv6FkO5Sq
AuxZaDaXMkHYQyhVzXbcgp1UKc/FJHdcf15BKFihPnlf+BRmcaiB9iMQpElUzYAS
7hC/UkthqyPqWMKZsyRY8I6i5r+pPvwiOAjKoTFcPUWSn7GmBeS5dFDCkI8swcw1
FpPCcdzQ501O3Sx9kHh4n6o9KmwwOMYMG06iDYVGT1NBlkJBAdiVytWEwvP7pmqN
blqZagmrk0JpilZgpboYCDT1kyLwGj28CCyq673teVWbDQiv3bK2Pv7W9YEjV4Ec
jc4jrwUKSgQOh954qx5oZLoSdgZffowThzfwqfGcm/mFfFAVsorM4OOtFrf5fc57
AMkYuW21eC1cNKJwnBzU3eIzeZL0AQbbJwEBEfqNU5m4O6gOKiLNLD3IKTJ5wdUs
sZyeIV2kfn/O0MfGUNfFiHa9vCKR9ycWRNRrCs74C4+WOcnQYmECfSSdzNfwjrSQ
6/+6cV92Di7Q0Q74tePT9IVBdOWPWHKx806vflqcrWJYIvlFVruFXpLoxoWUc/sL
Ec7u79RGVx7iiKgQ5EHIrNx9/wNsh0n033mhbI3E/u1T1PmFEnHSwK4BjITKy1nn
b0ir40WNemj4+6KvCXoctaTjfdxQdZPjw+x666BgjHAehV0HLjFi1/QYYHQYSm/Z
hdD339O5FLVHE8u7n/RXYvQdo7IplEfzYHF1fBIGMkT1Q9T5WZ5ygnbw6QGCZrTx
6Wj7/TWF5Ctxu1Gj+bS7fBidZC2RyfMI8RX/0ZbbcNa9+EaUAcQZNLe2dlTkAec3
7HB16XpWbixXCvdwSR3SbAlF2ZEUOQyOLuOSkD602LZcjOYYrazetId7vw0Rn/SE
P7THwb38FMivrJ4byvm2mC4j++uwTNjZgPXkCpZYurXL5ZePmlYrQLQk0XxktE4d
A8tNZsrjQRmdtMvcTYB+LNqluIVPnmoJlLzFrxRAEZFsDljWUcwOZ7aFJsmAooAa
zN2AB1F2qHtQyTxTTO+gKlgZRhOpoeUVj4TGSPGNPR18qg3ZJ0KDPh7M6Iv+qzKt
GGT0+7lTFKbnToDqewZR/kkFMpT60FQ=
=tpPK
-----END PGP MESSAGE-----

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2009-03-19T21:46:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

to visual:
我的 Gmail 因為跑了 offline 模式，我覺得他怪怪的，不曉得你會不會收到我的信。所以我再把信件內容貼在這裡。

-----BEGIN PGP MESSAGE-----
Version: GnuPG v1.4.6 (GNU/Linux)
Comment: Use GnuPG with Firefox : http://getfiregpg.org (Version: 0.7.5)

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
5VzCqsTUa5waVJdhu35BTcOMRR06vHj7coNR
=rlSr
-----END PGP MESSAGE-----

`easy PGP <http://www.blogger.com/profile/06838660695597946077>`_ at 2010-04-07T08:49:33.547+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

web-based的PGP加密工具,如果你是企業MIS,這可以參考看看
http://www.ezpgp.com
http://www.asiapeak.com/ezpgp_server.php

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2010-04-07T11:26:17.659+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

web-based PGP加密工具的一樣沒法避免 web server 遭人入侵，或是該系統管理員想動手腳。

這只解決了一個問題，而又造成另一種問題，最好隱私保密手段，就要在自己的手上就處理完畢。送離到別的機器，又會造成另一種風險。請見我的另一篇文章「`千萬不要相
信任何一個網頁系統(包含 Google)，除非你用了公私錀(如 PGP)加密`_」

.. _千萬不要相信任何一個網頁系統(包含 Google)，除非你用了公私錀(如 PGP)加密:
    http://hoamon.blogspot.com/2009/05/google-pgp.html


.. author:: default
.. categories:: chinese
.. tags:: firefox, gpg, linux, firegpg, ubuntu, pgp
.. comments::
E-Sun WebATM at Ubuntu 8.04+(32 / 64bits皆宜)
================================================================================

= 後記 =
我現在也可以在 Ubuntu 9.10 amd64 上使用了
= 後記結束 =

曾經上過一堂英聽課，老師在課堂上問我：「未來在台灣，可不可能是男女平權的」? 我說：「不可能，因為有很多事男人可以作，但女人不能作!」
她接著問：「以前女人沒有投票權，現在有了;
以前女人的工作單一，多半是在家照顧小孩，現在卻可以選擇非常多樣的職業。目前的確是男女不平等，但一天一天進步，總有一天是男女平權的。」

是的，很多事物的狀態不是靜止，而是動態的。

過去，我回到 Windows 下，不外乎是 WebATM 轉帳、報稅及列印某些特定格式的文件。但現在，「 WebATM 轉帳」功能可以在我的 Ubuntu
9.04 i386 上成功使用了，我相信未來「報稅」一定也可以，而這「特定格式文件」總有一天會不存在或是沒必要使用。

感謝`玉山銀行`_的技術團隊讓我們可以使用這麼方便的軟體，我決定下一次轉帳一定要用玉山銀行 WebATM ，給它收取 17 元的手續費(註1
請見文末附圖)。有機會，我也要辦玉山銀行的戶頭，因為我住埔里，最近的分行在草屯，所以不能想辦就辦。而且，我還要買 2884 玉山金的股票。

有趣的是，之前我就聽過華南銀行也想脫離 IE 的魔掌，不過反到是玉山銀行先作到了，先講可沒有先贏呀!

我在 Ubuntu 9.04 中，是使用 Firefox 3 及虹堡科技 EZ-100PU 讀卡機來作 WebATM 操作的。安裝方法如下：

# sudo apt-get install pcscd libpcsc-perl pcsc-tools libccid

因為虹堡 EZ-100PU 讀卡機目前提供的驅動程式並不支援 Ubuntu 8.10/9.04 預設的 pcsclite(pcscd)
套件，如果您使用的讀卡機是這個型號，在安裝 pcscd 套件後，下載這個以` libUSB 編譯的 pcscd `_，覆蓋原來的 pcscd 。

# tar -zxf pcscd_for_LibUSB.tar.gz
# cd pcscd
# ./install.sh

再到虹堡科技的網站下載 EZ-100PU 的`Linux(Ubuntu)驅動程式`_。

# tar -zxf 200962419545046871.gz
# cd EZUSB_Linux_x86_v1.4.7_For_Ubuntu
# ./check_env
# sudo ./install
# sudo reboot

重新進入系統後，請插上你的讀卡機，並檢查所有程式是否正確安裝：

# pcsc_scan
PC/SC device scanner
V 1.4.14 (c) 2001-2008, Ludovic Rousseau
Compiled with PC/SC lite version: 1.4.99
Scanning present readers
0: CASTLES EZ100PU 00 00

Fri Jun 19 15:49:51 2009
Reader 0: CASTLES EZ100PU 00 00
Card state: Card removed,

有看到 EZ100PU 及 Card removed 字樣，表示讀卡機正確安裝，且未插晶片卡。這時候再插入晶片卡，可以看到 Card inserted
字樣，即表示硬體安裝已完成。

Fri Jun 19 15:50:22 2009
Reader 0: CASTLES EZ100PU 00 00
Card state: Card inserted,
...

最後打開 Firefox ，並到 `https://addons.mozilla.org/zh-TW/firefox/addon/12324`_
下載玉山銀提供的 firefox plugins 安裝後，即可在玉山銀的
WebATM(`https://netbank.esunbank.com.tw/webatm/`_) 中使用。

* 註1: 男子漢不空口說白話。
`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/SmAUk7RliOI/AAAAAAAAB9g/Vql
1EYjnXu8/s400/Screenshot.png
`_
`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/Sm7he0q_QJI/AAAAAAAAB90/-lK
7mBLGd_c/s400/Screenshot-1.png
`_

.. _玉山銀行: http://www.esunbank.com.tw/
.. _ libUSB 編譯的 pcscd :
    https://netbank.esunbank.com.tw/webatm/cabs/pcscd_for_LibUSB.tar.gz
.. _Linux(Ubuntu)驅動程式: http://www.casauto.com.tw/in-
    download-02.aspx?cid=C_00000001&id=P_00000001
.. _https://addons.mozilla.org/zh-TW/firefox/addon/12324:
    https://addons.mozilla.org/zh-TW/firefox/addon/12324
.. _https://netbank.esunbank.com.tw/webatm/:
    https://netbank.esunbank.com.tw/webatm/
.. _* 註1: 男子漢不空口說白話。: http://3.bp.blogspot.com/_eKM9lHjTZjs/SmAUk7RliOI/A
    AAAAAAAB9g/Vql1EYjnXu8/s1600-h/Screenshot.png
.. _* 註1: 男子漢不空口說白話。: http://3.bp.blogspot.com/_eKM9lHjTZjs/Sm7he0q_QJI/A
    AAAAAAAB90/-lK7mBLGd_c/s1600-h/Screenshot-1.png


.. author:: default
.. categories:: chinese
.. tags:: e-sun bank, linux, windows, ubuntu
.. comments::
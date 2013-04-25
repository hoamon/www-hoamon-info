Ubuntu 6.06.1 + HUAWEI 3G 網卡 + 中華電信
================================================================================

不曉得之前作錯了什麼，讓 skype 無法通話。所以想要重灌我的 IBM notebook 。

趁著過年長假，我好好地整理一下 r51，其實也不算好好整理，嚴格地說：應該是隨便整理，\
因為我只備份3g網卡的 wvdial.conf 設定檔，其他的檔案，我並不需要備份，\
這得歸功 unix 的資料夾分類原則。整理後並花了1個小時把 Ubuntu os 重灌。

這一次的重灌，讓我對 Ubuntu 充滿了三分敬畏及三分害怕。

敬畏的是，我重灌完 Ubuntu 後，只作了三件事，就讓 r51 正常工作了。

1.  灌 gcin 及嘸蝦米字表
2.  把備份的 wvdial.conf 搬到 /etc 下
3.  設定 skype 下載點路徑，安裝 skype 軟體

害怕的是，重灌完後，我的 wifi 無線網卡是無法啟動的，我搞了很久，看了一些文件，\
但這麼看都不覺得是解決之道，因為我記得之前第一次安裝 Ubuntu 的時候，沒有這麼難的，\
不知道那裡出了問題。直到我更新了所有的軟體 patch 檔後，\
又重開了幾次機(因為已經放棄了，所以我在玩 Ubuntu linux 休眠、暫停功能)，結果我的無線網路就這樣子正常了。

好的讓人莫明奇妙，讓我沒有動力去找出問題在那，不像之前用的 fedora ，\
我總是可以找到問題點，並解決它。而這到底是幸還是不幸呢?

下面是我的 3G 網卡設定檔，檔名則為 /etc/wvdial.conf ，但請先安裝好 wvdial 軟體。

.. code-block:: plain

    [Dialer Defaults]
    Init1 = ATZ
    Init2 = ATQ0 V1 E1 S0=0 &C1 &D2
    Init3 = AT+CPIN="0000"
    Modem Type = Analog Modem
    Baud = 460800
    New PPPD = yes
    Modem = /dev/ttyUSB0
    ISDN = 0
    Phone = *99***1#
    Password = 0000
    Username = ................
    # 3g網卡上的S/N:我的是16位的英數字，
    [Dialer hangup]
    Modem = /dev/ttyUSB0
    Baud = 460800
    Init2 = ATZ
    ISDN = 0
    Modem Type = Analog Modem

啟動指令是：

.. code-blck:: bash

    # wvdial &

這樣就可以了。

.. author:: default
.. categories:: chinese
.. tags:: linux, chunghwa telecom, ibm, 3g, ubuntu, r51
.. comments::
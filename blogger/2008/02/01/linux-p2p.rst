在 linux NAT 上擋 p2p
================================================================================

使用 netfilter + ipp2p module。

安裝：


-   將 Makefile 中的 IPTABLES_SRC 變數設定成你放 iptables.h 的資料夾，該路徑下有
    include/iptables.h 。如果你沒有 iptables.h 的話，可上 netfilter 官方下載你所使用的 iptables
    版本的源始碼。
-   # make
-   複製 libipt_ipp2p.so 到 iptables 的 lib 資料夾 (通常是 /lib/iptables/ ，底下應該已有
    libipt_mac.so 檔案)
-   複製 ipt_ipp2p.ko 到你的 kernel modules 中的 netfilter 資料夾(我的是
    /lib/modules/2.6.17-1.2142_FC4/kernel/net/ipv4/netfilter/ )
-   # sudo depmod -a


下規則：
下面的規則是直接把所有的 p2p 封包擋下


-   # sudo iptables -A FORWARD -m ipp2p --ipp2p -j DROP


如果你要個別擋的話，請參照


-   # sudo iptables -m ipp2p --help



PS 此軟體可能無法擋下中小學教師常用的 FOXY 封包，因為這個 ipp2p module 是外國人寫的，而外國人不太用 FOXY ，但其他常見的
ed2k, bt 應該是沒問題，這點我會繼續觀察。

PS2 經實驗證明，它也可以擋下 Foxy 了。大家給它拍拍手。

.. author:: default
.. categories:: chinese
.. tags:: linux, ipatbles, p2p, ipp2p
.. comments::
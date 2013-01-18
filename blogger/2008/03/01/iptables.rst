用 iptables 來開防火牆的洞!
================================================================================

題目有點聳動，事實上，並沒有開洞，只是利用原來的洞作不同協定的事。

因為工作的關係，總是會幫別人代管主機，然而大公司有大公司的政策，所以代管主機通常只能露一個洞出來給大家用，也就是 80 port 。要用 ssh
管理主機時，得用 VPN 連線到公司的 VPN Gateway ，再作連線動作。

但目前我遇到的 VPN Gateway 有仲琦、思科兩家，我在 Linux 上實在找不到可用的 VPN client ，所以一直得用 VirtualBox
上的 XP 來作維護工作，這令人很不愉快。我只想打指令，卻得開個 GUI 來礙眼。

只是，答案早就在那了，我到昨天才撿起來。

/sbin/iptables -A PREROUTING -t nat -p tcp -s ${自己電腦的IP} --dport 80 -j DNAT
--to ${伺服器IP}:22

先利用 VPN 連線進到主機中，加入這條規則，之後你就可以不用再透過 VPN Gateway ，直接從 ${自己電腦的IP} 遠端連入了。

若是你想要使用 https 連線，一樣的道理，規則改成如下：

/sbin/iptables -A PREROUTING -t nat -p tcp -s ${自己電腦的IP} --dport 80 -j DNAT
--to ${伺服器IP}:443

只是這麼作只能用一個外部 IP 換得一個伺服器上的 Port 。

所以就把腦筋動到 netfilter-L7 模組上，正想大刀搞搞，結果看到官網上一句話：

"""Warning: Some users have reported kernel crashes when they using SMP with
l7-filter. (Some have also reported that their SMP systems run fine.) If you
have a multi-CPU machine, test carefully before putting it into production
with l7-filter."""

興致全減，因為我代管的主機都是雙核心，我可不想費這個風險。還是拿 ip 換 port 吧!

P.S. 測試過程中，有個插曲，本想利用 apache 的 R-Proxy 功能直接作 http => https 的工作，然後花了很多時間才發現
R-Proxy 只能作到 http => http 及 https => https ，而不能作 http => https 及 https =>
http 的工作。

.. author:: default
.. categories:: chinese
.. tags:: netfilter, linux, iptables
.. comments::
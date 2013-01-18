用 VirtualBox 讓 Windows Server 偷偷(背景執行)跑在 Linux Server 上
================================================================================

自從接觸到 VirtualBox 後，一直想要把它的 Guest OS 當成 Host OS 中的服務來使用，因為這樣子，我就可以在 Linux
Server 中再跑一個 Windows Server 。會這麼作的原因是要使用 MS Office API 來出 .doc 檔。

那麼該如何在 Linux Server 中，令它在一啟動時，即啟動 Windows Server Service 呢?其實很簡單，在你的
/etc/rc.local 中加入一行

VBoxVRDP -startvm WinXP &
#如果你的 WinXP 並不是建立在 root 帳號中，而是其他使用者的話，請使用下列命令
su - UserName -c "VBoxManage startvm 'WinXP' -type vrdp"

這樣就夠了， WinXP 是 Guest OS 的名稱。這種啟動方式，讓你不須要跑一個 X window 環境來秀出 Windows Server
的視窗，它會啟動在背景中，如果你有設定 Guest OS(WinXP) 可以遠端顯示的話，你可以在別台電腦以 rdp 連線來控制 Guest
OS(WinXP) 。

設定好了以背景方式啟動 Guest OS 後，再設定外部連線可以轉到 Guest OS port 。設定指令如下：

# VBoxManage setextradata "WinXP"
"VBoxInternal/Devices/pcnet/0/LUN#0/Config/http/Protocol" TCP

# VBoxManage setextradata "WinXP"
"VBoxInternal/Devices/pcnet/0/LUN#0/Config/http/GuestPort" 80

# VBoxManage setextradata "WinXP"
"VBoxInternal/Devices/pcnet/0/LUN#0/Config/http/HostPort" 8080

上述指令只須設定一次即可，設定後，請重新開啟 VirtualBox 軟體。這樣別人就可以從 http://x.x.x.x:8080/ 來瀏覽你的
Windows Server 的網頁伺服器了。

.. author:: default
.. categories:: chinese
.. tags:: linux, windows, virtualbox
.. comments::
在無 X window 下，在 Linux server 中安裝一個跑在 VirtualBox 上的 Windows XP
================================================================================

有時候，就是很無奈，得裝上一個自己不喜歡的東西來討人歡心，要不然生不出人家想要，且是一模一樣的封閉格式檔案。所以只好在 Linux Server 上裝個
VirtualBox 來跑 XP 。但問題是，它沒有 X window 耶，怎麼辦? 很簡單，照下面指令一樣畫個胡蘆就成了。

# 製作一個近 6g 的硬碟檔案(virtualbox用的vdi檔)
VBoxManage createvdi -filename GuestOSName.VDI -size 6000 -register
# 註冊你要使用的 WinXP 光碟檔
VBoxManage registerimage dvd /home/hoamon/WinXP.iso

# 創建一個虛擬機器，名稱是 GuestOSName
VBoxManage createvm -name GuestOSName -register
# 設定 GuestOSName 所用的記憶體為 768MB 、使用 dvd 、使用 nat 、
# 使用 GuestOSName.VDI 為 hda 硬碟、並在 3389 port 上使用「遠端桌面連線」來作控制虛擬機器、
# 在光碟機中放入 WinXP.iso
VBoxManage modifyvm GuestOSName -memory 768MB -acpi on -boot1 dvd -nic1 nat
-hda GuestOSName.VDI -vrdpport 3389 -dvd /home/hoamon/WinXP.iso

# 開啟虛擬機器，然後你就可以連入 XXX.YYY.ZZZ.WWW:3389 去安裝 Windows XP 了。
VBoxVRDP -startvm GuestOSName &

# 強制關機
VBoxManage controlvm GuestOSName poweroff

在這個過程中，有一個非常棒的設計，那就是這個遠端桌面連線並不是 Windows XP 的遠端桌面連線，它是 VirtualBox
所提供的遠端桌面連線，所以當我們一打開 GuestOSName 時，以 3389 連線進去是可以看到 BIOS 畫面，但此時 Windows 都還沒啟動。

因為是 VirtualBox 所提供的桌面連線，所以如果你的 Guest OS 裝的是 GNU/Linux 、 *BSD
之類的作業系統，一樣都是用遠端桌面連線來控制。

接下來若是要開放 Guest OS 連線請參照`用 VirtualBox 讓 Windows Server 偷偷(背景執行)跑在 Linux Server
上`_。

.. _用 VirtualBox 讓 Windows Server 偷偷(背景執行)跑在 Linux Server 上:
    http://hoamon.blogspot.com/2007/11/virtualbox-guest-os-host-os-linux.html


.. author:: default
.. categories:: chinese
.. tags:: linux, virtualbox, virtual machine
.. comments::
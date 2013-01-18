不重灌 R51 上的 Windows 了!
================================================================================

要`重灌 IBM R51，好累!`_所以想用另一個方法來解決。

最近有一項 Open Source 軟體很紅： `VirtualBox`_
虛擬軟體，它的目的就是讓你在一個作業系統上再安裝多個作業系統，這類型軟體的領導者曾經是 VMWare ，但漸漸地有其他商業的、自由的軟體追上來了。

大家都說 VirtualBox 的效率十分高，幾乎快等於直接執行 Guest OS(就是多灌的那個 OS) 了。

況且如果是用 Levono Recover CD 重灌的話，無助於我桌上型電腦的 Windows ，我的 CoreDuo2
也是要重灌的。然而如果我使用的是 VirtualBox 的安裝方式，那麼只要在 CoreDuo2 上安裝一次，就可以把那個安裝完成的 .vdi 檔複製到
R51 來，這樣可以省下一次 OS 、 Application 安裝時間，同時也是另一型式的 Ghost/Clone 。

於是爬了爬文，看看如何安裝使用，結果相當簡單， Ubuntu 的方法如下：

# sudo vim /etc/apt/source.list

加入 deb http://www.virtualbox.org/debian feisty non-free。

# sudo apt-get update
# sudo apt-get install virtualbox

會出現選單讓你選擇，挑預設值即可。

# sudo groupadd --gid 1111 usbfs
# sudo vim /etc/group

在 group 中的 vboxusers, usbfs 群組後面加入可以使用 virtualbox 的帳號，如：

usbfs:x:1111:hoamon

最後在 /etc/fstab 中加入 none /proc/bus/usb usbfs devgid=1111,devmode=664 0 0

這樣才可以在 Guest OS 中使用 usb 裝置。如果你還是有 usb 裝置的權限使用問題，請編輯
/etc/udev/rules.d/40-permissions.rules 檔案，把

SUBSYSTEM=="usb_device", MODE="0664"
改成
SUBSYSTEM=="usb_device", MODE="0666"

接著重開機一次。開機後請點選選單的「應用程式」->「系統工具」->「Innotek VirtualBox」，這樣就可以開始 Guest OS 的安裝。

所以我在 CoreDuo2 上安裝了一個 Windows Guest OS ，更新它的 Patch ，並設定好 WebATM 的各項要求，就把這個設定好的
WinXP.vdi copy 到 R51 上，什麼額外的動作都不需要，我的 R51 直接就可以開 IE 看我寫的網頁、線上報稅、使用 WebATM
了。而且速度真的與直接在 R51 上跑一個 Windows 差不多(甚至比較快，不過有可能是 Levono 的 XP
裝了一堆有得沒有得，造成的開機速慢，更何況這個 Win Guest OS 也才剛灌，這樣比不厚道)。

`VirtualBox`_ 真棒。


.. _重灌 IBM R51，好累!: http://hoamon.blogspot.com/2007/08/ibm-r51.html
.. _VirtualBox: http://www.virtualbox.org/


.. author:: default
.. categories:: chinese
.. tags:: open source, virtualbox, ibm, r51, virtual machine
.. comments::
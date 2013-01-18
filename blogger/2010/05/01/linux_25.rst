用隨身碟安裝 Linux
================================================================================

我的電腦有些是沒有光碟機的，事實上，光碟機的使用機率是愈來愈低，我曾有一台 Thinkpad 大半年沒開過光碟機，結果要用時，它卻發生讀片錯誤。

所以這次重新安裝 Ubuntu 10.04 時，我是採用隨身碟安裝的方式，而也因為 Open Source 工具愈來愈多、愈來愈方便下，我只使用了
usb-creator 程式，就將 ubuntu-10.04-alternate-amd64.iso 燒到 4G 隨身碟了，方法很簡單，先安裝 usb-
creator(# apt-get install usb-creator) ，然後在命令列裡執行 usb-creator-gtk 。選擇要安裝的 iso
檔，並抹除隨身碟內的資料，就可以「製作開機磁碟」了。




`.. image:: http://2.bp.blogspot.com/_eKM9lHjTZjs/S_sRkfCzsGI/AAAAAAAACio/ZbA
84eXlQGw/s400/Screenshot-%E8%A3%BD%E4%BD%9C%E9%96%8B%E6%A9%9F%E7%A3%81%E7%A2%
9F.png
`_




``_接下來，就是重新安裝機器了，首先要切換 BIOS 的開機選項，在技嘉的 BIOS 上，我只選了 usb-hdd 就可從隨身碟開機，然而華碩的
BIOS ，除了要將 boot 選項切到 remoted-device 外，還要調整 usb storage 的 Forced FDD
類型。調整後，就如往常一樣重灌 Ubuntu 了。




`.. image:: http://4.bp.blogspot.com/_eKM9lHjTZjs/S_sTJTflg-I/AAAAAAAACiw/BTH
FARFwPeQ/s400/P1060038.JPG
`_



.. _所以這次重新安裝 Ubuntu 10.04 時，我是採用隨身碟安裝的方式，而也因為 Open Source
    工具愈來愈多、愈來愈方便下，我只使用了 usb-creator 程式，就將 ubuntu-10.04-alternate-amd64.iso 燒到
    4G 隨身碟了，方法很簡單，先安裝 usb-creator(# apt-get install usb-creator) ，然後在命令列裡執行
    usb-creator-gtk 。選擇要安裝的 iso 檔，並抹除隨身碟內的資料，就可以「製作開機磁碟」了。: http://2.bp.blogs
    pot.com/_eKM9lHjTZjs/S_sRkfCzsGI/AAAAAAAACio/ZbA84eXlQGw/s1600/Screenshot
    -%E8%A3%BD%E4%BD%9C%E9%96%8B%E6%A9%9F%E7%A3%81%E7%A2%9F.png
.. _接下來，就是重新安裝機器了，首先要切換 BIOS 的開機選項，在技嘉的 BIOS 上，我只選了 usb-hdd
    就可從隨身碟開機，然而華碩的 BIOS ，除了要將 boot 選項切到 remoted-device 外，還要調整 usb storage 的
    Forced FDD 類型。調整後，就如往常一樣重灌 Ubuntu 了。: http://4.bp.blogspot.com/_eKM9lHjTZ
    js/S_sTJTflg-I/AAAAAAAACiw/BTHFARFwPeQ/s1600/P1060038.JPG


.. author:: default
.. categories:: chinese
.. tags:: linux, ubuntu
.. comments::
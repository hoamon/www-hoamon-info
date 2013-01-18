VirtualBox: 在命令列下，將 host os 中的 usb 設備指定給 guest os 使用
================================================================================

如果我們把 Windows 開在背景中執行，這時得用遠端桌面連線來控制它的。

但如果我們臨時想要為 Windows 加入一 usb 設備的話，該如何處理? 原本若依正常的使用方法，在 VirtualBox 程式中開出 Guest
OS 時，它在右下角視窗外會有添加 usb /光碟/硬碟…的按鈕，但在背景中執行時，這些按鈕則見不到了。

其實很簡單。首先查出你要添加的 usb 設備的 uuid 。

# VBoxManage list usbhost
UUID: aead9d43-12fb-4faa-8c83-8e810217210c
VendorId: 0x0ca6 (0CA6)
ProductId: 0x0010 (0010)
Revision: 0.5 (0005)
Manufacturer: CASTLES
Product: EZ100PU Smart Card Reader
Address: /proc/bus/usb/001/003
Current State: Captured

接下來，在指定的 guest os 中啟用它。
# VBoxManage controlvm {{YOUR_GUEST_OS_NAME}} usbattach aead9d43-12fb-4faa-
8c83-8e810217210c

你就會在 Windows 中，看到一 usb 設備被找到了。

而移除它的方法則是如下：
# VBoxManage controlvm {{YOUR_GUEST_OS_NAME}} usbdetach aead9d43-12fb-4faa-
8c83-8e810217210c

.. author:: default
.. categories:: chinese
.. tags:: linux, windows, virtualbox, virtual machine
.. comments::
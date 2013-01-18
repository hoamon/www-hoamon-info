高級 Subversion GUI: Eclipse
================================================================================

對滑鼠重度使用者來說，編寫 python 程式是需要一個稱手的 IDE 工具的，在這方面，我強烈建議使用 `Eclipse`_
，原因是跨平台、開源及外掛多，所以你可以用它來寫 java, PHP, perl, python, ruby...，缺點只有一個，要學會 java
才能幫它加特殊功能，還好你想得到的，多半有人作了。

但對不在乎滑鼠的使用者來說， Eclipse 是有點麻煩的，在編寫文字上，方便性就不如 VIM 了，快速移動、大區塊剪貼、尋找 re 字串、自動補齊(需
VIM 外掛)等，用 VIM 是十分容易作到的，像是你要打個 SuperviseCase.objects.all() ，你只要 Sup.obj.all()
這樣就夠了。

所以我並不常用 Eclipse 來開發程式，大部份是用它來 Demo 程式碼給學弟妹看，因為他們都是用這一套的。

但是 GUI 工具有一個好處，比較程式碼差異及看 svn log 時很方便，只要是使用 svn 時，會用到 less 指令的，都適合用 Eclipse +
subclipse 來作。雖然 subversion 也有其他 GUI 工具配合，但 Eclipse 牌子比較大，用戶也比較多。建議各位試試。




= 後記 =

現在我`改用 NetBeans `_了。

.. _Eclipse: http://www.eclipse.org/
.. _改用 NetBeans : http://hoamon.blogspot.com/2009/03/netbeans.html


.. author:: default
.. categories:: chinese
.. tags:: program, eclipse, subversion
.. comments::
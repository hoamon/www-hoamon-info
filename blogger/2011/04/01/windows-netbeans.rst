無法在 Windows 上的 NetBeans 作中文註解
================================================================================

為了讓 Python 程式能容易在團隊之間快速流動，我們要求大家在程式編碼上一律使用 utf8 。只要在程式檔的第一行宣告 #-*- coding:
utf8 -*- 以及使用 utf-8 編碼存檔即可。




不過，在 Windows 中執行時，因為它還活在 cp950 的時代，所以我們還要在 Python 主安裝目錄中的 Lib/site-
packages/sitecustomize.py 中加入




import sys

sys.setdefaultencoding('utf8')




這樣 python 程式在執行時，才不會遇到 UnicodeEncodeError (其實偶爾還是會遇到，原因是搞混了 Unicode 編碼及 UTF-8
編碼)。




而在使用 NetBeans 時，我們也會在 /etc/netbeans.conf 中設定 -J-Dfile.encoding=utf8 來讓
NetBeans 正常顯示程式中的 UTF-8 編碼中文字。




不過，在 mercurial commit 時，卻無法使用中文作註解。這時候，只要在 netbeans.conf 加入
-J-Dmercurial.encoding=utf8 即可。







.. author:: default
.. categories:: chinese
.. tags:: mercurial, python, windows
.. comments::
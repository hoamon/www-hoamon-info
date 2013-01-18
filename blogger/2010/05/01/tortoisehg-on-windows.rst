如何解決 TortoiseHG on Windows 上中文檔名的問題
================================================================================

因為 Windows 在紀錄檔案名稱時，`是用 UTF-16 ，而不是 UTF-8 作紀錄`_，所以如果在 Windows
中，加入一個「中文檔名(嚴格來說，是非 ascii 編碼的名稱)」的檔案，那麼這個檔案到了 Mac OS X, Linux 平台時，就無法使用了。




要解決這個問題，只要 Windows 使用者用 `fixutf8 extension`_ 先處理檔名即可。下載程式碼後，只要到
hgrc.d/Mercurial.rc 檔中，加入




[extensions]

fixutf8 = C:/fix-utf8/fixutf8.py




但使用這個外掛(16 (baf283ab9f92)版)會導致 TortoiseHG 無法作 commit 的動作，這 commit
問題，我找了很久，但實在沒辦法解決，只知道 TortoiseHG 將 commit message 以 cp950 送出，但 fixutf8 卻要求
message 要以 utf8 進入，但那裡的程式要修改，我就 de 不到了。




目前我只能回到 cmd.exe 底下，用 hg ci 來作提交動作。




而且，在使用 fixutf8 下，有可能會導致 merge 功能錯亂，這時候，就只得用 Linux/Mac OS X 來解決 merge 問題。

.. _是用 UTF-16 ，而不是 UTF-8 作紀錄: http://hg.io/stefanrusek/hg-
    fixutf8/src/tip/README
.. _fixutf8 extension: http://bitbucket.org/stefanrusek/hg-
    fixutf8/overview


.. author:: default
.. categories:: chinese
.. tags:: mercurial, linux, windows, mac
.. comments::
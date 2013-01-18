Eclipse + PyDev
================================================================================

一直以來，都是用 Vim 作編輯的：寫網頁、 Perl 、 Python 、 shell script 、設定檔…，但學弟妹們還不會用 Vim
就要求他們拿來寫 Python ，這有點為難。對很多人來說，「鍵盤」絕對是「沒有生產力」可言的。

那如果不用 Vim 的話，那麼我的第二選擇會是 Eclipse ，因為它是 open source ，是 IBM 拱的，可以跨平台，也適合拿來寫網頁、
Latex 、 Python 、 PHP ...。

寫了一份`簡單講義`_教他們如何在 Windows 上搞定 Eclipse + PyDev 。結果自己在 Ubuntu 平台上卻搞不定 Eclipse +
Subclipse ，問題是出在我使用 Gnu 的 Java Run Time ，而它在 ssl key 的部份會發生無法接受過長的 ssl
憑證，卡在這裡非常久，試著安裝 javahl 函式庫，但我不知道到那裡改設定( Eclipse
的選項實在太多了，雖然我現在終於知道要到那裡改了)，所以我放棄了 Gnu 的 jre ，改用 sun 出的 j2se sdk 。裝完後，在啟動
eclipse 前，先作如下設定

export JAVA_HOME=/usr/local/jdk1.6.0_01
export PATH=$JAVA_HOEE/jre:$JAVA_HOME/bin:$PATH
export CLASSPATH=$JAVA_HOME/lib

即可。

我打算給 Eclipse 一個機會，讓我在跑 Python 程式時能更有效率，編輯的部份當然還是得靠 VIM 了。

.. _簡單講義: http://down.hoamon.info/presentation/PythonDevUseEclipse.html


.. author:: default
.. categories:: chinese
.. tags:: java, eclipse, PyDev, subversion
.. comments::
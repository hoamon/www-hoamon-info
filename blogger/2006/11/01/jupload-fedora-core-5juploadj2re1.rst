LifeType的JUpload模組問題
================================================================================

`.. image:: http://bp2.blogger.com/_eKM9lHjTZjs/RdxdUXnbC_I/AAAAAAAAAAY/vWQUJ
3WnMHE/s200/resserver.jpg
`_`JUpload`_模組是為了使上傳檔案更便利所設定了，它用起來就像系統裡的「檔案管理員/檔案總管」程式，可以同時選定多個檔案上傳。

然而，我的個人電腦在昇級到Fedora Core 5後，這個JUpload模組失效了，原本一直以為是j2re的版本問題，所以一直在找1.4版的安裝程式，因
為java.com的程式已昇級到1.5了所以很難找，但找到後裝了卻會讓我的
firefox崩潰，於是改了方向，去下載新版的JUpload程式。但一樣是不行。十分不爽。

慢慢地在找問題的過程中，我知道了java程式的 log檔位置，也知道是錯在那裡了。原因在於我的電腦不允許java
applet去讀取我的檔案系統，這是權限的設定問題。所以我到了`javaworld討論區`_查了一下，權限該到那裡改，幸運地查到
java.policy檔案的設定方法。

在我的電腦裡，java.policy是在 /opt/jre1.5.0_06/lib/security 中，修改的方式是在這個檔案中的 grant
區塊裡加入：

permission java.io.FilePermission "", "read";

這樣即可。

當然，你要讓java applet能讀你系統中的任何檔案，你就要有心裡準備，準備什麼?別抓奇怪的java applet程式來玩，當心你的資料外洩。

最後，我的心情由「不爽」到「高興」。

.. _: http://bp2.blogger.com/_eKM9lHjTZjs/RdxdUXnbC_I/AAAAAAAAAAY/vWQUJ3W
    nMHE/s1600-h/resserver.jpg
.. _JUpload: http://www.jupload.biz/ (JUpload's website)
.. _javaworld討論區: http://www.javaworld.com.tw/ (javaworld討論區)


.. author:: default
.. categories:: chinese
.. tags:: java, lifetype, jupload
.. comments::
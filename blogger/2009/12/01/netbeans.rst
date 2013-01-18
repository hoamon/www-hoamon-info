我是個愚蠢的傢伙 --- NetBeans 用了快一年，才想到「自動補齊」是種選項
================================================================================

`.. image:: http://4.bp.blogspot.com/_eKM9lHjTZjs/SyxviHZpQMI/AAAAAAAACT4
/NOyu-HXt1zI/s400/Screenshot.png
`_
年初時，把我的常用編輯器 vim 改成 `NetBeans + jvi`_ 的工具以應付多專案、多檔案及多版本比對的混亂模式。

這混亂模式不是 vim 檔案編輯模式的錯，而是混亂工作流程造成的。如果只在一個資料夾、幾個簡單文件要編輯，我還是會用 vim 處理的。

在使用 NetBeans + jvi 的過程中，有一個現象一直困惱著我，那就是 NetBeans
會偵測我打入的字，並作文法檢查及自動完成函式名稱，這『自動化』的行為，理論上，應該會讓編輯者比較方便才是，但因為我用的是 jvi plugin
，所以我已習慣另一種自動補齊行為： Ctrl+p ，而且我往往不需要 NetBeans 幫我在打『點』時作自動補齊，因為我不需從 N
個函式名稱、屬性中挑出想要的，而是先輸入前幾個字，然後再用 Ctrl+p 來補齊。

這個自動化模式讓我寫程式碼的速度受到限制，但用久了也就習慣了，畢竟寫程式碼的瓶頸並不是文字輸入速度，而是思考速度。

今天我莫名其妙地想到，這個「自動補齊應該是一種選項」才是呀! NetBeans 怎麼會預設立場認為全天下的程式設計師都喜歡這個行為，一定不只有我是因為使用
jvi plugin 才不愛用 NetBeans 內建的自動補齊，也有別人就是不喜歡「自動補齊」才對呀!

於是，我翻了一下 Options ，在 [Editor] 中的 [Code Completion] 發現關閉這個行為的選項。天呀!
我用了快一年，才想到這件事。

「IDE必備自動補齊」的先入為主想法，讓我莫名其妙地忍受這個小問題將近一年。

.. _: http://4.bp.blogspot.com/_eKM9lHjTZjs/SyxviHZpQMI/AAAAAAAACT4/NOyu-
    HXt1zI/s1600-h/Screenshot.png
.. _NetBeans + jvi: http://hoamon.blogspot.com/2009/03/netbeans.html


.. author:: default
.. categories:: chinese
.. tags:: vim, netbeans
.. comments::
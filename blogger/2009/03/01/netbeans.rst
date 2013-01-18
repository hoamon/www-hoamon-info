為什麼我用 Netbeans + jvi 作網頁程式開發平台
================================================================================

這都怪 `NetBeans`_ 把 `Mercurial`_ 整合的太好了。

原本我都是用 `Gvim`_ 來寫 Web-base 程式的，事實上，我的 Gvim 也調校的不錯，有 File Tab 、 Class/Function
Navigator 、 Tab Complete ，而重要的是它還有 1G, G, yy, dd, cw, <ctrl>+f, <ctrl>+b, H,
M, L...等。
`.. image:: http://4.bp.blogspot.com/_eKM9lHjTZjs/SayMNHh5ZSI/AAAAAAAABzQ/oAO
9j46wAQY/s400/vim.png
`_
不過，當我要比對修改後的程式時，單純只用 hg diff|colordiff|less 就顯得有點薄弱了。
`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/SayMTCTcktI/AAAAAAAABzY/SK7
mwwmtMwU/s400/netbeans.png
`_
而這時，我發現 NetBeans 編輯器可以整合 vi key-binding ，天呀! 這是多麼棒的一件事，之前我在試用 Eclipse 時，就覺得它的
vi key-binding 效果不是很好用，而且還要花錢買，讓我打消了轉換平台的欲望，但這個 NetBeans + vi
的功能就實實在在地滿足了我的需求。

















`.. image:: http://2.bp.blogspot.com/_eKM9lHjTZjs/SayMY2yIe1I/AAAAAAAABzg/SCh
A9ImLtIw/s400/netbeans2.png
`_
更棒的是， NetBeans 整合版本控制的功能比 Eclipse 好。在 Eclipse 中，所謂的版本控制只不過是把我在 shell
裡用的指令，放進它的 menu 中而已。但 NetBeans 卻可以讓你在 Editor 中，實際看到程式差異並選擇回復。而在設定方面， Eclipse
的 menu/option/perspective 實在太多了, 常常讓我搞不懂，這玩意到底要到那去找。

令人驚奇的是 NetBeans 還結合了 jdbc 的功能讓我可以把它當作是 Mysql/PostgreSQL 客戶端介面使用。這也一併讓我省了設定
phpMyAdmin 的功夫。 NetBeans 真的作到了 One Stop Shopping 。

在安裝上， NetBeans 6.5 也比 Eclipse 3.X 來得簡單， Python, Mercurial 它已內建，我只去了
http://jvi.sourceforge.net/ 下載 vi plugin 。況且，之前我在安裝 Eclipse
時，有些機器會遇到裝不起來的情況，這也讓我頭痛呀~ 害我先將安裝成功好的 Eclise 打包起來，然後看誰需要，就整個給他。

只是使用 NetBeans 我得付出一個代價， NetBeans Editor 的反應略比 Gvim
慢一點，雖不致造成我的困惱，但就是感覺得到(`誤，已補正`_)。我想這也是沒辦法地，因為 NetBeans/Eclipse 之類的 IDE
平台還得即時看你輸入的單字去找它相關的說明，以及檢驗文法是否錯誤。

`.. image:: http://2.bp.blogspot.com/_eKM9lHjTZjs/Syxw1p8J7wI/AAAAAAAACUI/cR4
DgJpH02E/s400/Screenshot-1.png
`_

.. _NetBeans: http://www.blogger.com/www.netbeans.org
.. _Mercurial: http://www.blogger.com/www.selenic.com/mercurial/
.. _Gvim: http://www.blogger.com/www.vim.org
.. _+b, H, M, L...等。: http://4.bp.blogspot.com/_eKM9lHjTZjs/SayMNHh5ZSI/A
    AAAAAAABzQ/oAO9j46wAQY/s1600-h/vim.png
.. _不過，當我要比對修改後的程式時，單純只用 hg diff|colordiff|less 就顯得有點薄弱了。: http://3.bp.bl
    ogspot.com/_eKM9lHjTZjs/SayMTCTcktI/AAAAAAAABzY/SK7mwwmtMwU/s1600-h/netbe
    ans.png
.. _而這時，我發現 NetBeans 編輯器可以整合 vi key-binding ，天呀! 這是多麼棒的一件事，之前我在試用 Eclipse
    時，就覺得它的 vi key-binding 效果不是很好用，而且還要花錢買，讓我打消了轉換平台的欲望，但這個 NetBeans + vi
    的功能就實實在在地滿足了我的需求。: http://2.bp.blogspot.com/_eKM9lHjTZjs/SayMY2yIe1I/AAAA
    AAAABzg/SChA9ImLtIw/s1600-h/netbeans2.png
.. _誤，已補正: http://hoamon.blogspot.com/2009/12/netbeans.html
.. _)。我想這也是沒辦法地，因為 NetBeans/Eclipse 之類的 IDE
    平台還得即時看你輸入的單字去找它相關的說明，以及檢驗文法是否錯誤。: http://2.bp.blogspot.com/_eKM9lHjTZjs/
    Syxw1p8J7wI/AAAAAAAACUI/cR4DgJpH02E/s1600-h/Screenshot-1.png


Old Comments in Blogger
--------------------------------------------------------------------------------



`c9s <http://www.blogger.com/profile/05514217676033260267>`_ at 2009-03-15T12:13:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

其實長輩你要用 diff 的話，vim 提供了 vimdiff 以及 gvimdiff (圖形介面) 倒是一個可用的方案。

gvimdiff file1 file2

可以簡單使用 o (obtain) , p (put)
並利用 C-w l|h 切換視窗。

另外也可直接從 vim command-line 下:
:diffsplit [filename]

以及
:diffthis

vertical vimdiff:
To make these commands use a vertical split, prepend |:vertical|. Examples: >

:vert diffsplit main.c~
:vert diffpatch /tmp/diff

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2009-03-15T14:46:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

to c9s:
不過，我不只是要用 vim 比較檔案，還要能夠結合 mercurial 作同一檔案的版本比較。這部份， vim 有方便的解法嗎?

`c9s <http://www.blogger.com/profile/05514217676033260267>`_ at 2009-03-15T15:12:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

mercurial 我沒有研究過。
不過我想應該是要透過 mercurial 設定 external diff program 來呼叫 vimdiff. :-)

下面幾篇我找到的不知道對你有沒有幫助。
http://grml.org/mercurial/
http://stackoverflow.com/questions/399606/mercurial-no-editor-appears-when-
merge-conflicts-are-detected

這篇就有講到 diff 的相關設定了。但要直接呼叫的話可能需要寫一個 wrapper script.
http://naleid.com/blog/2008/11/25/my-mercurial-setup-plus-some-useful-shims-
and-jigs/

.. author:: default
.. categories:: chinese
.. tags:: mercurial, vim, eclipse, netbeans
.. comments::
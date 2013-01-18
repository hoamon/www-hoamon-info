另一種Latex套件：TexLive2007
================================================================================

發現另一種似乎比 cjk-latex 好用的 tex 套件。它也可以處理 utf8
的文件，且據說它嵌入字形檔的方式是比較好的(原諒我，我還不太懂 tex)，另外安裝也比較方便。

請 tex mirror 站下載 live-CD (
`http://ctan.cdpa.nsysu.edu.tw/systems/texlive/Images/`_ )。

將 images 檔掛載到你想要的目錄如 /mnt/iso

$ sudo mount -t iso9660 -o loop /path/xxx.iso /mnt/iso
$ cd /mnt/iso
$ sh install-tl.sh
$ [按下d，以選擇安裝路徑]
$ [按下1，選擇 /usr/local/texlive，如果你沒有系統管理員的權限，就選擇你可以寫入的目錄]
$ [按兩次r離開]

這樣子，你就可以部份安裝好 texlive 了。為什麼是部份安裝呢!因為這樣的安裝方式，在你移除了 /path/xxx.iso
後，就無法使用了。但這種方式對我來說無所謂，因為我的 /path/xxx.iso
就放在硬碟裡，不會不見的。這樣只有一個缺點：比較浪費硬碟空間。

接下來我們要設定系統環境。下面是 texlive 可以運行的環境：

alpha-linux HP Alpha GNU/Linux
hppa-hpux HPPA HP-UX
i386-darwin x86 Mac OS X
i386-freebsd x86 FreeBSD
i386-linux x86 GNU/Linux
i386-openbsd x86 OpenBSD
i386-solaris x86 Solaris
mips-irix SGI IRIX
powerpc-aix IBM RS/6000 AIX
powerpc-darwin PowerPC Mac OS X
powerpc-linux PowerPC GNU/Linux
sparc-linux Sun Sparc GNU/Linux
sparc-solaris Sun Sparc Solaris
win32 Windows (32-bit)
x86_64-linux x86 64-bit GNU/Linux

我的是 i386-linux ，所以要在 ~/.bashrc 中設定：

PATH=/mnt/iso/bin/i386-linux:$PATH; export PATH
TEXMFSYSVAR=/usr/local/texlive/2007/texmf-var; export TEXMFSYSVAR

就這樣完成了。

下面是測試範例：

::
    ** 1**  **\documentclass****[****12pt****]{****book****}**
    ** 2**  **\usepackage****{****CJKutf8****}**
    ** 3**  **\begin{document}**
    ** 4**  **\begin****{****CJK****}{**UTF8**}{**bsmi**}**
    ** 5**  **\tableofcontents**
    ** 6**  **\chapter****{**here**}**
    ** 7**  本常問問答集~(FAQ list)~是從一些經常被問到的問題及其適當的解答中，以
    ** 8**  方便的形式摘要而出的。跟上一版不同的是，其編排結構已徹底改變。
    ** 9**  **\textbf****{**有關新結構的細節，可參考「如何閱讀本問答集及了解其編排結構」
    **10**  該項中的說明。**}**
    **11**  **\chapter****{**CJK 巨集套件**}**
    **12**  這是一個測試，關於CJK package 的測試。**\LaTeX**
    **13**  **\chapter****{**桃花源記節錄**}**
    **14**  初狹，纔通人；復行數十步，豁然開朗。土地平曠，屋舍儼然。有良田、美池、**%**
    **15**  桑、竹之屬，阡陌交通，雞犬相聞。其中往來種作，男女衣著，悉如外人；黃髮、**%**
    **16**  垂髫， 並怡然自樂。見漁人，乃大驚，問所從來；具答之，便要還家，設酒、殺雞、**%**
    **17**  作食。村中聞有此人，咸來問訊。自云：「先世避秦時亂，率妻子邑人來此絕境，**%**
    **18**  不復出焉；遂與外人閒隔。」問今是何世；乃不知有漢，無論魏、晉。此人一一**%**
    **19**  為具言所聞，皆歎惋。餘人各復延至其家，皆出酒食。停數日，辭去。此中人語**%**
    **20**  云：「不足為外人道也。」
    **21**  **\end****{****CJK****}**
    **22**  **\end{document}**
    經 pdflatex 後的`成果`_。如果你使用上面的範例來跑 pdflatex 時，你會發現編譯時有錯誤訊息。這是 pdflatex
    還無法正確處理中文目錄(應該是 bug )，所以你只要手動修改 xxx.toc 檔，換上正確的中文即可編譯了。

.. _http://ctan.cdpa.nsysu.edu.tw/systems/texlive/Images/:
    http://ctan.cdpa.nsysu.edu.tw/systems/texlive/Images/
.. _成果: http://down.hoamon.info/texlive_utf8.pdf


Old Comments in Blogger
--------------------------------------------------------------------------------



`Cris <http://www.blogger.com/profile/06540595948394037530>`_ at 2007-07-19T20:02:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

請問有沒有texlive的相關教學或說明？小弟是windows XP 32bit

`xiang <http://www.blogger.com/profile/15320285482872160538>`_ at 2007-12-06T21:18:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

> 這是 pdflatex 還無法正確處理中文目錄(應該是 bug )

在\end{CJK}前面加上\newpage，可能可以解決問題。
我不知道原因，但是我自己這么做確實可以讓pdflatex正確顯示中文目錄和其它各種需要顯示中文的操作。

try it.

.. author:: default
.. categories:: chinese
.. tags:: latex
.. comments::
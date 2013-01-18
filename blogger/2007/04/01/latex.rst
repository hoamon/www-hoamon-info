終於裝了Latex
================================================================================

從我學 Linux 開始，看到許多教學文件不是用 Docbook 就是用 LaTeX 排版的，
一直很心動，想學好 LaTeX 語法，然後把我的文章、論文、報告…全部轉成 tex 格式的。

唸(想念)了很久，也買了 cwTex 的書，但一直沒有真正花時間來學。直到現在，要唸博班了，
一定得寫很多報告，還是早學早超生。

學之前，總要把 LaTeX 裝起來吧!要不然怎麼實作呢!這就是痛苦的開始…

一般來說，各家的 Linux 套件都會附 LaTeX 程式給你，只是這些程式不支援 utf8 中/日/韓文。
因為要讓 latex 支援中文，並不是直接 hack tex 及 LaTeX 的核心，都是以外掛套件的方式處理的。
所以你得要處理外掛套件及字形檔的問題。

參考很多網頁文件及 MyCJK.pdf ，事實上，還是沒搞清楚 cjk-latex 如何安裝。
所以我是用 debian 的 .deb 檔來作安裝的。請到 debian 的 testing 套件檔下載如下檔案：

cjk-latex_4.7.0+cvs20061019-2_all.deb
latex-cjk-chinese_4.7.0+cvs20061019-2_i386.deb
latex-cjk-chinese-arphic-bkai00mp_1.15_all.deb
latex-cjk-chinese-arphic-bsmi00lp_1.15_all.deb
latex-cjk-chinese-arphic-gbsn00lp_1.15_all.deb
latex-cjk-chinese-arphic-gkai00mp_1.15_all.deb
latex-cjk-common_4.7.0+cvs20061019-2_i386.deb
latex-cjk-japanese_4.7.0+cvs20061019-2_i386.deb
latex-cjk-japanese-wadalab_0.20050817-11_all.deb
latex-cjk-korean_4.7.0+cvs20061019-2_all.deb
latex-cjk-thai_4.7.0+cvs20061019-2_all.deb
tex-common_1.0.1_all.deb

然後在 ubuntu 中下：

$ sudo dpkg -i *deb

這樣就裝好了。測試範例如下：
::** 1**  **\documentclass****[****12pt****]{****report****}**
    ** 2**  **\usepackage****[****T1****]****{****fontenc****}**
    ** 3**  **\usepackage****{****CJKutf8****}**
    ** 4**  **\usepackage****[****USenglish****]****{****babel****}**
    ** 5**  **\usepackage****{****CJKulem****}**
    ** 6**  **\newenvironment****{**TChinese**}{**%
    ** 7**  **\CJKfamily****{**bkai**}**%
    ** 8**  **\CJKtilde**
    ** 9**  **\CJKnospace****}{}**
    **10**  **\begin{document}**
    **11**  **\begin****{****CJK****}{**UTF8**}{}**
    **12**  **\begin****{****TChinese****}**
    **13**  **\chapter****{**here**}**
    **14**  本常問問答集~(FAQ list)~是從一些經常被問到的問題及其適當的解答中，以
    **15**  方便的形式摘要而出的。**\uline****{**跟上一版不同的是，其編排結構已徹底改變。**}**
    **16**  **\textbf****{**有關新結構的細節，可參考「如何閱讀本問答集及了解其編排結構」
    **17**  該項中的說明。**}**
    **18**  **\chapter****{**CJK 巨集套件**}**
    **19**  這是一個測試，關於CJK package 的測試。**\LaTeX**
    **20**  **\chapter****{**桃花源記節錄**}**
    **21**  初狹，纔通人；復行數十步，豁然開朗。土地平曠，屋舍儼然。有良田、美池、**%**
    **22**  桑、竹之屬，阡陌交通，雞犬相聞。其中往來種作，男女衣著，悉如外人；黃髮、**%**
    **23**  垂髫， 並怡然自樂。見漁人，乃大驚，問所從來；具答之，便要 還家，設酒、殺雞、**%**
    **24**  作食。村中聞有此人，咸來問訊。自云：「先世避秦時亂，率妻子邑人來此絕境，**%**
    **25**  不復出焉；遂與外人閒隔。」問今是何世；乃不知有漢，無論魏、晉。此人一一**%**
    **26**  為具言所聞，皆歎惋。餘人各復延至其家，皆出酒食。停數日，辭去。此中人語**%**
    **27**  云：「不足為外人道也。」
    **28**  **\end****{****TChinese****}**
    **29**  **\end****{****CJK****}**
    **30**  **\end{document}**

經 pdflatex 編譯後的 `pdf 文件`_

嘿~開始認真學 Latex 了。

.. _pdf 文件: http://down.hoamon.info/utf8.pdf


.. author:: default
.. categories:: chinese
.. tags:: latex, linux, debian, ubuntu
.. comments::
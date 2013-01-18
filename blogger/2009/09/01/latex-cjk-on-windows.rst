Latex CJK on Windows
================================================================================

我都是使用 rst 格式作為日常書寫格式，因為很方便地讓我作版本控制。所以網頁程式開發的功能/技術規格書也是用 rst 來編輯的。

但有個問題，當我想作圖文合併時，我可以在 ubuntu 中，使用 rst2latex, latex, dvipdfmx 等工具來轉成 pdf 檔，如果是在
Windows 下呢? 我的那些學弟們多半還是在 Windows 下工作，為了他們著想，我寫了這篇文章。

首先，一樣使用 rst2latex 程式(這是 `python-docutils`_ 提供的)，把 rst 檔轉成 .tex 檔 * ，然後再利用
latex.exe 生出 .dvi 文件，最後再利用 dvipdfmx.exe 把 dvi 轉成 pdf 檔。指令如下：

C:\> "C:\Program Files\MiKTeX 2.7\miktex\bin\latex.exe" xxx.tex
C:\> "C:\Program Files\MiKTeX 2.7\miktex\bin\dvipdfmx.exe" xxx

所以在 Windows 中，生成 pdf 檔也不是件難事。

那麼我們如何讓 Windows 可以有 latex.exe 及 dvipdfmx.exe 的指令呢! 很簡單，安裝 `Basic MiKTex.exe`_
及`相關字型檔`_即可。

Basic MiKTex.exe 的安裝方式就是下一步、下一步。待安裝好後，請開啟 MiKTeX > Settings ，並在 Roots
中新增「相關字型檔」的資料夾位置(看你將解壓縮後的資料夾放在那裡，我是放在 C:\texmf)。接下來在命令列中打入指令：

C:\> ``initexmf -u``
C:\> ``initexmf --edit-config-file updmap``
這時候會出現純文字編輯器，請把以下紫色內容複製貼上，再存檔關閉。
``Map cwmu.map
Map cwku.map
Map cwfsu.map
Map cwhbu.map
Map cwyu.map``````
C:\> ``initexmf --mkmaps``

這樣你就可以使用 latex.exe 及 dvipdfmx.exe 來生成 pdf 檔了 **。

詳細步驟可參考政大應數蔡炎龍老師的`教學文件(本站備份)`_。



-   註1 rst 及 tex 檔其實都只是純文字檔，只是它們的內文用不同的結構化標籤作格式排版。
-   註2 Windows 下使用的字型檔，其字型名稱為 cwmu, cwku, cwfsu, cwhbu, cwyu ，所以原本我們在 tex
    中，所寫的 \begin{CJK}{UTF8}{kai} 要改成 \begin{CJK}{UTF8}{cwku} 。

.. _python-docutils: http://docutils.sourceforge.net/
.. _Basic MiKTex.exe: http://miktex.org/
.. _相關字型檔: http://riemann.math.nccu.edu.tw/%7Eyenlung/file/texmf.zip
.. _教學文件(本站備份): http://www.hoamon.info/_d/latex_in_Windows.pdf


.. author:: default
.. categories:: chinese
.. tags:: latex, windows, ubuntu
.. comments::
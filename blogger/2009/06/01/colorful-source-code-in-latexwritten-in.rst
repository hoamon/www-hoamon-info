colorful source code in Latex(written in reStructed Text)
================================================================================

之前提到使用 Vim 的 `plugin VST`_ 來撰寫可自動轉換 latex 格式的簡單結構文章。VST 相當容易使用，不過在轉換程式碼到 pdf
格式時，它無法使用類似 2html 的技巧來讓程式碼變色。

所以我參考了 `Listings Package`_ 的語法，稍為修改了 VST 的程式碼(其實只是加上幾個宣告而已)。
::** 1 ****diff -r 56c0141f8add Configure/vim/plugin/vst-x.vim**
    ** 2 ****--- a/Configure/vim/plugin/vst-x.vim    Tue Jun 02 00:12:23
    2009 +0800**
    ** 3 ****+++ b/Configure/vim/plugin/vst-x.vim    Tue Jun 02 00:14:07
    2009 +0800**
    ** 4 ****@@ -4541,6 +4541,18 @@**
    ** 5 **                        \.'\usepackage{longtable}'."\n"
    ** 6 **                        \.'\usepackage{tabularx}'."\n"
    ** 7 **                        \.'\usepackage{amsmath}'."\n"
    ** 8 ****+            \.'\usepackage{color}'."\n"**
    ** 9 ****+            \.'\usepackage{listings}'."\n"**
    **10 ****+
    \.'\definecolor{Brown}{cmyk}{0,0.81,1,0.60}'."\n"**
    **11 ****+
    \.'\definecolor{OliveGreen}{cmyk}{0.64,0,0.95,0.40}'."\n"**
    **12 ****+
    \.'\definecolor{CadetBlue}{cmyk}{0.62,0.57,0.23,0}'."\n"**
    **13 ****+
    \.'\lstloadlanguages{Python,PHP,Ruby,Bash,Perl}'."\n"**
    **14 ****+            \.'\lstset{language=Python,frame=ltrb,framesep=
    5pt,basicstyle=\normalsize,'."\n"**
    **15 ****+            \.'
    keywordstyle=\ttfamily\color{OliveGreen},'."\n"**
    **16 ****+            \.'
    identifierstyle=\ttfamily\color{CadetBlue}\bfseries,'."\n"**
    **17 ****+            \.' commentstyle=\color{Brown},numbers=left,bac
    kgroundcolor=\color{white},'."\n"**
    **18 ****+            \.'
    stringstyle=\ttfamily,escapeinside=``,identifierstyle=}'."\n"**
    **19 ****+            \."\n"**
    **20 **                        \.countrysettings."\n"
    **21 **                        \.'\renewcommand\CJKglue{\hskip -0.3pt
    plus 0.08\baselineskip}'."\n"
    **22 **                        \.'\linespread{1.382}'."\n"
這樣就可以在 vim 中撰寫如下語法，來讓程式碼在 pdf 中變色了：
::
    .. raw:: latex

        \begin{lstlisting}
    import sys
    print sys.getdefaultencoding()
    sys.path.append(".")
    sys.path.append("/home/hoamon/`桌面`")
    from hashlib import md5
    from random import random
    for i in xrange(10): print md5(str(i+random())).hexdigest()
    def whatever(x): print x + 3
    whatever(10) # 13
    #`中文要作跳脫，使用符號為[數字鍵1]左邊的那一個 \\``
        \end{lstlisting}

    .. raw:: latex

        \lstinputlisting{xxx.py}


下圖就是成果啦：
`.. image:: http://2.bp.blogspot.com/_eKM9lHjTZjs/SiQOA-
KYQcI/AAAAAAAAB4Y/F3TQLTXMB0I/s400/Screenshot.png
`_
沒有網頁格式的那樣多采多姿，但聊勝於無呀!

.. _plugin VST: http://cle.linux.org.tw/~edt1023/vim/vst/index.html
.. _Listings Package:
    http://dante.ctan.org/CTAN/macros/latex/contrib/listings/
.. _下圖就是成果啦：: http://2.bp.blogspot.com/_eKM9lHjTZjs/SiQOA-
    KYQcI/AAAAAAAAB4Y/F3TQLTXMB0I/s1600-h/Screenshot.png


.. author:: default
.. categories:: chinese
.. tags:: latex, vim, restructured text, vst
.. comments::
Pygments:程式碼變色的另一種方法
================================================================================

如果你喜歡 Python 多於 VIM 的話，那麼你還有 `Pygments`_ 可以用。感謝 `Tib`_ 提供的 `style`_ 檔。

首先請先安裝 pygments ，請用

# sudo easy_install Pygments-0.7.1-py2.4.egg

這樣你就多了一個 pygmentize 指令了。如果你想要把 pymail.py 變顏色，請下

# pygmentize -f html -O encoding=utf-8,linenos=1 -l python -o pymail.html
pymail.py

所得到的 pymail.html 檔則是把 pymail.py 程式碼中的關鍵字作分類的動作，這樣還沒有上顏色喔~要上顏色的作法則是

# pygmentize -f html -S colorful -a div.highlight

這樣則會產生一個 css 語法的程式碼。如果你不喜歡 colorful ，你可以看看你的
/yourpath/Pygments-0.7.1-py2.4.egg/pygments/styles 資料夾下有那些 .py
，這些都可以用。如果還是不喜歡的話，可以參考一下 tib 的 style 檔，把它放到 /yourpath/Pygments-
0.7.1-py2.4.egg/pygments/styles 下，檔名則要命名為「 Class Name 去掉 Style
後全部小寫的英文字」。這樣你就可以用

# pygmentize -f html -S defaultsbt -a div.highlight


:: 1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27

::#!/usr/bin/python
    import smtplib

    def mkmail(toaddr, name, pwk, history):
        fromaddr = 'powerkey@cams.wra.gov.tw'
        subject  = 'PowerKey of CAMS'
        # Add the From: and To: headers at the start!
        msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n"
               % (fromaddr, toaddr, subject))
        msg += """**本信 由系統自動發送，請勿回覆本信**
    =====================================

    %s 先生/小姐：
    感謝你的使用。密碼如下方連結：
    http://www/PowerKey/showkey.html?powerkey=%s

    密碼信寄送的歷史紀錄：
    %s
    """ % (name[0:3], pwk, history)

        server = smtplib.SMTP('localhost')
        server.set_debuglevel(0)
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()

    mkmail('hoamon@hoamon.info', '何岳峰', '11e4', 'history')





.. _Pygments: http://pygments.org/
.. _Tib: http://sbt.idv.tw/
.. _style: http://sbt.idv.tw/temp/default-sbt.txt


.. author:: default
.. categories:: chinese
.. tags:: vim, python, pygments
.. comments::
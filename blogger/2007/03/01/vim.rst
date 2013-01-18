可怕的 VIM
================================================================================

每次在 blogger 上發表帶有程式碼的文章時，都感到十分麻煩。自己要作 space 轉 dash 的動作，還有變顏色。

但沒想到 VIM 就有一個指令可以讓文章變成網頁格式。

請把你編輯的文章調成你想要發佈的樣子，如行號顯示、顏色區別等，然後用 :TOhtml 指令即可。

下面就是一個 Python 程式碼轉出來的網頁結果：

::** 1 ****#!/usr/bin/python**
    ** 2 ****# -*- coding: utf-8 -*-**
    ** 3 ****import** smtplib
    ** 4 **
    ** 5 ****def** **mkmail**(toaddr, name, pwk, history):
    ** 6 **    fromaddr = **'****powerkey@test.com.tw****'**
    ** 7 **    subject  = **'****PowerKey****'**
    ** 8 **    **# Add the From: and To: headers at the start!**
    ** 9 **    msg = (**"****From: %s****\r\n****To:
    %s****\r\n****Subject: %s****\r\n****"**
    **10 **           % (fromaddr, toaddr, subject))
    **11 **    msg += **"""******本信由系統自動發送，請勿回覆本信****
    **12 ****=====================================**
    **13 **
    **14 ****%s 先生/小姐：**
    **15 ****感謝你的使用。密碼如下方連結：**
    **16 ****`http://www/PowerKey/showkey.html?powerkey=%s`_**
    **17 **
    **18 ****密碼信寄送的歷史紀錄：**
    **19 ****%s**
    **20 ****"""** % (name[0:3], pwk, history)
    **21 **
    **22 **    server = smtplib.SMTP(**'****localhost****'**)
    **23 **    server.set_debuglevel(0)
    **24 **    server.sendmail(fromaddr, toaddr, msg)
    **25 **    server.quit()
    **26 **
    **27 **mkmail(**'****homon%2hoamoin.ino****'**, **'****何岳峰****'**,
    **'****11e4****'**, **'****history****'**)


.. _http://www/PowerKey/showkey.html?powerkey=%s:
    http://www/PowerKey/showkey.html?powerkey=%s


.. author:: default
.. categories:: chinese
.. tags:: vim, python
.. comments::
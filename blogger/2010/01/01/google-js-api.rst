使用 Google AJAX Libraries API  時，無法離線撰寫網頁程式?
================================================================================

在網頁程式中，我都是使用 Google AJAX Libraries API 來 host jquery
程式庫的，然而這麼作有一個缺點，如果你是在離線作程式設計時，要手動修改樣版，把 Google 來源的 js 檔改成從本機讀取，是有點麻煩，但致少作得到。




但若是將來在系統上線後，使用者上得了你寫的網頁系統，卻無法連至 www.google.com 呢?
那怎麼辦，雖然這個機率會滿低的，但也是有可能會發生在這個網頁系統屬公司內部系統，而對外連線卻被中斷的情況下。




別怕! 很簡單，下面就是一個範例，第 6、7、8 行改成本機 host 的檔即可。



::
    ** 1 ****<****link**** ****rel****=****"stylesheet"****
    ****title****=****"default"**** ****type****=****"text/css"****
    ****media****=****"screen"**** ****href****=****"`http://ajax.googleapis.
    com/ajax/libs/jqueryui/1.7.2/themes/smoothness/jquery-ui.css`_"****>****
    2 ****<****script**** ****type****=****"text/javascript"**** ****src****=
    ****"`http://www.google.com/jsapi`_"****>****</****script****>**
    ** 3 **
    ** 4 ****<****script**** ****type****=****"text/javascript"****>**
    ** 5 ****    ****if**** **(**typeof**** google ==
    ****'undefined'**)** ****{**
    ** 6 ****        ****document****.write**(**unescape**(**'%3Cscript
    src="/localmedia/jquery-1.4.min.js"
    type="text/javascript"%3E%3C/script%3E'**))**;**
    ** 7 ****        ****document****.write**(**unescape**(**'%3Cscript
    src="/localmedia/jquery-ui-1.7.2.custom.min.js"
    type="text/javascript"%3E%3C/script%3E'**))**;**
    ** 8 ****        ****document****.write**(**unescape**(**'%3Clink
    type="text/css" href="/localmedia/smoothness/jquery-ui-1.7.2.custom.css"
    /%3E'**))**;**
    ** 9 ****    ****}**** ****else**** ****{**
    **10 ****        google.load**(**"jquery"****, ****"1.4.0"**)**;**
    **11 ****        google.load**(**"jqueryui"****, ****"1.7.2"**)**;**
    **12 ****    ****}**
    **13 ****</****script****>**


延伸閱讀： `Using CDN Hosted jQuery with a Local Fall-back Copy`_

.. _http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/themes/smoothness
    /jquery-ui.css:
    http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/themes/smoothness
    /jquery-ui.css
.. _http://www.google.com/jsapi: http://www.google.com/jsapi
.. _Using CDN Hosted jQuery with a Local Fall-back Copy:
    http://weblogs.asp.net/jgalloway/archive/2010/01/21/using-cdn-hosted-
    jquery-with-a-local-fall-back-copy.aspx


.. author:: default
.. categories:: chinese
.. tags:: javascript, jquery, google
.. comments::
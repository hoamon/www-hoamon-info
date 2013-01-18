懂基本原理與不懂基本原理的差別
================================================================================

我在使用 Google AJAX Library api 時，遇到一個奇怪的問題：
::
    //第一段
    <script src="http://www.google.com/jsapi"></script>
    <script>
     google.load("jquery", "1.3.2");
     google.load("jqueryui", "1.7.2");
    </script>
    <script>
     var $p = $('<p>123</p>');
     alert($p.text()); // it works
    </script>

以上程式碼居然不等於下面的程式碼!
::
    //第二段
    <script src="http://www.google.com/jsapi"></script>
    <script>
     google.load("jquery", "1.3.2");
     google.load("jqueryui", "1.7.2");
     var $p = $('<p>123</p>'); //會發生「未定義 $ 」問題。
     alert($p.text());
    </script>

但第一段程式碼可換成下面程式碼
::
    //第三段
    <script src="http://www.google.com/jsapi"></script>
    <script>
     google.load("jquery", "1.3.2");
     google.load("jqueryui", "1.7.2");
     google.setOnLoadCallback(function() {
       var $p = $('<p>123</p>');
       alert($p.text()); // it works
     });
    </script>

也就是 js 引擎對 <script> 區塊的判讀有特殊行為存在，要不然就是 jsapi.js 程式有獨到之處，但因為我不懂 js 引擎也沒仔細去看
jsapi.js 程式碼，所以我只能 try and error ，慢慢兜。

.. author:: default
.. categories:: chinese
.. tags:: jquery, ajax, google
.. comments::
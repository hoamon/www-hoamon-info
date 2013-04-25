資料結構重於演算法
================================================================================

引言：「萬丈高樓平地起。」

曾有個程式宗師說：「只讓我了解你程式的演算法，我是無法得知你程式的資料結構。\
但讓我了解你的資料結構，我大概也知道了你的演算法。」\
這可說明了演算法是依附在資料結構上的。

選擇一個正確的資料結構比找到一個華麗的演算法來的重要。
來個例子看看：
一個原始的文字檔內容如下：

.. code-block:: bash

    [amon@amon amon]$ cat hash.tables
    AA,4E00
    AB,4E01
    AB,7500
    QQ,7500
    QP,4E00
    WWW,8888
    WXY,7500

請使用任一的程式語言將上述文字檔格式改成如下：

.. code-block:: plain

    7500 => AB,QQ,WXY,
    8888 => WWW,
    4E01 => AB,
    4E00 => AA,QP,

評份標準：以程式碼中的分號( ; )較少者，勝出。\
但如果你喜歡使用其他不以分號作為結束符號的語言，也可以，不過一個迴圈至少要算一行。\
想一想，你覺得該用多少行來完成這個題目。

上述的題目，我們可以了解原始檔案的內容是以"行"為單位，一行之中又可分成兩個部份。\
左邊是以 A-Z 所組成的單字，右邊是 16 進位的數字，它們的關係是屬於多對多的關係。\
而目標檔案的格式在一行當中則成了 16 進位數字對應一個包含多值的文字字串。\
它們的關係則是一對一或是一對多的關係。

目標檔案的格式不管是一對一或是一對多的關係，\
這都可以讓我們聯想到一種資料結構： key => value(我想我們都太好學了，\
所以只能聯想到資料結構，而不是一張 50 元的樂透會有多少期望值)

有趣的是，這種資料結構在 php、perl、python 中是垂手可得的，不用宣告，\
不用費心堆砌。而不同的是這種資料結構在三種語言中有不同的實作方法，\
也有不同的名字及特性。

| php: associative array(簡稱 aa or double a，要不然實在是太長，太難唸了)
| perl: hash(因為它是用 hash 演算法作最佳化的)
| python: dictionary(這個比較能形容 key => value 的名詞)

aa 的特性能容許多個相同的 key 對應不同的 value (我也不懂為什麼要這麼作，這麼作好像沒有什麼好處)。\
perl 的 hash 則是太重要了，重要到它有個特別的名字 % ，寫 perl 程式一定要好好地了解 hash 。\
而 python 的 dictionary 則多了例外處理(其實也不只有 dictionary 有，是整個 python 語言都有 exception)。

首先我們來看 php 程式該何解決這個問題。

.. code-block:: bash

    [amon@amon amon]$ cat -n aa.php
    01  <?
    02  $lines = file('./hash.tables');
    03  foreach($lines as $line){
    04   preg_match("/^([^,]+),([^,]+)\n/", $line, $match);
    05   $aa[$match[2]] .= "$match[1]," ;
    06  }
    07  foreach($aa as $k => $v){
    08   echo "$k => $v\n";
    09  }
    10  ?>
    [amon@amon amon]$ php aa.php
    4E00 => AA,QP,
    4E01 => AB,
    7500 => AB,QQ,WXY,
    8888 => WWW,

在line 2中讀取檔案， line 3~6 將字串切開並放入 $aa 中， \
line 4 使用了正規表示式將資料切開並放入$match中。 line 7~9 則把 $aa 列印出來。

接下來，我們來看看 python 如何解決。

.. code-block:: bash

    [amon@amon amon]$ cat -n dictionary.py
    1 from sys import stdin as s
    2 d = {}
    3 for l in s.readlines():d.setdefault(l[:-1].split(",")[1],
                                []).append(l[:-1].split(",")[0])
    4 for k in d.keys(): print k + " => " + ','.join(d[k]) + ','
    [amon@amon amon]$ python dictionary.py < hash.table
    7500 => AB,QQ,WXY,
    8888 => WWW,
    4E01 => AB,
    4E00 => AA,QP,

line 1 匯入了 sys 物件以使用讀取 STDIN 的方法，line 2 初始化 dic 變數為一個空的 dictionary \
( python 不用宣告變數，但是第一次使用時一定要給個初始值)， line 3 從 STDIN 讀入一行資料，\
將字串切割並置入 dic 中。 line 4 則是把 dic 給列印出來。

再來看看 perl 的程式。

.. code-block:: bash

    [amon@amon amon]$ cat -n hash.pl
    1  (($v, $k) = split /,/) and $hash{$k} .= "$v," while(chomp($_ = <>));
    2  print "$k => $v\n" while(($k, $v) = each %hash);
    [amon@IBM_amon ~]$ perl hash.pl hash.tables
    7500 => AB,QQ,WXY,
    8888 => WWW,
    4E01 => AB,
    4E00 => AA,QP,

是的，不要嚇一跳，它真的只有兩行。第一行作的工作挺多的，把資料去掉行尾的"\n"符號，\
再切成兩個部份，並放入 %hash 中。第二行就只是把 %hash 列印出來而已。而 hash.pl 也可以換成另一個版本。

.. code-block:: bash

    [amon@amon amon]$ cat -n hash.pl
    1  /([^,]+),([^,]+)/ and $hash{$2} .= "$1," while(chomp($_ = <>));
    2  print "$k => $v\n" while(($k, $v) = each %hash);

第一行的 split 函數，被換成了正規表示式，其餘的保持一樣。

上面的例子中， hash 及 dictionary 的結果是一樣的，\
因為它們都使用 hash 演算法來作資料結構的最佳化，而 aa 就沒有這種特徵，基本上，它的 key 值是先進先出的。

正確的資料結構，可以讓你的演算法精簡，讓其他人易讀，好處多多。

另外，大家也可以注意到，在資料的 i/o 上，利用系統上的 STDIN 也可以讓你的程式更精簡一點。\
不過，該不該用，還是在於你的 tradeoff (取捨)。

Old Comments in Blogger
--------------------------------------------------------------------------------

`micmic <http://www.blogger.com/profile/14469716380183411089>`_ at 2007-03-09T19:12:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    php 可改成

    .. code-block:: bash

        1  $lines = file('./hash.tables');
        2  foreach($lines as $line){
        3      list($k,$v)=explode(',',$line);
        4      $k_arr[trim($v)].=isset($k_arr[trim($v)])
                                ? "$k,":trim($v)."=>$k,";
        5  }
        6  echo implode("\n",$k_arr);

    少兩行

.. author:: default
.. categories:: chinese
.. tags:: python, algorithm, php, perl, data structure
.. comments::
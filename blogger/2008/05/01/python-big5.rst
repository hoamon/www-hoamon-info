Python 不支援 Big5 擴充字(誤)
================================================================================

"""README: 感謝使徒提姆，我居然天真地以為 Python 沒有作到 Localization 。下面第一段文是我在放屁，請見諒! 就把此文當作是
os.popen 的一段小範例吧! """

有 7 個 Big5 擴充字：碁, 銹, 裏, 墻, 恒, 粧, 嫺，無法透過 Python 的 unicode 函式作轉換。所以我只好呼叫外部
iconv 程式來作轉換。

一開始，我選用 os.system 來作轉換，但 os.system 的所得到的回傳值是 subshell 執行程式的狀態，而不是轉換後的 utf8
碼，後來就改用 os.popen 。

程式範例如下：
::try:
      value = unicode(str(v), 'big5')
    except:
      value = os.popen('echo "%s"|iconv -f big5 -t utf8 2>&1' %
      v.replace('`', "'").replace('\n', '')).read().replace('\n', '')
      if 'iconv: ' in value: value = unicode(str(v), 'big5', 'ignore')
    一開始先嘗試用 unicode 函式轉換，不成功後才使用 os.popen ，並將 stderr 的訊息轉到 stdout
    去，如果在得到的回傳值中發現了 iconv: 的字串，則再使用 unicode 函式作『錯誤 ignore 』的轉換。

這樣就能兼顧程式效率及轉換正確率了。

Old Comments in Blogger
--------------------------------------------------------------------------------



`AndCycle <http://www.blogger.com/profile/12331975295931012974>`_ at 2008-05-06T11:20:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

人家這裡有個純py的codec, 雖然很破, 但是可以用 :p
http://www.andcycle.idv.tw/~andcycle/work/BahaDump/lib/big5ext.py

`使徒提姆 !? <http://www.blogger.com/profile/07429567259240612236>`_ at 2008-05-06T11:47:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

python不是不支援,big5擴充字要用cp950. unicode(str(v), 'cp950')即可.

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2008-05-06T20:20:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

感謝使徒提姆的指正，謝謝。

.. author:: default
.. categories:: chinese
.. tags:: iconv, python
.. comments::
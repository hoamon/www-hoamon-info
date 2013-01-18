Trac + Mercurial on Apache 的亂碼問題
================================================================================

這個問題搞了我很久。

用 trac 內帶的 tracd 來跑， changelog 部份的中文就是正常的，但跑在 apache 上時，它就亂了，而且只亂 changelog
部份，程式碼的 diff 結果及 raw 格式都沒事。

看了很久的 mercurial-plugin-0.11 程式碼，看來看去覺得這應該是 mercurial 的錯，不過為什麼我在 shell
中用沒事，或是用 tracd 跑也沒問題，但它跑在 apache 上就錯了呢???

hg 在讀 changelog 的部份，它是用 mercurial.changelog.changelog 函式來處理，但裡面有一個 read() 被
mercurial-plugin 拿來用了，而這個 read 函式在解讀字串時，要叫用 util.tolocal() 來處理編碼，只要沒設定
os.environ['HGENCODING'] 的話，它就會預設為 ascii ，這就是造成 changelog 亂碼問題的地方。

以前，我只須在 /etc/python2.5/sitecustomize.py 設定 sys.setdefaultencoding('utf8')
就行了，現在還得加上 os.environ['HGENCODING'] = 'utf-8' 。

我還是不太懂 os 及 sys 的差別是什麼?

Old Comments in Blogger
--------------------------------------------------------------------------------



`Willie Wu <http://www.blogger.com/profile/11242009037751251792>`_ at 2009-01-22T00:43:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

請試試看設定 apache 設定檔：

SetEnv HGENCODING utf8

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2009-01-22T08:53:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我設

SetEnv HGENCODING utf8

或是

SetEnv HGENCODING UTF-8

都沒有用。謝謝。

.. author:: default
.. categories:: chinese
.. tags:: mercurial, trac, python, apache
.. comments::
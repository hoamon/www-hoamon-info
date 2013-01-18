莫非定律： 當你相信用不著時，它偏偏派上用場
================================================================================

上禮拜，我作了大掃除。清掉了堆在家裡一段時間的紙箱。結果，今天我的桌上型電腦開不了機了，需要箱子送回維修。

因為「桌上型電腦會壞掉」這件事，我想要把「HG」伺服器，全部丟給 `bitbucket.org`_ 管理。我的桌上型電腦只剩下三種功能： hg
server, zotera sync server, file backup 。

zotera sync server 用到的機會不多，因為我最近不常看文獻，而且它的使用頻率不高。而 file backup 是將代管的 web
system 的資料順便備一份到我家作異地備援，如果我沒開機，則會拖個幾天才作異地備份。

於是，最影響我工作效率的是「 hg server 」無法運作。雖然 hg
是分散式版本控制器，不用中央伺服器存在，也能正常工作。但少了中央伺服器，我的眾多電腦們就不方便傳送 changeset 了。

為此，我相信 bitbucket.org 的伺服器維護能力高於我，所以我要把全部儲存庫交給它們管理。而且 bitbucket.org
的託管方案很優惠，我們可以開設任意數量的 public 或 private 儲存庫，只要這些儲存庫的參與用戶不高於 5 位。超過 5
位才開始計價，詳可閱`此`_。

.. _bitbucket.org: http://bitbucket.org/
.. _此: https://bitbucket.org/plans


.. author:: default
.. categories:: chinese
.. tags:: bitbucket, zotera, hg
.. comments::
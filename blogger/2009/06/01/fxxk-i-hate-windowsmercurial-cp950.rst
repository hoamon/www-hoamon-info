FxxK! I hate Windows(Mercurial cp950 problem)
================================================================================

一個因為中文檔名，讓我必須在 Windows 下工作的專案 *。今天我多花了 2 個小時，只為了要送出 4.3 MB 的中文檔名資料夾。是什麼問題呢! 是
{urlopen 10053} ，但倒底它是個什麼問題，我還是搞不懂。我後來是把它的檔名改短一點，然後先 copy 至學校的其他 windows 後，再作
hg push ，這樣總算成功了。

PS 我有試過 hg-fixutf8 了。但它只會在 commit 及 update 時作 utf8 <=> cp950 的轉換。這樣我無法在
NetBeans 中工作。

.. author:: default
.. categories:: chinese
.. tags:: mercurial, windows
.. comments::
Mercurial 在開發「模組或函式庫」的應用策略
================================================================================

前幾天，學弟問了我一個問題，讓我發現原來我們對 branch
的概念還不是很熟悉。事實上，這是件好事，從問問題中，才能發現原來事情不是我們所想像的，早發現早好。最痛苦的是在弄亂運作中的程式碼後才驚醒。

在說明學弟的問題前，要先來前情提要。我們研究室到目前為止至少開發了 4 套系統，用「至少」是因為這 4 套比較大型，除 django 程式碼外，自己所寫的
.py 及 .js 近 4 萬行，且不含樣版。而這 4 套系統當然有部份的程式碼是一樣的，我想程式碼寫得多的設計師一定也是這麼想，常用的 bug
紀錄器、郵政地址選擇、政府機關資料等東西，一定會弄個模組另外放，到時候開發新系統時，整個模組(資料夾)拿進來就行了。

但是一個模組該如何與主系統共存開發呢? 尤其是模組與主系統程式碼都還在變動階段。
使用 Mercurial 讓這件事，變得非常輕鬆，假設我們有 A, B, C, D 等 4 個系統，而有一個 common 模組，這時，我們應該在
common 模組開 4 個 branches ，分別是


-   'release for A
-   ''releasr for B
-   ''release for C'
-   'release for D'

假設這 4 個 branches 都是在 changeset:300 時 branch 出去的。然後，過了一段時間，因為 C 系統的需求，我們修改了
common 模組，它的 changeset 來到了 340 ，且我們也將這 300:340 的修改 merge 到 'release for C'
了，這樣對其他 3 個系統有沒有影響? 當然沒有。

因為在伺服器運作的儲存庫上，以 A 系統為例，一定是把 common 模組切到 'release for A' 了(用 hg update -C
'release for A' 這個指令)，就算某天將 A 系統上的 common 更新至 changeset:340 ，但這也只有在
common/.hg 的資料是 340 的， common/* 的資料一定還是停在 'release for A' 這個 branch 上，而
'release for A' 的最新版仍舊是 300 。

所以那天如果負責 A 系統的程設師有空了，它想使用 common 模組的最新功能時，他只要在 'release for A' 的 branch 中，
merge tip 版本，並處理 A 系統這邊應對新 common 模組的修改，就可無痛昇級。

利用 branch 觀念，我們可以輕鬆整合多種函式庫、模組之間的版本整合問題，那麼學弟的問題是什麼呢?
如下圖：

`.. image:: http://2.bp.blogspot.com/_eKM9lHjTZjs/S_eUI4VFJ1I/AAAAAAAACig/nTE
onPwIdXk/s400/Screenshot.jpg
`_

學弟很貼心地在 branch 後，再為 " default 分枝" 作一個 manual commit ，以維持兩個 heads
，這樣會讓其他人在使用時，不致於出現 +1 head 的訊息(但這也只是在某些情況下)。

結果我後來又把 " default 分枝" 的成果 merge 到 'Release for XXX' ，這讓儲存庫上只剩下 1 個 head
，這個結果讓學弟有點困惑，他以為剩下一個 head ，那其他人在寫程式時，會不小心 commit 錯 branch 。
我說不會，因為他們原本手頭上的儲存庫就指定好是用那一種 branch ，所以在 hg pull -u 後，程式碼會變成該 branch
的最新版，在改完程式後，他們 commit 的成果也寫入相同的 branch ，而不會在 " default 分枝" 上， commit 到
'Release for XXX' 。

這惟一的小問題是其他學弟要把 commit 後的成果 push 到 HG Server 時，會出現提醒 +1 head 的訊息，但這是沒辦法避免的，用
hg push -f 就解決，因為既然 branch 了，就一定會有 multi heads 的情形。

.. _如下圖：: http://2.bp.blogspot.com/_eKM9lHjTZjs/S_eUI4VFJ1I/AAAAAAAACig/n
    TEonPwIdXk/s1600/Screenshot.jpg


.. author:: default
.. categories:: chinese
.. tags:: mercurial
.. comments::
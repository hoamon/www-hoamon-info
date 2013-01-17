================================================================================
在分散式版本控制器中使用 Fork 來輔助 Branch
================================================================================

.. figure:: branches_in_another_fork.png
    :align: center
    :width: 600px

    2f40672 乃 default branch; 以其為基礎，向上開設 6 個 branches

團體協同程式開發時，在新舊功能開發及維護之際，在人員分工不同元件之際，\
我們往往利用 branch 方式來孤立程式碼的撰寫，使其不與其他元件相混。

然 branch 的使用常常使程式新手不知所措，甚而把程式碼攪得比義式麵條更難分更解。\
本文即介紹另一種方法： fork ，在某些環境下，可輔助程式新手得到類似利用 branch 的功能。

.. more::

其實 fork 就是 clone ，只是當我們把儲存庫放置於 `Bitbucket.org <https://bitbucket.org/>`_ \
或 `Github.com <https://github.com/>`_ 時，\
它能幫我們把 https://bitbucket.org/hoamon/A fork 成 https://bitbucket.org/hoamon/B 。\
不然，我們通常使用 clone 指令，把 https://bitbucket.org/hoamon/A 下載成 local_A 專案，\
再把 local_A 專案佈置到 https://hg.you-domain.com/B 去。

因為 hg, git 的分散式控制特性，所以當我們把專案 clone 到另一個伺服器 https://bitbucket.org/hoamon/B 去操作時，\
它的意義就像是開了 branch 一樣，差別是開 branch 方式是可以讓整個團隊都收到 changeset ，\
而放到另一個伺服器則只有能讀取該伺服器的工程師看得到你所修改的 changeset 。

接下來，筆者以自身的個人網站專案為範例。筆者的個人網站 https://bitbucket.org/hoamon/www-hoamon-info ，\
主要是放置個人資訊及部落格文章之用，因為是公開資訊，所以在 bitbucket 上管理時，\
就直接開 public 專案。然而，某些部落格文章在撰寫時，並不是一蹴可及，\
如果文章寫作手法是埋兵伏將，前文論點與後文大相逕庭，\
若是文章寫到一半， push 到 public 儲存庫後，被好奇之人率先解讀，反而會造成不少困惱。

為此，筆者將 www-hoamon-info fork 到 https://bitbucket.org/hoamon/www-hoamon-info-drafts ，\
並在 www-hoamon-info-drafts 作草稿文章的寫作，待定稿後才 push 回 www-hoamon-info 專案。\
而 www-hoamon-info-drafts 就設定為 private 專案以避免過早洩露資訊。

bitbucket 的 fork 按鈕如下圖：

.. figure:: fork_button.png
    :align: center
    :width: 600px

點選後，出現新專案的資訊填寫表單：

.. figure:: new_repo.png
    :align: center
    :width: 600px

其中要注意的是 fork 時，也可針對該專案的不同 tags, branches 作選擇，\
若是選擇某一 branch 或是 tip 本身就是某一個 branch ，\
則 hg clone 的行為是把該 branch 最頂頭的那個 changeset 抓出來，\
並一路往它的父 changeset 抓取。這樣子的 fork 是看不到其他 branch 的最頂頭 changeset 的。

所以對一個不太敢用 branch 的工程師，他可以先用 fork 頂著，當他要開發 a1 元件時，\
就把原專案 fork 到 xxx-a1 ，然後在這裡修修改改; 要開發 b3 元件時，\
再從原專案 fork 到 xxx-b3 去修改。等 xxx-a1 元件修改完成後，就特別指定 push 的任置，\
把 xxx-a1 的 changeset push 回 https://bitbucket.org/hoamon/xxx 去。\
如果遇到 xxx 已有他人新增的 changeset ，那新手工程師也只要 pull xxx -u 回來，作一次 merge ，\
就能把 xxx-a1 所有修改全 push 回 xxx 了。下面命令列是開發 xxx-a1 時，對應上面腳本所用到的指令：

.. code-block:: bash

    hoamon@nb ~/ $ hg clone https://bitbucket.org/hoamon/xxx-a1
    hoamon@nb ~/xxx-a1 $ cd xxx-a1
    hoamon@nb ~/xxx-a1 $ #"Do someting one; write codes..."
    hoamon@nb ~/xxx-a1 $ hg commit -m "write note one"
    hoamon@nb ~/xxx-a1 $ #"Do someting two; write codes..."
    hoamon@nb ~/xxx-a1 $ hg commit -m "write note two"
    hoamon@nb ~/xxx-a1 $ #"Do someting three; write codes..."
    hoamon@nb ~/xxx-a1 $ hg commit -m "write note three"
    hoamon@nb ~/xxx-a1 $ hg pull -u https://bitbucket.org/hoamon/xxx #抓原專案的新 changeset
    hoamon@nb ~/xxx-a1 $ hg merge
    hoamon@nb ~/xxx-a1 $ hg di #檢查別人寫的東西，沒問題就 commit
    hoamon@nb ~/xxx-a1 $ hg commit -m "merge for ..."
    hoamon@nb ~/xxx-a1 $ hg push #預設值是 push 到 https://bitbucket.org/hoamon/xxx-a1
    hoamon@nb ~/xxx-a1 $ hg push https://bitbucket.org/hoamon/xxx #這是 push 到 xxx

--------------------------------------------------------------------------------
Fork + Branch
--------------------------------------------------------------------------------

又如果你是一位還算了解 branch 用法的程式設計師，那一樣是可以利用 Fork 形式來\
幫你整理程式碼。

像是原專案已經有多個程式設計師開了 branch 在修改了，你覺得不想再湊上一腳。\
而且手上多個元件，自己也得開多個 branch 來處理，如果別人的再加上自己的，那不會天下大亂嗎? \

以我的個人網站為例，把 www-hoamon-info fork 到 www-hoamon-info-drafts 後，\
我開始要撰寫多篇文章，但把每篇文章視為一個元件，希望在撰寫時，不要互有影響。\
於是以 2f40672 changeset 為底，陸續建立 6 個 branches ，一篇文章一個。待完成一篇，就把該 \
branch 關閉，並 merge 回 default ，再 push 到 https://bitbucket.org/hoamon/www-hoamon-info 。\
以下是相關的指令：

.. code-block:: bash

    hoamon@nb ~/www-hoamon-info-drafts $ hg update default
    hoamon@nb ~/www-hoamon-info-drafts $ hg branch "article one" #建立文章一的 branch
    hoamon@nb ~/www-hoamon-info-drafts $ hg add somefile_1.rst
    hoamon@nb ~/www-hoamon-info-drafts $ # write some note for somefile_1.rst
    hoamon@nb ~/www-hoamon-info-drafts $ hg commit -m "write note for somefile_1"
    hoamon@nb ~/www-hoamon-info-drafts $ hg update default #要再回到 default branch
    hoamon@nb ~/www-hoamon-info-drafts $ hg branch "article two" #建立文章二的 branch
    hoamon@nb ~/www-hoamon-info-drafts $ hg add somefile_2.rst
    hoamon@nb ~/www-hoamon-info-drafts $ # write some note for somefile_2.rst
    hoamon@nb ~/www-hoamon-info-drafts $ hg commit -m "write note for somefile_2"
    hoamon@nb ~/www-hoamon-info-drafts $ ... #建立多篇文章的 branch
    hoamon@nb ~/www-hoamon-info-drafts $ hg update "article two" #要回到 article two branch
    hoamon@nb ~/www-hoamon-info-drafts $ # write some lines for somefile_2.rst
    hoamon@nb ~/www-hoamon-info-drafts $ hg commit --close-branch -m "done for somefile_2" # 假設得到的是 123:abc1234 的 changeset
    hoamon@nb ~/www-hoamon-info-drafts $ hg update default
    hoamon@nb ~/www-hoamon-info-drafts $ hg merge -r abc1234
    hoamon@nb ~/www-hoamon-info-drafts $ hg commit -m "merge for article two"
    hoamon@nb ~/www-hoamon-info-drafts $ hg push #預設值是 push 到 https://bitbucket.org/hoamon/www-hoamon-info-drafts
    hoamon@nb ~/www-hoamon-info-drafts $ hg push --new-branch "article two" https://bitbucket.org/hoamon/www-hoamon-info #這是 push 到 www-hoamon-info

如下圖，我完成 "Rights of People Own Guns" 一文後，把該 branch 合併至 default ，\
得到 7ecfcfc changeset 。這是 www-hoamon-info-drafts 的分枝圖。

.. figure:: forked.png
    :align: center
    :width: 600px

把 7ecfcfc push 到 www-hoamon-info 後，可以從下圖看到， www-hoamon-info 也只會拿到 7ecfcfc 母系的所有 changeset ，\
在這裡看不到 skill_of_teacher 、 do_my_best 、 colombo …等 branch 的 changeset 。

.. figure:: original.png
    :align: center
    :width: 600px

利用 fork+branch ，我就能確保自己開的 branches 不會與別人開的 branches 有太多彼此互相影響的機會，\
降低程式碼攪亂的機會。

--------------------------------------------------------------------------------
重點提示
--------------------------------------------------------------------------------

在 push 回原專案時，用 hg push --new-branch "article two" 時，\
這 --new-branch "article two" 的意思是限定只送出 "article two" branch 的 changeset ，\
要不然它會視為你是要把手頭上( fork 出來的那個儲存庫)的所有 changeset 全 push 出去。

.. author:: default
.. categories:: chinese
.. tags:: python, mercurial, bitbucket
.. comments::

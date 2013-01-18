如何處理「合併(merge)錯誤的 hg 儲存庫」? 就是再用「merge」來復原!
================================================================================

學弟把我們已經作好的分枝要合併進主線時，不知怎麼搞地 merge 得非常混亂，而且也 push -f 進 hg 伺服器。

我們總共有三種分枝： 'default', 'Release for XXX', 'convert to InnoDB'，這次是要把 'convert
to InnoDB' 的成果合併進 'default' ，再合併到 'Release for XXX' 。'convert to InnoDB' 是我們將
`django-based 的系統從 MyISAM 引擎改到 InnoDB`_ 所作的程式碼修改。主要的修改是發生在索引上，因為原本有一個地方設定了
unique_together = (('name', 'uplevel_id'), ) ，而它會造成 MySQL Error code
1071錯誤('Specified key was too long; max key length is 767 bytes')，因為 name
的原長度是 256 ，而我們又使用 utf8 ，所以它的實際長度為 256 * 3 = 768 ，但在 InnoDB 的索引中，限制為 767
以下，所以我們必須將 name 的長度限制為 255 。

當我改完程式碼後，就請學弟們在自己的本機上測試，如果沒問題的話，就作合併的動作，並送到實際運作的網站去。

結果，他合出了下面這個東西：

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/TJ9TtJT5IhI/AAAAAAAACmQ/dXs
FxL4a1qE/s400/1.+original.png
`_

D 版是我的分枝成果，我希望他把 D 合併到 B 跟 C 中。但他生出了 E, F, G, H 。這 4 個版本都不是我想要的。

一開始，我的作法是再次作手動合併，結果我迷失在那些修改的程式碼中，花了快 3 個小時，依舊無法解開，所以我當時用下策來處理，就是以 hg strip
指令把 hg 伺服器上的 E ~ H 的版本洗掉。然後重作合併。

這個方法十分爛，但當下，剛好沒有人上傳程式碼，而我又陷在那堆程式碼中，所以我選了這個作法。

這種作法，會有一個大問題，如果有人在未刪除版本前，就作了 pull, update ，那麼下次他在 push 時，就會出現衝突。他一定會 merge
到亂掉，因為他手上的 E ~ H 版本的程式碼不具含意，所以他也無法以程式碼內含意義來作合併，這樣他會像我一樣陷入毛線當中。

所以，在我解決 hg 伺服器上的亂象後，我靜下心來仔細思考，才發現我何必管 E ~ H 作了什麼事呢! 我只要在 merge 時，忽略它們的修改就行啦!

首先，我 clone 一個 LOCAL 儲存庫，而且只 clone A, B, C, D 之前的版本。作法必須分兩次，因為 clone
只會把該版本的媽媽下載下來，所以像是 A, B, C, D 4 個版本，卻有 2 個 heads ，我就得分兩個指令來下載，指令如下：

$ hg clone https://SERVER/my_software LOCAL -r C
$ cd LOCAL
$ hg pull -u -r D

然後，依我原本想要的合併方式處理：

$ hg ci -m '"convert to InnoDB" branch ...' --close-branch #P.S. 這個作法事後會造成問題
*1
$ hg merge -r B
$ hg ci -m WRITE_f'_COMMIT_MESAGE # 產生 f'
$ hg merge -r C
$ hg ci -m WRITE_g'_COMMIT_MESAGE # 產生 g'

這樣 LOCAL 的版本圖就像下圖一樣。

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/TJ9TtKX5tZI/AAAAAAAACmI/J9T
YX2l19zE/s400/2.+local.png
`_

再來，我把伺服器上的錯誤版本 clone 到本機的 SERVER-FIX ，然後在 SERVER-FIX 中依 branch 作合併，最後合併出
'convert to InnoDB' 及 'Release for XXX' 兩種 heads ，指令如下：

$ hg clone https://SERVER/my_software SERVER-FIX
$ cd SERVER-FIX
$ hg update -C H
$ hg merge -r E
$ hg ci -m WHATEVER_MESSAGE

成果如下圖：

`.. image:: http://2.bp.blogspot.com/_eKM9lHjTZjs/TJ9Ts4mdQEI/AAAAAAAACmA/XON
JTvmxWKk/s400/3.+server-fix.png
`_

接下來，我回到 LOCAL 儲存庫中，把 changeset push 到 SERVER-FIX 中，成果如下圖：

`.. image:: http://4.bp.blogspot.com/_eKM9lHjTZjs/TJ9Tskgo_QI/AAAAAAAACl4/eQf
lXm3RWpQ/s400/4.+merge_server-fix_local.png
`_

最後，我要作的就是把 I, G, g' 三者合而為一，而且要在 merge 時，完全忽略 I, G 的程式碼修改，怎麼作呢? 指令如下：

$ cd SERVER-FIX
$ hg update -C g'
$ hg merge -r I
$ hg status
M models.py
$ hg cat -r g' models.py > models.py # I 版的修改，只在 models.py 上，而我又用 g' 版的
models.py 把 I 版修改完全洗掉了
$ hg ci -m MERGE_g'_I_MESSAGE
$ hg merge -r G
$ hg status
M models.py
$ hg cat -r g' models.py > models.py # G 版的修改，只在 models.py 上，而我又用 g' 版的
models.py 把 G 版修改完全洗掉了
$ hg ci -m MERGE_g'_I_G_MESSAGE

最後成果如下圖：

`.. image:: http://1.bp.blogspot.com/_eKM9lHjTZjs/TJ9TsTVGcBI/AAAAAAAAClw/JF3
upQCUW3A/s400/5.+done.png
`_

再為各位整理一下，合併「錯誤的 hg 儲存庫」步驟：

1. 在本機上，重作一個完全正確的 LOCAl 儲存庫。
2. 在本機上，重現一個與伺服器相同的 SERVER-FIX 儲存庫，並依 branch 作合併，讓一個 branch 只有一個 head 。
3. 將 LOCAL 的成果 push 到 SERVER-FIX 中。
4. 讓 SERVER-FIX 中的 head 與 LOCAL 的 tip 合併。而且在合併時，完全消除程式碼的修改，讓它們合併完，程式碼是與
    LOCAL 的 tip 程式碼完全相同。
5. 確認無誤，就能 push 到 hg 伺服器了。

以這種方式處理完的 hg 伺服器，才可以讓所有人都免去再次合併 E~H 這段錯誤程式碼的痛苦。

基本上， hg 的主要運作方法，就是要讓所有人習慣在自己的本機上， merge 自己與其他人的成果，如果你能順暢地走完 1 ~ 4
的步驟，也代表你足以應用 hg 在大部份的程式碼修改工作了。

註1 我太早在 'convert to InnoDB' 分枝上下 --close-branch ，所以我後來在使用 hg update -C
'convert to InnoDB' 時，它居然是 update 到 I 版，而不是 e' 版。

.. _django-based 的系統從 MyISAM 引擎改到 InnoDB:
    http://hoamon.blogspot.com/2010/09/django-based-myisam-innodb.html
.. _結果，他合出了下面這個東西：: http://3.bp.blogspot.com/_eKM9lHjTZjs/TJ9TtJT5IhI/AAA
    AAAAACmQ/dXsFxL4a1qE/s1600/1.+original.png
.. _這樣 LOCAL 的版本圖就像下圖一樣。: http://3.bp.blogspot.com/_eKM9lHjTZjs/TJ9TtKX5t
    ZI/AAAAAAAACmI/J9TYX2l19zE/s1600/2.+local.png
.. _成果如下圖：: http://2.bp.blogspot.com/_eKM9lHjTZjs/TJ9Ts4mdQEI/AAAAAAAACmA
    /XONJTvmxWKk/s1600/3.+server-fix.png
.. _接下來，我回到 LOCAL 儲存庫中，把 changeset push 到 SERVER-FIX 中，成果如下圖：: http://4.b
    p.blogspot.com/_eKM9lHjTZjs/TJ9Tskgo_QI/AAAAAAAACl4/eQflXm3RWpQ/s1600/4
    .+merge_server-fix_local.png
.. _最後成果如下圖：: http://1.bp.blogspot.com/_eKM9lHjTZjs/TJ9TsTVGcBI/AAAAAAAAC
    lw/JF3upQCUW3A/s1600/5.+done.png


.. author:: default
.. categories:: chinese
.. tags:: mercurial, hg
.. comments::
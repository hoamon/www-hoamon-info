命令列比較好!!(範例篇)
================================================================================

早想寫一篇有關使用命令列及選單介面的效率、任務達成困難性比較。

如果我說使用命令列比較有效率、能達成更困難的工作(do more with less)，但是不容易。你相信嗎？

應該是相信吧!畢竟，我都已經強調"不容易"了。只是你一定很難想像黑黑的螢幕加上難按的鍵盤如何工作？

這篇文章就是讓你有一個概念來想像"命令列文化"的博大精深。

在了解命令列及選單介面的差別前，我先來十個命令列技巧：

1.快速刪除層層資料夾中的特定檔案：
[amon@amon amon]$ rm -r `find .|grep "amon[^/]\+.jpg$"`


2.抓取螢幕快照：
三秒後，對整個螢幕拍照
[amon@amon amon]$ sleep 3;xwd -root|xwdtopnm|pnmtojpeg >test.jpg


3.抓取整個網站的內容：
[amon@amon amon]$ wget -c -r http://www.amon.idv.tw/


4.只想聽音樂：
[amon@amon amon]$ mpg123 */*.mp3
[amon@amon amon]$ ogg123 */*.ogg


5.影像處理：
將input.jpg圖檔插入一串文字"測試"，然後順時針旋轉45度再轉存為output.png
[amon@amon amon]$ convert -font /mnt/BP/fonts/ngulim.ttf \
>-encoding Unicode \
>-fill black \
>-pointsize 48 \
>-draw 'text 100,200 "'`echo 測試|iconv -f Big5 -t UTF8`'"' \
>-rotate 45 \
>input.jpg output.png


6.Ping目前的區網中，那些電腦是開機的：
[amon@amon amon]$ nmap -sP 192.168.100.1-254|grep "Host"|cut --delimiter=" "
-f2


7.抓取unicode.org的gif圖檔(六萬餘筆)
[amon@amon amon]$ perl -e \
>'print "wget -c http://www.unicode.org/cgi-
bin/refglyph?24-",sprintf("%04X",$_), \
>" -O ",sprintf("%04X",$_),".gif\n" for (19968..20000)'>tt
[amon@amon amon]$ sh tt


8.分析apache的log檔，得到不同小時的使用人數：
[amon@amon httpd]$ perl -ne 'print $1, "\n" if /\[ [^:]+Sad\d\d).* \]/x'
access_log* \
> |sort|uniq -c|perl -ne 'print $2, "\t", $1, "\n" if /(\d+)\s+(\d+)/' >~/x
[amon@amon httpd]$ gnuplot
gnuplot> plot "/home/amon/x"
gnuplot> set output "/home/amon/x.png"
gnuplot> set term png
gnuplot> replot
[amon@amon httpd]$ display /home/amon/x.png


9.快速大量更改檔名，將x-y.jpg改成00002306xxxxyyyy.jpg，例如1-1.jpg改為000023060010001.jpg：
工作上的需要，我得掃瞄大量的日治時期總督府檔案，而其圖檔的命名規則為 000 02306 001 0001
四個區塊，000表總督府檔案，02306表冊號，001表文件件號，0001表頁碼。因為在頁碼部份時常跳號，例如：0003-0009的檔案為大於
A3尺寸，並不用掃瞄，所以無法利用ACDSee之類的軟體幫我作批次改檔名。
一冊的圖檔多為350頁上下，如果在掃瞄時直接鍵入，那麼我得按15*350=5250次的數字鍵，想到就累。於是我在一開始鍵檔名時，只鍵了 1-
1.jpg、2.jpg、3.jpg、4-2.jpg、6.jpg…349-14.jpg、350.jpg等(頁碼在前、件號在後)，然後用命令列來改檔名。
[amon@amon pic]$ ls >../t
[amon@amon pic]$ perl -ne '$a = $1 if /-(.*)\./;print $a, "\n"' ../t >../t_l
[amon@amon pic]$ perl -ne '$a = $1 if /^(\d+)[-\.]/;print $a, "\n"' ../t
>../t_r
[amon@amon pic]$ paste -d. ../t_l ../t_r >../lr
[amon@amon pic]$ perl -ne 'printf("00002306%03d%04d.jpg\n", $1, $2)
if/(.+)\.(.+)/' ../lr >../long_lr
[amon@amon pic]$ paste ../t ../long_lr > ../all
[amon@amon pic]$ perl -ne 'chop;system "mv $_"' ../all
如此一來，我後面的幾百冊都可以直接套用上面7行指令，豈不快哉。


10.終極必殺技-關機：
[root@amon root]$ shutdown -h 21:00
[root@amon root]$ shutdown -h +10
[root@amon root]$ shutdown -k time to maintain
[root@amon root]$ shutdown -r +10


有趣吧!指令列有沒有超乎你的想像呢!!本篇還未完成。畢竟題目說的是"比較好"，所以總要寫個對照組吧! 下回我會把它和選單模式來作一個真正的比較。

Old Comments in Blogger
--------------------------------------------------------------------------------



`薛 <http://www.blogger.com/profile/07363986516234346633>`_ at 2007-11-05T23:18:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

就用這一篇來比較指令列與圖型介面的易用性（不管是易於使用/完成工作）

1.快速刪除層層資料夾中的特定檔案：
[amon@amon amon]$ rm -r `find .|grep "amon[^/]\+.jpg$"`
其實find指令有支援動作參數，其中包含delete，不用特意使用``再丟給rm來刪，而且如果find出來的內容太長是無法運作的，到時候要配合xargs反
而弄的更麻煩，另外-r參數是不必要的，因為不是刪資料夾；grep有點多餘，正規表示法也用的不是時候，用“find . -name amon*.jpg
-delete”就可以了
使用圖型介面的作法是搜尋“amon*.jpg”然後刪掉，大部份的Windows使用者皆會使用搜尋，但大部份的Linux使用者不見得會使用find
-delete

2.抓取螢幕快照：
三秒後，對整個螢幕拍照
[amon@amon amon]$ sleep 3;xwd -root|xwdtopnm|pnmtojpeg >test.jpg
單一功能就不用比較了吧，這只是秀命令列的能力（Windows土法煉鋼的作法就有按精可用）

3.抓取整個網站的內容：
[amon@amon amon]$ wget -c -r http://www.amon.idv.tw/
同上，單一功能免比較（這…這好像IE有內建）

4.只想聽音樂：
[amon@amon amon]$ mpg123 */*.mp3
[amon@amon amon]$ ogg123 */*.ogg
其實用mplayer就好了啊？（略）

5.影像處理：
將input.jpg圖檔插入一串文字"測試"，然後順時針旋轉45度再轉存為output.png
[amon@amon amon]$ convert -font /mnt/BP/fonts/ngulim.ttf \
>-encoding Unicode \
>-fill black \
>-pointsize 48 \
>-draw 'text 100,200 "'`echo 測試|iconv -f Big5 -t UTF8`'"' \
>-rotate 45 \
>input.jpg output.png
用小畫家會不會快一點…（同1，一定要轉45度的話找photoXXX吧）

6.Ping目前的區網中，那些電腦是開機的：
[amon@amon amon]$ nmap -sP 192.168.100.1-254|grep "Host"|cut --delimiter=" "
-f2
嗯…還是單一功能，掃網芳的軟體好像都會附加這個功能

7.抓取unicode.org的gif圖檔(六萬餘筆)
[amon@amon amon]$ perl -e \
>'print "wget -c http://www.unicode.org/cgi-
bin/refglyph?24-",sprintf("%04X",$_), \
>" -O ",sprintf("%04X",$_),".gif\n" for (19968..20000)'>tt
[amon@amon amon]$ sh tt
還是一樣，用Xi好像不用想那麼多（還是同1）

8.分析apache的log檔，得到不同小時的使用人數：
[amon@amon httpd]$ perl -ne 'print $1, "\n" if /\[ [^:]+Sad\d\d).* \]/x'
access_log* \
> |sort|uniq -c|perl -ne 'print $2, "\t", $1, "\n" if /(\d+)\s+(\d+)/' >~/x
[amon@amon httpd]$ gnuplot
gnuplot> plot "/home/amon/x"
gnuplot> set output "/home/amon/x.png"
gnuplot> set term png
gnuplot> replot
[amon@amon httpd]$ display /home/amon/x.png
雖然此功能有軟體內建了，不過既然用在伺服器注重的是資源OK啦

9.快速大量更改檔名，將x-y.jpg改成00002306xxxxyyyy.jpg，例如1-1.jpg改為000023060010001.jpg：
工作上的需要，我得掃瞄大量的日治時期總督府檔案，而其圖檔的命名規則為 000 02306 001 0001
四個區塊，000表總督府檔案，02306表冊號，001表文件件號，0001表頁碼。因為在頁碼部份時常跳號，例如：0003-0009的檔案為大於
A3尺寸，並不用掃瞄，所以無法利用ACDSee之類的軟體幫我作批次改檔名。
一冊的圖檔多為350頁上下，如果在掃瞄時直接鍵入，那麼我得按 15*350=5250次的數字鍵，想到就累。於是我在一開始鍵檔名時，只鍵了 1-
1.jpg、2.jpg、3.jpg、4-2.jpg、6.jpg…349-14.jpg、350.jpg等(頁碼在前、件號在後)，然後用命令列來改檔名。
[amon@amon pic]$ ls >../t
[amon@amon pic]$ perl -ne '$a = $1 if /-(.*)\./;print $a, "\n"' ../t >../t_l
[amon@amon pic]$ perl -ne '$a = $1 if /^(\d+)[-\.]/;print $a, "\n"' ../t
>../t_r
[amon@amon pic]$ paste -d. ../t_l ../t_r >../lr
[amon@amon pic]$ perl -ne 'printf("00002306%03d%04d.jpg\n", $1, $2)
if/(.+)\.(.+)/' ../lr >../long_lr
[amon@amon pic]$ paste ../t ../long_lr > ../all
[amon@amon pic]$ perl -ne 'chop;system "mv $_"' ../all
如此一來，我後面的幾百冊都可以直接套用上面7行指令，豈不快哉。
基本上我還是沒搞清楚一定不能用ACDSee改名的理由，如果需要更強的判斷式只需要上toget找一找，前陣子還有看到可自訂函數的改名工具（有需要我可以找出來
）
不過基本上都要動到函數的話而又已經寫好判斷式這點OK啦

10.終極必殺技-關機：
[root@amon root]$ shutdown -h 21:00
[root@amon root]$ shutdown -h +10
[root@amon root]$ shutdown -k time to maintain
[root@amon root]$ shutdown -r +10
定時關機已經不是新鮮事了，Windows內建也有此功能，如果使用軟體還能做更多

總結來看，使用命令列來完成以上的事與使用圖型介面相比所付出的代價好像有點太高了
至少，裡面有超過一半的事是大部份Windows使用者會，大部份Linux使用者不會的
而使用Windows的人基本上在使用一段時間後都能完成上面大部份的事，但使用Linux一段時間卻不見得能完成上面的事（指命令列）

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2007-11-05T23:56:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

這篇文章是我在學習了 Linux 約一年時(大概是在 5 年前，這麼說我玩 Linux 也有 6 年了，與 blogspot
時間對不上的原因是這文章是從別的系統轉來的)所寫的，一直沒有更新，但對我來說，在作類似上面的功能時，我大概不脫那幾個指令，有比較長進的，那就是 find
的參數多懂了幾個， Perl 多半改用 Python 取代了。

當時的時空背景是我用了 Windows 3年， Linux 1 年，在我發現了命令列後，開始覺得電腦真的很好玩，幾乎沒什麼事作不到，而在 Windows
上，可能是因為我沒上軟體王、 pchome 上找些有趣的軟體，所以那時候，我在 Windows 上作的工作大概只有 MS Office、Matlab、VB
、CD-Bruning，還滿無趣。

而經你( 薛 )這麼比較，這 10 個命令列範例已經無法讓現今的圖形介面使用者驚豔了，但在當時可是讓我覺得 Linux 是天下無敵的。

不過，話說回來，我還滿有自信打這 10 個指令的速度，會比點滑鼠還快。哈哈哈~~

`薛 <http://www.blogger.com/profile/07363986516234346633>`_ at 2007-11-06T01:17:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

其實Windows一直都沒有變，這些事98也能做到，而XP更加方便，XP應該可以說是微軟最成功的系統了，Vista是最大的敗筆（至少目前還這麼覺得），指令
嘛…我認為真的不會比較快，以第一條來說，除非那台電腦是開個搜尋視窗都要讀個10秒的老電腦，不然基本上檔名打下去、delete按下去檔案就刪掉了，而打指令還
要稍微想一下語法、參數
對大部份的人來說，他們不需要專研一堆技術只為了換來讓一件事簡單一點點，就像是我不會花大把的錢買Intel CPU只為了讓電腦再快一點點，使用者只要弄到稍微
懂一點點，然後就可以慢慢摸出功能，這樣就夠了，現實面老闆要你刪除檔案是不會等你說“等我研究一下find參數要怎麼下”，也不會聽你說“等我研究完這個判斷式改
檔名可以快點”除非你的身份就是工程師，工作就是研發程式讓員工工作更有效率，平常沒在工作也不要緊（就是我啦= =）
基本上現在的Linux是很強沒錯，但非常缺乏軟體，所以當你有一個特殊需求時基本上如果這是一個單一需求（大部份是的）那麼你找Windows軟體通常會比找Li
nux方案來的快點、多點
Linux是天下無敵這點我同意，至少在我理解了Linux的系統架構時（非使用者架構…強調==）我也是這麼覺得，至少…一些異想天開的想法使用Linux來實現
會比Windows快的多，例如…嗯…還是那個魔速網芳限速精靈最經典（沒打錯字），朋友知道了都說不可思議
我覺得，易於完成工作還是要建立在易於理解使用上，就像今天新聞那個什麼阿里巴巴的什麼雲講的，這個東西我用都不會用我只會把它丟到垃圾桶，不管它有多好用，沒錯，
因為我不能使用它它就是沒用

`何岳峰 hoamon <http://www.blogger.com/profile/03979063804278011312>`_ at 2008-08-03T03:26:00.000+08:00:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我剛看了一下，在 Windows 檔案總管內好像無法用「正規表示式」尋找檔案。

這一點， Linux find 及 Linux grep 又勝了一籌。

當然啦~ 一般的使用者根本不會聽過「正規表示式」，又談何使用。

但本文的重點是「使用命令列比較有效率、能達成更困難的工作(do more with less)，但是不容易」。

所以並不適合一般使用者。本文是適合不想再當一般使用者的一般使用者的。

.. author:: default
.. categories:: chinese
.. tags:: linux, shell script
.. comments::
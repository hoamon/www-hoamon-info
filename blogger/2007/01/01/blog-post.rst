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

.. author:: default
.. categories:: chinese
.. tags:: linux, shell script
.. comments::
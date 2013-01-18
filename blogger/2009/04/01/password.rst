明碼的 password 實在是很傷惱筋耶
================================================================================

通常，我遇到的系統管理員如果是 Linux/Un*x 玩得比較久的也才會對這個明碼 password 有戒心。其他 Windows 或是 Linux
菜鳥就顯得無所謂了，甚至他們還會想要告訴我他們的密碼是什麼! 或許是我不容易遇到高級 Windows 系統管理員吧!

所以，當我在寫網頁程式或是系統管理程式時，這資料庫或是其他系統密碼是不會寫在程式碼中的，因為我們的程式都會放到版本控制器去，且在開發團隊中是不太會鎖權限的
，所以如果我們成員有人笨笨地把帳密流出去，那上面的程式碼一定會被其他人看光光，當然，我絕對不介意別人看我的程式，怕的是他們發現我們系統上的其他帳密(雖然我
的機器一律使用公私錀，但還是怕，因為我沒發覺的洞實在是很多)。

而我的作法是把帳密放到設定檔，並且把這個設定檔檔名加上 .example 來提醒其他人記得參照這個 example 檔來修改成適當的內容。

但是用在系統管理檔中，就覺得有點麻煩了，像是定時備份資料庫的 script ，不過就那麼 10 多行，如果還得另外讀個設定檔，就有給它多此一舉了。

還好 MySQL 提供一個在 Linux/Unix 下的用法，在執行備份 script 的帳號家目錄中，放置一個 .my.cnf 檔，其內容為

[client]
password=some_paSSwoRD

然後把 ~backupmysql/.my.cnf 的權限設為 600 。這樣你就可以在 /etc/crontab 寫入

/usr/bin/sudo -u backupmysql /some/path/backup_mysql_script

而 /some/path/backup_mysql_script 的內容，可以如下：

mysqldump -u root --database test > /home/backupmysql/test.sql

如此一來，將 backup_mysql_script 作版本控制後，也不會有人曉得你的 mysql root 密碼是什麼了!

.. author:: default
.. categories:: chinese
.. tags:: mysql, linux, shell script
.. comments::
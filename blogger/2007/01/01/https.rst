公私錀應用在網路通訊上(https部份)
================================================================================

什麼是https呢?一般如果你有過線上刷卡的經驗，那麼你就有使用https的機會了，平常你瀏覽網頁時，網址的開頭都是http，這代表你是使用 http協定
與遠端的網頁伺服器作網頁要求的動作，然而http協定是不會把你跟網頁伺服器說的話作加密的動作的，所以，掌管你網路的系統管理員絕對有能力及機會知道你和伺服器
要求什麼樣的網頁(不要懷疑，hinet、seednet的管理員絕對是可以看到的，只是要不要而已)，像是你看過那些美美的圖片啦、什麼人寄了什麼的信給你呀(當
你使用yahoo的webmail時)、發表什麼內容的文章…等。所以如果你在線上刷卡時，還是使用http協定的話，那我想網路管理員應該會更有錢點。

在傳送極度機密資料時，都應該使用https協定，這也是銀行會在提供線上刷卡時必須使用https協定讓使用者刷卡的原因。本討論區也是使用了 https協定，
主要有兩個理由，一是筆者的帳號/密碼都是一樣地，如果你過濾出這個ops討論區中我所使用的帳號/密碼，那也知道我所有管理機器的密碼了，二是我不想讓各地的pr
oxy server快取這個ops討論區的內容，這個討論區我希望是小眾的、專屬於會員的。

https的使用是很簡單，像ssh的tips一樣，先把公私錀生出來，然後放對位置，再重新啟動你的網頁伺服器即可啦。

首先生成公私key，

# openssl req -new > your_define.csr

過程中會要求你輸入your_define.csr的密碼，先隨便輸入4個字以上的密碼，這個your_define.csr只是設定過程中的產物，最後的成品與它
無關，所以它的密碼也就隨便設吧!接著輸入你的國家代碼、州名(省名)、縣市名、組識名、單位名、主機名、系統管理員email等。最後的兩個項目，我也不知道該輸
入什麼，但是沒輸也沒有關係。

# openssl rsa -in privkey.pem -out your_define.key

輸入剛設定your_define.csr的密碼來產生your_defice.key

# openssl x509 -in your_define.csr -out your_define.crt -req -signkey
your_define.key -days 3560

-days 3650表這個公私錀會在10年才過期。
到這裡表示公私錀已成功完成了，接下來更改你的/etc/httpd/conf.d/ssl.conf。

......
......
SSLCertificateFile /where_you_stored/your_define.crt
SSLCertificateKeyFile /where_you_stored/your_define.key
......
......


這個檔在你安裝mod_ssl.xxx.rpm後才會出現。
最後重新啟動你的apache就可以了。

注意：使用apache的老手可能會很習慣一個ip設很多虛擬網站，但是在https上，因為ssl layer比http layer還要早溝通完畢，所以一個i
p只能使用一對公私錀，這在你有兩個以上的虛擬網站時，如果你的公私錀名字定為a.hoamon.info，那當使用者連到b.hoamon.info時，會出現「
這個憑證名字為a.hoamon.info，但你所要連線的網站是b.hoamon.info，有可能是有人要截斷你與伺服器之間的通訊，你確定要繼續連線嗎?」

這個問題目前是無解的。只有多設幾個ip才行。

.. author:: default
.. categories:: chinese
.. tags:: linux, apache
.. comments::
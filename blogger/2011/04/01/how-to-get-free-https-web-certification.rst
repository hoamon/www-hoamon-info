How to get a free HTTPS web certification authority by StartSSL.com
================================================================================

一般在上網時，所用的 Http 協定是明碼的，使用者與網站伺服器之間的任何網路結點(閘道器)都有方法可以看到網路連線所傳遞的訊息，所以如果網站所提供的服務
關係到機密(隱私)資料時，我都會讓網站用 Https 加密協定服務。




使用 Https 服務時，有一個重要觀念： 如何拒絕「中間人攻擊」。




假想一個以 Https 加密協定服務的 A 網站，在它與使用者傳遞公錀(加密憑證)時，是被一個中間人接走，而中間人再把它自己的公錀傳遞給使用者，結果使用者
傻傻地使用中間人的公錀加密，再把加密資訊傳到中間人，而中間人用自己的私錀解密後，再用 A 網站公錀加密傳回 A 網站，在這個模式，雖然使用的是 Https
協定，但資料還是被中間人看光光了。




所以要防止此類攻擊，就必須讓使用者能「確認」公錀真的是 A
網站的。方法是使用者自己手頭上要有一些公認機構所發行的公錀憑證(一般的瀏覽器都已經包入)，然後在拿到 A
網站的公錀憑證時，用手頭上已有的公認機構公錀憑證去驗證這個 A 網站的公錀憑證是否被這些公認機構簽核過，如果有，則表示公錀的確就是 A
網站的，當使用者用這把公錀加密時，就只能被 A 網站解密。




本篇文章的目的是站在 A 網站的立場上，如何將 A 網站的公錀交給公認機構作簽核，這樣使用者在瀏覽 A 網站時，才不會跳出一個警示視窗告知使用者：「 A
網站有安全疑慮」。




一般將公錀交給公認機構去作簽核是要花錢的，像是國內最大的簽證公司(我猜的)網際威信最便宜的簽核年費是 `18000`_
元。這筆費用不是每個人願意負擔的，像是我的 https 網站，主要是提供我們團隊作專案管理之用，也就不到 10 位的使用者，要我花 18000
元，去買一個「讓使用者在一年之內不會看到該網站有安全疑慮」的警告訊息，這我可花不下手。




所幸，有`公認機構`_了解這種需求，它以「給非商業網站一年免費」作廣告宣傳，如果有更高級的簽核需求，它才額外收費。那麼以我上述所要的，其實就拿那個「一年免
費」用用即可。




首先請使用 Firefox (它們目前不支援 Chrome)去瀏覽 `http://www.startssl.com/`_
，並點選右上角的錀匙圖示，如下圖：




`.. image:: http://1.bp.blogspot.com/-8ZEiBUkbyCU/Tapjb99h8DI/AAAAAAAAC50/8yR
1XD1BO9A/s400/auth.png
`_




就能看到 Sign-up 按鈕，如下圖：




`.. image:: http://3.bp.blogspot.com/-rknUblr0uGk/TapaNmBQrRI/AAAAAAAAC5s/jf8
hssa1FgU/s400/ssl-01.png
`_





按下 Sign-up 按鈕就開始註冊帳戶的流程，整個公錀簽核的程序分成三個階段：

1.  註冊帳戶
2.  驗證網址
3.  公錀簽核

1. 註冊帳戶時， startssl 會給你的瀏覽器一個全新的公私錀檔，這個公私錀檔是專供你的帳戶使用的，這個公私錀檔要好好保管，搞丟了，你就不能
    再用這個帳戶申請簽核的動作，因為它的登入不是用帳號密碼作登入機制，而是用公私錀作登入機制。




2. 驗證網址，你必須證明要作簽核的網址是你所管理的。而這個驗證動作完成後，你也只有 30 天的期限去作簽核它的公錀，過期後，就必須再次驗證網址。




3. 針對已驗證過的網址，你可以申請簽核公錀的動作，主要分兩種作法，一是 startssl 完全生出一把全新的公私錀憑證;
    二是我們自己生出私錀及公錀請求檔，再把公錀請求檔交給 startssl
    去作出已簽核的公錀。本文是介紹第二種方法，因為私錀應該是自己處理會比較妥當，不要懶惰到連解密錀匙也委託他人製造，我個人認為這種人不只懶還不負責任。




``_原則上，公錀不過是一個文字檔，所以它在 Linux, Window$, Mac 作業系統下，都能處理，但`我個人還是喜歡用 Linux
來作這件事`_。




1. 註冊帳戶：


`.. image:: http://2.bp.blogspot.com/-qPOnO5vrR2I/TapaKiZrhjI/AAAAAAAAC5k
/Pe5Qw-GOKjA/s400/ssl-02.png
`_




請填寫你的詳細資料，原則上，他們只採 web 審核，所以只要你的資料不要「太假」，他們都會通過。**但如果你要為商業網站申請憑證的話，這就不能開玩笑了，因
為你買憑證時，它會要你給護照及身份證、駕照的文件作審核。**

``_
`.. image:: http://1.bp.blogspot.com/-2LfHWJqREqY/TapaKkdiryI/AAAAAAAAC5c/sso
EhAi4WTE/s400/ssl-03.png
`_




請到註冊信箱接受具驗證碼的信。並注意「目前的這個視窗」是不允許關閉的，如果你關閉當下這個網頁，再用相同連結回來，這樣你填寫的驗證碼就算是對的，它也不會通過
你的申請。

``_
`.. image:: http://3.bp.blogspot.com/-ITN3i3TxxrE/TapaKTbtxbI/AAAAAAAAC5U/-4w
m4SWDQdI/s400/ssl-04.png
`_




產生「帳戶」專用的公私錀檔，可選擇 Hign Grade 。

``_
`.. image:: http://1.bp.blogspot.com/-yNhdc29FcU8/TapaKL64ThI/AAAAAAAAC5M/xkE
ON5Oqx7s/s400/ssl-05.png
`_




將公私錀檔安裝至瀏覽器上，這裡的公私錀檔是指你的帳戶與 startssl 網站溝通時，所用的公私錀檔，而不是你的網站要用的公錀。

``_
`.. image:: http://4.bp.blogspot.com/-i8lTJE7t0SM/TapaJ5mEY0I/AAAAAAAAC5E/y8u
Z1_MWZeQ/s400/ssl-06.png
`_




建議你備份這份公私錀檔。

``_
`.. image:: http://1.bp.blogspot.com/-RGjbRexiBN0/TapaCJa40SI/AAAAAAAAC48/hQz
VoTBV4sU/s400/ssl-07.png
`_




``_完成後，可見到帳戶頁面。




2. 驗證網址：


`.. image:: http://2.bp.blogspot.com/-X8ZFKe-
RIGE/TapaBygO2BI/AAAAAAAAC40/vXS3akoVZNs/s400/ssl-08.png
`_




我是選擇 Domain Name Validation 方式。

``_
`.. image:: http://2.bp.blogspot.com/-Bx4ARqCgKIg/TapaBuWPfBI/AAAAAAAAC4s/gXm
opESp7YA/s400/ssl-09.png
`_




填入網址。

``_
`.. image:: http://3.bp.blogspot.com/-K0xDwKS8Fjo/TapaBpTU64I/AAAAAAAAC4k/bl5
0_uOxO8E/s400/ssl-10.png
`_




startssl 會從 whois 資料中抓出管理員信箱，所以你必須確認該網址的 whois 內容是正確的。

``_
`.. image:: http://4.bp.blogspot.com/-DafmcUTgSAQ/TapaBctW8uI/AAAAAAAAC4c/5YQ
ZacVFlSI/s400/ssl-11.png
`_




請到信箱收取驗證碼。並填入上面的 Verification Code 中。

``_
`.. image:: http://4.bp.blogspot.com/-nai5Kz8T_9w/TapZ6WtePDI/AAAAAAAAC4U/ltM
192MYpAM/s400/ssl-12.png
`_




成功後，你只有 30 天的時間，去簽核該網站的公錀檔。




3. 簽核公錀：

``_
`.. image:: http://1.bp.blogspot.com/-OdB3j6YgmJY/TapZ6RYz00I/AAAAAAAAC4M/_Bl
0KnpG4ro/s400/ssl-13.png
`_




公錀可以有很多種用途( Email/XMPP/Object Code )，但目前我只需要 Web 的，所以選擇 Web Server SSL/TLS
certificate 。

``_
`.. image:: http://1.bp.blogspot.com/-ZsXmNLwDd7A/TapZ57ldIhI/AAAAAAAAC4E/0sZ
83-YDnn8/s400/ssl-14.png
`_




要使用自己獨立生成的私錀來作簽核公錀的動作，請選擇 Skip 。




欲生成長度為 4096 bits 的私錀檔並使用 des3 格式作私錀加密(密碼長度要大於 4 個字元)，請使用如下指令：


# openssl genrsa -des3 -out exmple.com.key 4096
Generating RSA private key, 4096 bit long modulus
.............................................................................
.............................................................................
......++
...............................................++
e is 65537 (0x10001)
Enter pass phrase for exmple.com.key:
Verifying - Enter pass phrase for exmple.com.key:

從新增的私錀中，產生一個憑證請求檔，並在請求檔中，寫入「目標網址」(也就是你剛驗證過的那個網址)的所屬資料，如：所在地、單位名稱、負責人信箱等：

# openssl req -new -key exmple.com.key -out exmple.com.csr
Enter pass phrase for exmple.com.key:
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:{{TW}}
State or Province Name (full name) [Some-State]:{{Taichung}}
Locality Name (eg, city) []:{{Taichung}}
Organization Name (eg, company) [Internet Widgits Pty Ltd]:{{EXAMPLE-
Company}}
Organizational Unit Name (eg, section) []:{{EXAMPLE-Company}}
Common Name (eg, YOUR name) []:{{EXAMPLE Company}}
Email Address []:{{master@exmple.com}}

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:




兩個 {{ }} 所包住的部份，請自己修改成正確資料。

``_
`.. image:: http://4.bp.blogspot.com/-bKuP2sans4o/TapZ5_fEu7I/AAAAAAAAC38/TZ4
ETwaFgtk/s400/ssl-15.png
`_




在 Linux 完成 CSR 檔的製作後，你會得到 example.com.csr 檔案，請將檔案內容貼入上圖的文字框中。




`.. image:: http://2.bp.blogspot.com/-1OYiG61krw0/TapZ5vNL8FI/AAAAAAAAC30/UUD
h27gAOlU/s400/ssl-16.png
`_




CSR檔如無誤，它會出現上圖的訊息。

``_
`.. image:: http://2.bp.blogspot.com/-OMovbnxOl4U/TapZvzCejyI/AAAAAAAAC3s/Uil
X1qgCiGQ/s400/ssl-17.png
`_




它要你選擇要生成簽核公錀的頂層網域。

``_
`.. image:: http://4.bp.blogspot.com/-XTZUu1hsbPo/TapZvbFmGQI/AAAAAAAAC3k/NTg
osxMRsiU/s400/ssl-18.png
`_




請填入你所提供 https 服務的網址名稱。

``_
`.. image:: http://1.bp.blogspot.com/-fl_-
Z3t2aW8/TapZvKR4nyI/AAAAAAAAC3c/w4zDDt2ByTM/s400/ssl-19.png
`_




確認要簽核公錀的網址。 startssl 簽核的公錀，預設會給你的目標網域及它的頂層網址兩個。如果你要簽核公錀的網址希望是 *.example.com
，也就是除頂層網域外，把它的下層網域一網打盡，也是可以，只要二年付 USD 49.9 即可，大約 1500 元的新台幣，而且這是 wild cards
網址，網際威信可沒這麼好康，一個就要 18000 元、二個就是要 36000 元。這時，我又感到「全球化」的愉悅。

``_
`.. image:: http://4.bp.blogspot.com/-Lt_sktMzq5Y/TapZu7NgubI/AAAAAAAAC3U/Sqb
zhtakfQI/s400/ssl-20.png
`_




接下來，請把文字框中的文字貼到 example.com.crt 中，這個內容即已被簽核過的公錀檔。另外，請順便下載上圖中的 intermediate 及
root 兩個 CA 檔案。

``_
`.. image:: http://1.bp.blogspot.com/-Z9BYdvv4Pg0/TapZuiIiQbI/AAAAAAAAC3M
/ZXOPthN-HSM/s400/ssl-21.png
`_




``_整個工作完成了。

然後在 Apache 設定檔中設定如下：
::SSLEngine on
    SSLProtocol all -SSLv2
    SSLCipherSuite ALL:!ADH:!EXPORT:!SSLv2:RC4+RSA:+HIGH:+MEDIUM
    SSLCertificateFile /etc/apache2/example.com.crt
    SSLCertificateKeyFile /etc/apache2/example.com.key
    SSLCertificateChainFile /etc/apache2/sub.class1.server.ca.pem
    SSLCACertificateFile /etc/apache2/ca.pem
    SetEnvIf User-Agent ".*MSIE.*" nokeepalive ssl-unclean-shutdown重新啟動
    Apache 時，它會問你私錀密碼為何?
    這個動作在管理員面前發生是沒有問題的，但在系統自動重開機時，會造成困惱，所以我們可移除私錀的加密，指令如下：

# openssl rsa -in exmple.com.key -out exmple.com.key.no_password

exmple.com.key.no_password 這個私錀檔就是沒加密的，將它寫入 apache 設定檔即可。

.. _18000: http://www.verisign.com.tw/ssl/buy-ssl-certificates/compare-
    ssl-certificates/
.. _公認機構: http://www.startssl.com/
.. _ ，並點選右上角的錀匙圖示，如下圖：: http://1.bp.blogspot.com/-8ZEiBUkbyCU/Tapjb99h8DI
    /AAAAAAAAC50/8yR1XD1BO9A/s1600/auth.png
.. _就能看到 Sign-up 按鈕，如下圖：: http://3.bp.blogspot.com/-rknUblr0uGk/TapaNmBQr
    RI/AAAAAAAAC5s/jf8hssa1FgU/s1600/ssl-01.png
.. _我個人還是喜歡用 Linux 來作這件事: http://hoamon.blogspot.com/2009/02/windows-
    https.html
.. _1. 註冊帳戶：:
    http://2.bp.blogspot.com/-qPOnO5vrR2I/TapaKiZrhjI/AAAAAAAAC5k/Pe5Qw-
    GOKjA/s1600/ssl-02.png
.. _但如果你要為商業網站申請憑證的話，這就不能開玩笑了，因為你買憑證時，它會要你給護照及身份證、駕照的文件作審核。: http://1.bp.
    blogspot.com/-2LfHWJqREqY/TapaKkdiryI/AAAAAAAAC5c/ssoEhAi4WTE/s1600/ssl-0
    3.png
.. _，如果你關閉當下這個網頁，再用相同連結回來，這樣你填寫的驗證碼就算是對的，它也不會通過你的申請。: http://3.bp.blogspo
    t.com/-ITN3i3TxxrE/TapaKTbtxbI/AAAAAAAAC5U/-4wm4SWDQdI/s1600/ssl-04.png
.. _產生「帳戶」專用的公私錀檔，可選擇 Hign Grade 。: http://1.bp.blogspot.com/-yNhdc29FcU8
    /TapaKL64ThI/AAAAAAAAC5M/xkEON5Oqx7s/s1600/ssl-05.png
.. _將公私錀檔安裝至瀏覽器上，這裡的公私錀檔是指你的帳戶與 startssl 網站溝通時，所用的公私錀檔，而不是你的網站要用的公錀。: htt
    p://4.bp.blogspot.com/-i8lTJE7t0SM/TapaJ5mEY0I/AAAAAAAAC5E/y8uZ1_MWZeQ/s1
    600/ssl-06.png
.. _建議你備份這份公私錀檔。: http://1.bp.blogspot.com/-RGjbRexiBN0/TapaCJa40SI/AAAAA
    AAAC48/hQzVoTBV4sU/s1600/ssl-07.png
.. _2. 驗證網址：: http://2.bp.blogspot.com/-X8ZFKe-
    RIGE/TapaBygO2BI/AAAAAAAAC40/vXS3akoVZNs/s1600/ssl-08.png
.. _我是選擇 Domain Name Validation 方式。: http://2.bp.blogspot.com/-Bx4ARqCgKI
    g/TapaBuWPfBI/AAAAAAAAC4s/gXmopESp7YA/s1600/ssl-09.png
.. _填入網址。: http://3.bp.blogspot.com/-K0xDwKS8Fjo/TapaBpTU64I/AAAAAAAAC4k/
    bl50_uOxO8E/s1600/ssl-10.png
.. _startssl 會從 whois 資料中抓出管理員信箱，所以你必須確認該網址的 whois 內容是正確的。: http://4.bp.b
    logspot.com/-DafmcUTgSAQ/TapaBctW8uI/AAAAAAAAC4c/5YQZacVFlSI/s1600/ssl-11
    .png
.. _請到信箱收取驗證碼。並填入上面的 Verification Code 中。: http://4.bp.blogspot.com/-nai5
    Kz8T_9w/TapZ6WtePDI/AAAAAAAAC4U/ltM192MYpAM/s1600/ssl-12.png
.. _3. 簽核公錀：: http://1.bp.blogspot.com/-OdB3j6YgmJY/TapZ6RYz00I/AAAAAAAAC
    4M/_Bl0KnpG4ro/s1600/ssl-13.png
.. _公錀可以有很多種用途( Email/XMPP/Object Code )，但目前我只需要 Web 的，所以選擇 Web Server
    SSL/TLS certificate 。: http://1.bp.blogspot.com/-ZsXmNLwDd7A/TapZ57ldIhI/
    AAAAAAAAC4E/0sZ83-YDnn8/s1600/ssl-14.png
.. _兩個 {{ }} 所包住的部份，請自己修改成正確資料。: http://4.bp.blogspot.com/-bKuP2sans4o/Ta
    pZ5_fEu7I/AAAAAAAAC38/TZ4ETwaFgtk/s1600/ssl-15.png
.. _在 Linux 完成 CSR 檔的製作後，你會得到 example.com.csr 檔案，請將檔案內容貼入上圖的文字框中。: http:/
    /2.bp.blogspot.com/-1OYiG61krw0/TapZ5vNL8FI/AAAAAAAAC30/UUDh27gAOlU/s1600
    /ssl-16.png
.. _CSR檔如無誤，它會出現上圖的訊息。: http://2.bp.blogspot.com/-OMovbnxOl4U/TapZvzCejyI
    /AAAAAAAAC3s/UilX1qgCiGQ/s1600/ssl-17.png
.. _它要你選擇要生成簽核公錀的頂層網域。: http://4.bp.blogspot.com/-XTZUu1hsbPo/TapZvbFmGQI
    /AAAAAAAAC3k/NTgosxMRsiU/s1600/ssl-18.png
.. _請填入你所提供 https 服務的網址名稱。: http://1.bp.blogspot.com/-fl_-
    Z3t2aW8/TapZvKR4nyI/AAAAAAAAC3c/w4zDDt2ByTM/s1600/ssl-19.png
.. _確認要簽核公錀的網址。 startssl 簽核的公錀，預設會給你的目標網域及它的頂層網址兩個。如果你要簽核公錀的網址希望是
    *.example.com ，也就是除頂層網域外，把它的下層網域一網打盡，也是可以，只要二年付 USD 49.9 即可，大約 1500
    元的新台幣，而且這是 wild cards 網址，網際威信可沒這麼好康，一個就要 18000 元、二個就是要 36000
    元。這時，我又感到「全球化」的愉悅。: http://4.bp.blogspot.com/-Lt_sktMzq5Y/TapZu7NgubI/AAA
    AAAAAC3U/SqbzhtakfQI/s1600/ssl-20.png
.. _接下來，請把文字框中的文字貼到 example.com.crt 中，這個內容即已被簽核過的公錀檔。另外，請順便下載上圖中的
    intermediate 及 root 兩個 CA 檔案。:
    http://1.bp.blogspot.com/-Z9BYdvv4Pg0/TapZuiIiQbI/AAAAAAAAC3M/ZXOPthN-
    HSM/s1600/ssl-21.png


.. author:: default
.. categories:: chinese
.. tags:: linux, ssl, https, openssl, windows, mac
.. comments::
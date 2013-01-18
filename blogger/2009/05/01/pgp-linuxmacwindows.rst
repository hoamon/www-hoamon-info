如何使用 PGP (Linux/Mac/Windows 皆適用)來加解密及簽章驗證
================================================================================

最簡單的方式就是安裝 `GnuPG`_, `Firefox`_, `FireGPG`_ 。`但為什麼要用 PGP 呢?`_

`GnuPG`_: 是作業系統上的應用程式，其功能是以 PGP 公私錀作文章或檔案的加解密及簽章之用。其操作介面為命令列模式。
`FireGPG`_: 是 Firefox 的外掛套件，它的功能是提供操作 GnuPG 程式的圖形介面。
`Firefox`_: 不用說了吧! 現在還有人不知道 Firefox 是幹什麼的嗎?

上面程式都安裝好後，請打開 Firefox > 工具列 > 工具 > FireGPG > 金錀管理程式，如下圖：

`.. image:: http://3.bp.blogspot.com/_eKM9lHjTZjs/SfuADAyBCPI/AAAAAAAAB2o/LTx
3yM26WzY/s400/Screenshot-Key+manager.png
`_

我已經有一些金錀(有些是公錀，有些是私錀，但一律顯示公錀編號)了，綠色框是名稱及註釋、黑色框是 email 、黃色框是金錀編號、紅色框是信任程度。

如果是自己產生的金錀，則同時擁有公私錀，如果是別人給的金錀，則只有公錀。我們都是拿公錀來加密，然後用私錀來解密的，或是用私錀來簽章，再用公錀來驗證。

如果你還沒有金錀，請按下[New Key]，然後填寫


1.  Name(最好是別人認得出你的名字)
2.  Email(必須吻合你使用的email，否則使用你公錀的人會誤會這把公錀的真實使用者是誰?)
3.  註釋(可簡單說明你是誰)
4.  密碼(這是用來鎖住私錀的，以防止你的私錀不小心落入別人手上，如果沒有這個密碼，別人也無法拿這把私錀來作解密的動作。同樣地，如果你忘了這個密
    碼，那麼你的公錀也就無用，且過去別人用該公錀加密的內容，你也解不開了，請慎重。)
5.  建議點選金錀永遠不失效(Never Expire)。

再來就是按下[產生金錀]了。請耐心等候一段時間。並在此時胡亂開啟你的程式，亂打一些指令或文句，讓這把金錀不致於與別人的金錀重複。

成功產生後，要測試加解密的功能，可打開 Firefox > 工具列 > 工具 > FireGPG > 文字編輯器。

請在文字編輯器中，鍵入文句，完成後請點選加密，此時會詢問你用那把公錀，可以 Ctrl
鍵作複選，完成後，該文句就會變成一堆奇怪的亂碼，此亂碼只有你當初選定的那些公錀所對應的私錀才能作解密的動作。

再按下解密鈕， FireGPG 即會找尋該密文所對應的私錀作解密，如果你的私錀當初有設定密碼，此時，會先詢問你密碼為何! 正確鍵入後，它即為你解密。

接下來，測試作簽章及驗證，一樣打開 Firefox > 工具列 > 工具 > FireGPG > 文字編輯器。

請在文字編輯器中，鍵入文句，完成後請點選簽章，此時會詢問你用那把私錀(只能選定一把)，完成後，該文句後面會出現一段奇怪的驗證碼，此驗證碼只有你當初選定私錀
所對應的公錀才能作驗證的動作。

再按下驗證鈕， FireGPG 即會找尋該驗證碼所對應的公錀作驗證，驗證成功後，會顯示私錀的公開資訊(名稱、註釋、email、公錀編號)及簽章時間。

上面的工作都可正確使用後，接下來，就是把公錀傳給其他人。有二種方式，一種是[匯出至檔案]，一種是[匯出至伺服器]。

匯出至檔案後，你可以透過第三方管道(像是隨身碟、email、放在blog 上)把公錀傳遞給其他人，這樣別人在收到公錀後檢查它的 fingerprint
或是公錀編號是否與你真實公錀相同，相同時就可確定這把公錀的確是你所屬的。但此法的缺點是不容易更新公錀內容(什麼，公錀不是一開始產生後，就一直用下去嗎?
為什麼會有變動。欲知詳請，請待`下篇`_分解)。

另一種方式[匯出至伺服器]，則是把公錀上傳至某一伺服器( FireGPG 的預設值是 subkeys.pgp.net )，然後跟其他人告知你的公錀編號及
fingerprint ，讓其他人到 subkeys.pgp.net
去下載。此法在使用上比較便利，省去了自行傳檔的功夫，一律要求其他人到公錀伺服器上抓取。

當你把公錀上傳至伺服器後，你就要廣為宣傳你的公錀編號、email，慎重一點的，還可以註明 fingerprint 。像我的處理方式就是放在
`http://hoamon.blogspot.com/`_ 及 `http://www.hoamon.info/#AboutMe`_
中，以及我在實體名片及信件簽名檔上都放了公錀編號、 email 及 fingerprint 。方便其他人比對公錀的真實性。但請注意一點，如果你是用網路形式
來比對公錀編號的話，它會有一定程度的不可信，因為你不知道你的閘道器管理員有沒有動過手腳，最好的確認方式是與公錀主人面對面比對
*1，再次之是電話比對(已經有風險了)，其他方法的風險就更高了。

註1: 如果你看過天龍特攻隊的話，或許你就會知道「面對面比對」也是有風險的，因為你不知道對方是不是「小白」。

當大家都擁有你的公錀時，就能寄送加密文本給你，如此一來，絕對可以保證，發文者與收文者之間沒有人可以破解此一加密文本。

不過，以上兩種匯出方法，所匯出的都只是公錀，如果想要匯出私錀來作備份的話，就必須打指令了，記得公錀不用作備份，它是可以從私錀中產生的。但其實也非常簡單，指
令如下(Windows 用戶請到你的 GnuPG 安裝位置中打該指令)：

# gpg -a --export-secret-keys {XXX} > private_key.txt

{XXX} 可以是 email 位置，也可以是公錀編號。匯出後，私錀內容就存在 private_key.txt 中。請慎重保管此檔。

又如果你想要把某個檔案作加密，也是得使用命令列來達到，如下(可用多把公錀加密)：

# gpg -r {XXX} -r {YYY} -e {some_filename_you_want_to_encrypt}

解密則直接下

# gpg -d {some_fileame} > new_filename

.. _GnuPG: http://www.gnupg.org/
.. _Firefox: http://http//www.moztw.org/
.. _FireGPG: http://tw.getfiregpg.org/
.. _但為什麼要用 PGP 呢?: http://hoamon.blogspot.com/2009/05/google-pgp.html
.. _上面程式都安裝好後，請打開 Firefox > 工具列 > 工具 > FireGPG > 金錀管理程式，如下圖：: http://3.bp
    .blogspot.com/_eKM9lHjTZjs/SfuADAyBCPI/AAAAAAAAB2o/LTx3yM26WzY/s1600-h
    /Screenshot-Key+manager.png
.. _下篇: http://hoamon.blogspot.com/2009/05/pgp.html
.. _http://hoamon.blogspot.com/: http://hoamon.blogspot.com/
.. _http://www.hoamon.info/#AboutMe: http://www.hoamon.info/#AboutMe


.. author:: default
.. categories:: chinese
.. tags:: gpg, linux, windows, mac, firegpg, pgp
.. comments::
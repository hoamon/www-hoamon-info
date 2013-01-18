Python及PHP的公私鑰加密方法
================================================================================

昨天費了好大的一番勁，終於可以在 Python 中作公私鑰的處理，忙完了 Python 這邊，再往 PHP
去作，居然只花30分鐘。這最大的原因我想是出在一開始我完全不知道加解密該如何處理，所以我有些時間是花在私錀加解密上，而且 Python
這邊的模組還真是多，我試玩了 5 個，才找到我要的東西。分別是：


1.  python-crypto - 這個模組是基本模組，使用的函式太複雜了，不會用。
2.  ezPyCrypto - 這個簡單些了，但他作出來的公私鑰無法與其他程式相容(這一點，我也不知道為什麼)。
3.  SSLCrypto - 與 ezPyCrypto 是相同作者，而這個模組的效率比 ezPyCrypto 好。但一樣不能與其他程式相容。
4.  pyopenssl - 作者說他不欣賞 M2Crypto 與 SWIG 介接的方式，是的，我也不欣賞。但 pyopenssl 似乎是用
    https 通訊上的，而我找不到加解密的用法。
5.  M2Crypto - 終於讓我找到了。但它有一大缺點。它底層是用 SWIG 來與 OpenSSL 介接的，而 SWIG 程式在
    Windows 上非常難裝。

M2Crypto 在 ubunto 6.06.01 及 fedora core 5 中都有了。只是我還是用 PyPi 上的 0.17 版。而安裝方式是：


-   先安裝 python2.4-pyrex 、 libssl-dev 、 swig 。
-   到 m2crypto 資料夾執行 sudo python setup.py install


接下來，測試 M2Crypto 模組，因為我希望這個模組所用的公私鑰可與其他程式互動，所以用 openssl 來產生公私鑰。產生方法：

# openssl genrsa -out rsaprivate.pem 2048
# openssl rsa -in rsaprivate.pem -out rsapublic.pem -pubout -outform PEM

這樣我們就有兩支鑰匙了。接下我們用 Python with 私鑰 加密。

from M2Crypto import RSA

def test_encrypt(padding):
----msg="The magic words are squeamish ossifrage."
----priv=RSA.load_key('rsaprivate.pem')
----padding=eval('RSA.'+padding)
----ctxt=priv.private_encrypt(msg, padding)
----file = open(' c.txt', 'wb')
----file.write(ctxt)

if __name__ == '__main__':
----test_encrypt('pkcs1_padding')

我們得到了 c.txt 這個加密檔。好了，接下來，要到 Windows 去冒險了。

請先安裝 openssl.exe ，版本須大於 0.9.8 喔~
接下來設定 php.ini ，把 ;extension=openssl.dll 的註解拿掉，重新啟動 Apache2 。這樣你的 PHP 就多了
openssl 相關函式庫了。

接下來執行下面的 PHP 程式，它會用公鑰來解密，最後會得到「String decrypt : The magic words are squeamish
ossifrage.」。恭喜你啦。公私鑰加解密就這麼簡單。

<?php
$fp=fopen ("rsapublic.pem","r");
$pub_key=fread($fp,8192);
fclose($fp);
$fp=fopen ("c.txt","r");
$crypttext=fread($fp,8192);
fclose($fp);
openssl_get_publickey($pub_key);
openssl_public_decrypt($crypttext,$newsource,$pub_key);
echo "String decrypt : $newsource\n";
?>

.. author:: default
.. categories:: chinese
.. tags:: m2crypto, python, openssl, php
.. comments::
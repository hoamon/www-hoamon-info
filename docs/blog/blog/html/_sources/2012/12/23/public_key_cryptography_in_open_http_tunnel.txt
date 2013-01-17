================================================================================
公錀加密在開放式 Http 連線的應用
================================================================================

.. figure:: ssl.png
    :align: center

為某個業主撰寫系統時，遇到他們網路資安單位的"高規格要求"。\
他們只准防火牆開放 80 埠口對外服務，\
而該應用系統又需要寄信服務，在這種限制下。我們只能把寄信功能配置在外部伺服器上，\
讓外部伺服器定時去抓取該應用系統，處理寄信事宜。

但問題是需要寄信的內容，包含了人名、單位及 Email 地址，\
在 `新版個人資料保護法 <http://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=I0050021>`_ 上路後，\
這事變得相當棘手，個資保全的舉證責任是在「被告」身上，而且客戶向業主求償後，\
就換業主向資料管理人員求償，可別錢還沒賺到就賠了一屁股。

.. more::

解決方案是在外部伺服器使用 Https 協定供後台管理人員檢查資料及執行寄信排程，\
而外部伺服器向應用系統索取網頁時，雖是跑在 Http 協定上，\
但應用系統的網頁內容皆先用外部伺服器提供的公錀作加密後再回傳。

但公錀加密的速度及文本長度皆有限制，所以採用 AES 對稱加密錀匙對文本加密，\
再把加密錀匙用公錀加密。

下面是用 AES 演算法作加解密的程式範例：

.. code-block:: python

    import os, base64, random
    from Crypto.Cipher import AES
    from Crypto.PublicKey import RSA
    class AESCrypto:
        u""" plain 文本的字串長度須為 16 的倍數
            利用 pad function 來幫文本後面補上字碼以符合此限制
        """
        BLOCK_SIZE = 32
        PADDING = '{'
        def pad(self, s):
            return s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING
        def EncodeAES(self, s):
            return base64.b64encode(self.cipher.encrypt(self.pad(s)))
        def DecodeAES(self, e):
            return self.cipher.decrypt(base64.b64decode(e)).rstrip(self.PADDING)
        def __init__(self, secret=''):
            if secret:
                self.secret = secret
            else:
                self.secret = os.urandom(self.BLOCK_SIZE)
            self.cipher = AES.new(self.secret)
        def public_key_encypt_secret(self, public_key):
            key = RSA.importKey(public_key)
            return key.encrypt(base64.b64encode(self.secret),
                                random.randint(-10240000, 10240000))
    if __name__ == '__main__':
        ac = AESCrypto()
        encoded = ac.EncodeAES('This is a TTTest')
        decoded = ac.DecodeAES(encoded)
        print decoded # will show up "This is a TTTest"
        # 如果 some_file 是透過網路傳輸得來，通常它會是 b64encode 。
        public_key = base64.b64decode(open('some_file').read())
        encypt_secret = ac.public_key_encypt_secret(public_key)
        # encypt_secret 要回傳給私錀擁有者
        print encypt_secret


其中要注意的是 base64 字串，某些加解密方法的輸出值會是 binary code ，\
為了該它能方便傳輸於不同環境，就要使用 base64 把它轉成純文字符。\
加密錀匙在匯出前先使用公錀加密後才匯出。

在外部伺服器中，則是每次連線就隨機生成一把 rsa 公私錀，把公錀傳給應用系統，\
待抓取應用系統回傳網頁時，先用私錀解開加密錀匙，再用加密錀匙解開加密文本。

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf8 -*-
    import base64, random, urllib, json
    from Crypto.PublicKey import RSA

    def some_view_function(R):
        key = RSA.generate(1024) #隨機生成公私錀
        public_key = base64.b64encode(key.publickey().exportKey())
        url = ('http://some.domain/some_where_funciton/?public_key=%s' % public_key)
        fd = urllib.urlopen(url)
        if str(fd.code) != '200': return HttpResponse('There are Some Error in "%s"'%url)
        content = fd.read()
        ed = json.loads(content)
        secret = base64.b64decode(key.decrypt(base64.b64decode(ed['password'])))
        ac = AESCrypto(secret)
        plain_body = ac.DecodeAES(ed['body']) #得到明碼 body
        ....

雖然應用系統與外部伺服器是用 Http 溝通，但其傳輸內容仍受加密保護，\
而抓回來的資料，可在外部伺服器上瀏覽，此時使用者己經是跑在 Https 上頭了，\
這樣資料從頭(應用系統)到尾(使用者)都有加密，就不失資訊保全要求。

**PS** 外部伺服器的 Https 憑證乃透過筆者的 :doc:`StartSLL.com 帳戶建置 <../../11/05/startssl_com_web_ssl_retailer>` ，\
從文首圖中的組織(O)一欄即可得知。

.. author:: default
.. categories:: chinese
.. tags:: public key cryptography, https, http, python, rsa, aes
.. comments::

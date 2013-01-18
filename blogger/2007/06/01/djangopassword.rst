手動建立django的password
================================================================================

因為在 django 架構中已經包含了使用者認證，所以要照它的規矩處理使用者的密碼。

如果你想要從資料庫中手動加入一個使用者帳號呢?密碼會是你比較麻煩的地方，但其實說麻煩也不麻煩，你只要遵守 hashtype$salt$hash
這個規則就好了。目前可使用的 hashtype 有兩種： md5 及 sha1 ，而 salt 則是讓 hash 字串更亂的種子。製作密碼的程式如下：

from sha import sha
hash = sha('xxx000000').hexdigest() # xxx 就是 salt ，而 000000 則是使用者設定的密碼
print '$'.join(['sha1', 'xxx', hash]) # 結果是
sha1$xxx$7ff010c44c5ed59a6e1171020f9762313234a1cd

就把 sha1$xxx$7ff010c44c5ed59a6e1171020f9762313234a1cd 貼到資料庫的 password 欄位中就行了。



.. author:: default
.. categories:: chinese
.. tags:: django, hash, python, sha
.. comments::